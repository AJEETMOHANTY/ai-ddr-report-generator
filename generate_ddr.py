import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found in .env file")

# Configure Gemini
genai.configure(api_key=api_key)

# Use model
model = genai.GenerativeModel("gemini-2.5-flash")


def generate_ddr(merged_data):
    """
    Generate final DDR report using Gemini

    This function:
    1. Removes internal metadata like page/image references
    2. Sends clean structured data to Gemini
    3. Generates professional DDR output
    """

    # -----------------------------------
    # Remove page/image metadata
    # -----------------------------------
    cleaned_data = {}

    for area, details in merged_data.items():

        # Keep thermal summary as it is
        if area == "thermal_summary":
            cleaned_data[area] = details
            continue

        # Remove page/image metadata
        cleaned_data[area] = {
            "issue": details["issue"],
            "thermal_status": details["thermal_status"]
        }

    # -----------------------------------
    # Gemini prompt
    # -----------------------------------
    prompt = f"""
Generate a professional Detailed Diagnostic Report (DDR).

Inspection + Thermal Findings:
{cleaned_data}

Required report format:

1. Property Issue Summary
- Give overall summary of issues

2. Area-wise Observations
For each area use this format:

Area Name:
Issue:
Thermal Validation:
Observation:

Example:

Hall:
Issue: Skirting dampness
Thermal Validation: Moisture detected
Observation: Dampness observed near lower wall skirting.

Bedroom:
Issue: Wall dampness
Thermal Validation: Cold spots detected
Observation: Moisture traces visible on bedroom walls.

3. Root Cause Analysis

4. Severity Assessment

5. Recommendations

6. Missing Information

Rules:
- Do NOT create tables
- Do NOT mention page references
- Do NOT mention image references
- Do NOT use markdown symbols like ** or *
- Keep report professional
- Keep observations structured
"""

    try:
        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        return f"Error generating DDR: {str(e)}"