from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from fastapi import Form
import joblib
import pandas as pd
import numpy as np
import faiss
import os

app = FastAPI()

# Load Recommender objects at startup

MODEL_PATH = os.getenv('MODEL_PATH', '/data/movie_recommender_v02.joblib')

with open(MODEL_PATH, 'rb') as f:
    data = joblib.load(f)
    df = data['df']
    embeddings = data['embeddings']
    index = data['index']

# Options for top popular movies
df_sample = df.nlargest(1000, 'vote_count').reset_index(drop=True)

@app.get("/", response_class=HTMLResponse)
def home():
    # Create dropdown options from movie titles
    options = "".join([f'<option value="{title}">{title}</option>' 
                       for title in df_sample['title']])            # Choosing from top 1000 voted movies
    html_content = f"""
    <html>
        <head align='centre'>
            <title>Movie Recommender</title>
            <style>
            body {{
                background: #f0f4f8;
                font-family: 'Segoe UI', sans-serif;
                text-align: center;
                padding: 40px;
            }}
            h2 {{
                color: #333;
                margin-bottom: 20px;
            }}
            select, input[type=number], input[type=submit] {{
                padding: 10px;
                font-size: 16px;
                border: 1px solid #ccc;
                border-radius: 5px;
                margin: 10px;
            }}
            input[type=submit] {{
                background-color: #007BFF;
                color: white;
                border: none;
                cursor: pointer;
            }}
            input[type=submit]:hover {{
                background-color: #0056b3;
            }}
        </style>
        </head>
        <body align='center'>
            <h2>🎬 Movie Recommender System</h2>
            <form action="/recommend" method="post">
                <select name="title">
                    {options}
                </select>
                <input type="number" name="k" value="5" min="1" max="20"/>
                <input type="submit" value="Get Recommendations"/>
            </form>
        </body>
    </html>
    """
    return html_content


@app.post("/recommend", response_class=HTMLResponse)
async def recommend_movies(title: str = Form(...), k: int = Form(5)):
    # Search for movie_id by title
    matches = df[df['title'].str.lower() == title.lower()]
    if matches.empty:
        return f"<h3>Movie '{title}' not found.</h3>"
    movie_id = matches.index[0]

    # Search for top k similar movies
    _, indices = index.search(embeddings[movie_id:movie_id+1], k)

    #Build HTML Table
    table_rows = ""
    for i in indices[0]:
        movie = df.loc[i, ['title', 'genres', 'vote_average', 'spoken_languages']]
        table_rows += f"<tr><td>{movie['title']}</td><td>{movie['genres']}</td><td>{movie['vote_average']}</td><td>{movie['spoken_languages']}</td></tr>"
    html_table = f"""
    <html>
    <head>
        <title>Recommendations</title>
        <style>
            body {{
                background: #f0f4f8;
                font-family: 'Segoe UI', sans-serif;
                text-align: center;
                padding: 40px;
            }}
            table {{
                margin: 20px auto;
                width: 90%;
                border-collapse: collapse;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                background: white;
            }}
            th, td {{
                padding: 12px;
                border: 1px solid #ccc;
            }}
            th {{
                background-color: #007BFF;
                color: white;
            }}
            h2 {{
                margin-bottom: 20px;
                color: #333;
            }}
            a {{
                display: inline-block;
                margin-top: 20px;
                text-decoration: none;
                color: #007BFF;
                font-weight: bold;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <h2>🎥 Recommendations for '{title}'</h2>
            <table>
                <tr><th>Title</th><th>Genre</th><th>Avg Vote</th><th>Languages</th></tr>
                {table_rows}
            </table>
            <a href="/">← Back to Home</a>
    </body>
    </html>
    """
    return html_table
