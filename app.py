import joblib
from ui import build_ui
from utils import predict_salary

# Load the full pipeline (preprocessor + model)
model = joblib.load("models/linear_regression_pipeline.pkl")

# Build Gradio UI
iface = build_ui(model, predict_salary)

if __name__ == "__main__":
    iface.launch()
