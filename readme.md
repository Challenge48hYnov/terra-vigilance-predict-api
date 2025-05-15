# Terra Vigilance Predict API

This repository contains a predictive API for Terra Vigilance, which provides predictions for environmental events such as floods and earthquakes based on machine learning models.

## Prerequisites

- macOS, Linux, Windows, or WSL (Windows Subsystem for Linux)
- [uv](https://github.com/astral-sh/uv) - A fast Python package installer and resolver

## Installation

### 1. Install `uv`

#### For macOS or Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### For Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

This will download and install the latest version of `uv` on your system.

### 2. Clone the repository

```bash
git clone <repository-url>
cd terra-vigilance-predict-api
```

### 3. Install dependencies

Use `uv sync` to install all dependencies defined in `pyproject.toml`:

```bash
uv sync
```

## Running the API

Start the API server using `uvicorn` with `uv run`:

```bash
uv run uvicorn api_server:app --reload --host 0.0.0.0 --port 8000
```

This will:

- Start the FastAPI server
- Enable auto-reload for development
- Make the API accessible on all network interfaces at port 8000
- You can access the API at http://localhost:8000

## API Documentation

Once the server is running, you can access the interactive API documentation at:

- http://localhost:8000/docs (Swagger UI)
- http://localhost:8000/redoc (ReDoc)

## API Usage

The API provides a `/predict` endpoint that accepts POST requests with the following JSON structure:

```json
{
  "sismicite": 0.5,
  "concentration_gaz": 1.2,
  "pluie_totale": 25.5,
  "quartier": 3
}
```

The response will include:

- `prediction_code`: Numeric code representing the predicted event(s)
- `prediction_label`: String representation of the predicted event(s)

Example:

```json
{
  "prediction_code": 1,
  "prediction_label": "['innondation']"
}
```

## Project Structure

- `api_server.py` - FastAPI application entry point
- `preprocessor.pkl` - Scikit-learn preprocessing pipeline
- `xgb_model.json` - XGBoost model for predictions
- `lgbm_model.txt` - LightGBM model (alternative)
- `datasets/` - Directory containing structured datasets for different environmental events
  - `inondation/` - Flooding datasets
  - `seisme/` - Earthquake datasets
- `*.ipynb` - Jupyter notebooks for model development and evaluation

## Development

For development work, you can activate a virtual environment with `uv`:

```bash
uv venv
source .venv/bin/activate  # On macOS/Linux
```

## Dependencies

The project uses the following main dependencies (see `pyproject.toml` for the complete list):

- FastAPI - API framework
- XGBoost, LightGBM - Machine learning models
- Pandas - Data manipulation
- scikit-learn - Feature preprocessing
- uvicorn - ASGI server
