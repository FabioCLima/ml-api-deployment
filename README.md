<div align="center">

# ML API Deployment

**FastAPI REST API for sports analytics + ONNX model serving + LangGraph AI toolkit**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-AI%20Toolkit-1C3C3C?style=flat)](https://langchain.com/langgraph)
[![ONNX](https://img.shields.io/badge/ONNX-Model%20Serving-005CED?style=flat)](https://onnx.ai)
[![License](https://img.shields.io/badge/license-MIT-success?style=flat)](LICENSE)

</div>

---

## What This Project Demonstrates

Two production patterns for deploying ML and AI systems:

1. **REST API with FastAPI** — structured data access with SQLAlchemy, Pydantic schemas, and full CRUD operations
2. **ONNX model serving** — deploying trained classification models in a portable runtime format
3. **LangGraph AI toolkit** — an agentic layer built on top of the API for intelligent data querying

---

## Part 1 — Fantasy Football REST API

A read-focused REST API for the Sports World Central (SWC) fantasy football platform.

**Endpoints cover:**
- `/` — health check
- `/players` — list NFL players, search by ID
- `/scoring` — player performance and fantasy points
- `/leagues` + `/teams` — membership and league data
- `/analytics` — aggregate counts and platform stats

**Tech used:** FastAPI · SQLAlchemy · SQLite · Pydantic · pytest

```bash
cd api
pip install -r requirements.txt
uvicorn main:app --reload
# Docs at http://localhost:8000/docs
```

---

## Part 2 — ONNX Player Acquisition Models

Three classification models trained and exported to ONNX format — predicting player acquisition decisions at different thresholds (10%, 50%, 90% probability).

```
chapter13/complete/
├── acquisition_model_10.onnx   # conservative — flag top 10%
├── acquisition_model_50.onnx   # balanced
├── acquisition_model_90.onnx   # aggressive — flag top 90%
├── main.py                     # model loading + inference
└── player_acquisition_model.ipynb
```

ONNX enables model serving without framework lock-in — the same model runs in Python, C++, Java, or on-device.

---

## Part 3 — LangGraph AI Toolkit

An agentic interface that wraps the API with reasoning capabilities — the model can query player data, calculate scores, and answer natural language questions about the fantasy platform.

```
chapter14/complete/
├── langgraph_notebook.ipynb              # ReAct agent querying the API
├── langgraph_notebook_with_toolkit.ipynb # Full toolkit integration
└── swc_toolkit.py                        # LangChain tools wrapping API endpoints
```

---

## Project Structure

```
ml-api-deployment/
├── api/
│   ├── main.py        # FastAPI app
│   ├── models.py      # SQLAlchemy ORM
│   ├── schemas.py     # Pydantic request/response
│   ├── crud.py        # Database operations
│   ├── database.py    # Session factory
│   └── test_main.py   # API tests
├── chapter13/         # ONNX model training + serving
└── chapter14/         # LangGraph AI toolkit
```

---

## Skills Demonstrated

`FastAPI` · `REST API design` · `SQLAlchemy` · `Pydantic v2` · `ONNX model export` · `Model serving` · `LangGraph` · `LangChain tools` · `SQLite` · `pytest` · `OpenAPI/Swagger`
