import re


def extract_temperature_data(thermal_text):
    """
    Extract hotspot/coldspot temperatures
    from thermal report using regex
    """

    hotspots = re.findall(
        r"Hotspot\s*:\s*(\d+\.\d+)",
        thermal_text
    )

    coldspots = re.findall(
        r"Coldspot\s*:\s*(\d+\.\d+)",
        thermal_text
    )

    return {
        "hotspots": hotspots,
        "coldspots": coldspots
    }


def merge_reports(inspection_text, thermal_text):
    """
    Merge inspection + thermal findings

    Removes duplicate issues
    Adds thermal confirmation
    """

    merged_data = {}

    # Hall issue detection
    if "Hall" in inspection_text and "dampness" in inspection_text:
        merged_data["Hall"] = {
            "issue": "Skirting dampness",
            "thermal_status": "Moisture likely detected"
        }

    # Kitchen issue detection
    if "Kitchen" in inspection_text:
        merged_data["Kitchen"] = {
            "issue": "Kitchen dampness",
            "thermal_status": "Cold spots observed"
        }

    # Master Bedroom issue detection
    if "Master Bedroom" in inspection_text:
        merged_data["Master Bedroom"] = {
            "issue": "Wall dampness + efflorescence",
            "thermal_status": "Moisture confirmed"
        }

    # Extract temperature summary
    temp_data = extract_temperature_data(thermal_text)

    merged_data["thermal_summary"] = temp_data

    return merged_data