# Student Performance Prediction System

This project is an end-to-end Machine Learning application that predicts student academic performance based on various input features such as study habits, demographic details, and previous scores.

I built this project to learn how real-world ML systems are developed — from data ingestion and preprocessing to model training, API deployment, and production-ready structure.

---

## Why I Built This Project

I wanted practical experience with:

- End-to-end Machine Learning pipelines
- Data preprocessing and feature engineering
- Model training and evaluation
- Flask / FastAPI deployment
- Logging and exception handling
- Clean project structure used in production systems

---

## Features

- Predict student performance using trained ML model
- Modular pipeline architecture
- Data ingestion and preprocessing
- Feature engineering workflow
- Multiple model training and evaluation
- Hyperparameter tuning
- REST API deployment using Flask / FastAPI
- Structured logging and custom exception handling

---

## Tech Stack

- Python
- Scikit-learn
- Pandas
- NumPy
- Flask
- FastAPI
- Git

---

## Project Structure

```text
student-performance-prediction/
│── app.py                     # Main Flask/FastAPI application
│── requirements.txt           # Python dependencies
│── setup.py                  # Package setup file
│── README.md                 # Project documentation
│
├── artifacts/                # Saved trained models / preprocessors
│
├── notebooks/                # Jupyter notebooks for experiments / EDA
│
├── src/                      # Main source code
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── train_pipeline.py
│   │   └── predict_pipeline.py
│   │
│   ├── logger.py
│   ├── exception.py
│   └── utils.py
│
└── templates/             
