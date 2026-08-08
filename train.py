from src.data_loader import load_data
from src.model import (
    split_data,
    train_linear_regression,
    train_random_forest,
    evaluate_model,
    save_model
)


def main():
    # Load dataset
    data = load_data("data/final.csv")

    # Split dataset
    X_train, X_test, y_train, y_test = split_data(data)

    # Train Linear Regression
    linear_model = train_linear_regression(X_train, y_train)

    # Train Random Forest
    random_forest_model = train_random_forest(X_train, y_train)

    # Evaluate models
    linear_mae = evaluate_model(
        linear_model,
        X_test,
        y_test
    )

    random_forest_mae = evaluate_model(
        random_forest_model,
        X_test,
        y_test
    )

    print(f"Linear Regression MAE: {linear_mae:.2f}")
    print(f"Random Forest MAE: {random_forest_mae:.2f}")

    # Save Random Forest model
    save_model(
        random_forest_model,
        "models/real_estate_model.pkl"
    )

    print("Random Forest model saved successfully.")


if __name__ == "__main__":
    main()