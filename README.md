# Real Estate Price Prediction

## Project Overview

This project predicts real estate prices using machine learning.

The original Week 9 Real Estate code was modularized into separate Python files. Two models are trained:

- Linear Regression
- Random Forest Regressor

The models are evaluated using Mean Absolute Error (MAE). Random Forest gives the lower MAE, so it is saved and used for price prediction.

## Project Structure

```text
Real_Estate_Project/
├── data/
│   └── final.csv
├── logs/
│   └── app.log
├── models/
│   └── real_estate_model.pkl
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── logger.py
│   └── model.py
├── app.py
├── train.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Files

- `train.py` - Trains, evaluates and saves the machine learning model.
- `app.py` - Runs the Streamlit price prediction application.
- `data_loader.py` - Loads the dataset.
- `model.py` - Contains model training, evaluation, saving and loading functions.
- `logger.py` - Records project activities and errors.
- `final.csv` - Dataset used for the project.
- `real_estate_model.pkl` - Saved Random Forest model.

## Model Results

- Linear Regression MAE: 86,948.68
- Random Forest MAE: 46,713.42

Random Forest was selected because it has the lower MAE.

## How to Run

### 1. Install Libraries

```bash
python -m pip install -r requirements.txt
```

### 2. Train the Model

```bash
python train.py
```

This trains the models and creates:

```text
models/real_estate_model.pkl
```

### 3. Run the Application

```bash
python -m streamlit run app.py
```

Enter the property details and click **Predict Price** to get the estimated property price.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit