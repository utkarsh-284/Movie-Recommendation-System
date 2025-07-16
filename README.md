# Movie Recommendation System

A web-based movie recommender system built with FastAPI and FAISS, providing content-based movie recommendations using precomputed embeddings and a trained model.

---

## 🚀 Features
- **Web UI**: Simple, interactive web interface for movie recommendations.
- **Content-Based Filtering**: Uses movie metadata and embeddings for recommendations.
- **Pretrained Model**: Fast, efficient recommendations using a precomputed FAISS index.
- **Dockerized**: Easy deployment with Docker and Docker Compose.
- **Prebuilt Docker Image**: No need to download model/data files separately—just pull and run!

---

## 🗂️ Project Structure
```
Movie-Recommendation-System/
├── app/
│   ├── main.py                # FastAPI app
│   ├── requirements.txt       # Python dependencies
│   └── data/
│       └── movie_recommender_v02.joblib  # Model & data (not in repo)
├── Dockerfile                 # Docker build file
├── docker-compose.yaml        # Docker Compose config
├── Model/                     # Notebooks, raw/processed data, model files
└── README.md                  # This file
```

---

## ⚙️ Requirements
- Python 3.9+
- (Recommended) Docker & Docker Compose

Python dependencies are listed in `app/requirements.txt`.

---

## 🏗️ Setup & Usage

### **Option 1: Use the Prebuilt Docker Image (Recommended)**
You do **not** need to download any model or data files. Everything is included in the image!

```sh
docker pull utkarshbh284/movie-recommendation-system:latest
docker run -p 8000:8000 utkarshbh284/movie-recommendation-system:latest
```
- The app will be available at [http://localhost:8000](http://localhost:8000)

---

### **Option 2: Build and Run Locally (with Docker or Python)**

#### 1. **Clone the Repository**
```sh
git clone https://github.com/utkarsh-284/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

#### 2. **Obtain Model/Data Files**
> **Note:** Large model/data files (`.joblib`, `.pkl`, `.csv`) are NOT included in this repository due to size. You must obtain them separately if you build the image yourself or run locally.

- Download `movie_recommender_v02.joblib` and place it in `app/data/`.
- (Optional) For development or retraining, see the `Model/` directory for notebooks and raw data.

#### 3. **Run with Docker Compose**
```sh
docker-compose up --build
```
- The app will be available at [http://localhost:8000](http://localhost:8000)

#### 4. **Run Locally (Without Docker)**
1. Install Python dependencies:
   ```sh
   cd app
   pip install -r requirements.txt
   ```
2. Ensure `movie_recommender_v02.joblib` is in `app/data/`.
3. Start the app:
   ```sh
   uvicorn main:app --reload
   ```
4. Visit [http://localhost:8000](http://localhost:8000)

---

## 🧠 How It Works
- Loads a precomputed model and FAISS index from `movie_recommender_v02.joblib`.
- Web UI allows users to select a movie and get similar recommendations.
- Uses content-based similarity (embeddings) for fast, relevant results.

---

## 📁 Model & Data Files
- **Not included in repo:** `.joblib`, `.pkl`, `.csv` files (see `app/data/` and `Model/`)
- **How to obtain:**
  - [Provide a download link here, or instructions for requesting the files.]
  - Place `movie_recommender_v02.joblib` in `app/data/` before running (not needed if using the prebuilt Docker image).
- **For retraining:**
  - See Jupyter notebooks in `Model/` for data processing and model building.

---

## 📝 API Endpoints
- `/` (GET): Home page with movie selection form.
- `/recommend` (POST): Returns HTML table of recommended movies for the selected title.

---

## 🐳 Docker Details
- The Dockerfile installs all dependencies and copies the app code.
- The model file is copied into the image at build time. If you update the model, rebuild the image.
- Exposes port 8000.
- **Prebuilt image available:** `utkarshbh284/movie-recommendation-system:latest`

---

## 🙋 FAQ
**Q: Why aren’t model/data files in the repo?**
A: They are too large for GitHub and are not versioned with code. Download them separately as described above, or use the prebuilt Docker image.

**Q: Can I use my own data/model?**
A: Yes! See the notebooks in `Model/` for retraining and generating your own `.joblib` file.

---

## 📣 Credits
- Built with [FastAPI](https://fastapi.tiangolo.com/), [FAISS](https://github.com/facebookresearch/faiss), and [Uvicorn](https://www.uvicorn.org/).
- Model/data processing: [pandas](https://pandas.pydata.org/), [numpy](https://numpy.org/), [joblib](https://joblib.readthedocs.io/).

---

## 📬 Contact
For questions or access to model/data files, please open an issue or contact the maintainer.