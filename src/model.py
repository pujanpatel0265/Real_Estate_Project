import os
import pickle

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

from src.logger import setup_logger


logger = setup_logger()


def split_data(data):
    try:
        # Separate input features and target
        X = data.drop("price", axis=1)
        y = data["price"]

        # Split data into 80% training and 20% testing
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=X["property_type_Condo"]
        )

        logger.info("Data split successfully.")

        return X_train, X_test, y_train, y_test

    except Exception as error:
        logger.error(f"Error splitting data: {error}")
        raise


def train_linear_regression(X_train, y_train):
    try:
        # Create and train Linear Regression model
        model = LinearRegression()
        model.fit(X_train, y_train)

        logger.info("Linear Regression model trained successfully.")

        return model

    except Exception as error:
        logger.error(f"Error training Linear Regression: {error}")
        raise


def train_random_forest(X_train, y_train):
    try:
        # Create and train Random Forest model
        model = RandomForestRegressor(
            n_estimators=200,
            criterion="absolute_error",
            random_state=42
        )

        model.fit(X_train, y_train)

        logger.info("Random Forest model trained successfully.")

        return model

    except Exception as error:
        logger.error(f"Error training Random Forest: {error}")
        raise


def evaluate_model(model, X_test, y_test):
    try:
        # Make predictions
        predictions = model.predict(X_test)

        # Calculate Mean Absolute Error
        mae = mean_absolute_error(y_test, predictions)

        logger.info(f"Model MAE: {mae}")

        return mae

    except Exception as error:
        logger.error(f"Error evaluating model: {error}")
        raise


def save_model(model, file_path):
    try:
        # Create models folder if it does not exist
        os.makedirs("models", exist_ok=True)

        # Save trained model
        with open(file_path, "wb") as file:
            pickle.dump(model, file)

        logger.info("Model saved successfully.")

    except Exception as error:
        logger.error(f"Error saving model: {error}")
        raise
    
    
def load_model(file_path):
    try:
        # Load the saved model
        with open(file_path, "rb") as file:
            model = pickle.load(file)

        logger.info("Model loaded successfully.")

        return model

    except Exception as error:
        logger.error(f"Error loading model: {error}")
        raise
    
#After training, I save the Random Forest model as a pickle file.
# The load_model() function loads that saved model so the Streamlit application can make predictions without training the model again.