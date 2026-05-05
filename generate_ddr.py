import google.generativeai as genai
import os
from dotenv import load_dotenv

# Explicitly load .env from current folder
load_dotenv(dotenv_path=".env")

# Get API key from .env
api_key = os.getenv("GEMINI_API_KEY")

# Debug check
print("Loaded API Key:", api_key)

# Configure Gemini
genai.configure(api_key=api_key)

# Load model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_ddr(merged_data):
    """
    Generate final DDR report using Gemini
    """

    prompt = f"""
    Generate a professional DDR report.

    Input Data:
    {merged_data}

    Include:
    1. Property Issue Summary
    2. Area-wise Observations
    3. Root Cause
    4. Severity
    5. Recommendations
    6. Missing Information

    Do not hallucinate.
    """

    response = model.generate_content(prompt)

    return response.text