from segment_water import detect_water
from forecast_flood import forecast_risk

print("🌊 Welcome to FloodWatch-AI 🌊")
print("Running water detection...")

detect_water("data/sample.jpg")

print("Running flood forecast...")
forecast_risk()
