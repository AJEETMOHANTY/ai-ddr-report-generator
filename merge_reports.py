import re


def extract_temperature_data(thermal_text):
    """
    Extract hotspot and coldspot values
    from thermal report
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
    Dynamically detect issues
    from inspection report
    """

    merged_data = {}

    issue_mapping = {
        "Hall": "Skirting dampness",
        "Bedroom": "Bedroom dampness",
        "Master Bedroom": "Wall dampness + efflorescence",
        "Kitchen": "Kitchen dampness",
        "Common Bathroom": "Tile gaps + plumbing issues",
        "Master Bathroom": "Tile hollowness",
        "Parking": "Parking leakage",
        "External wall": "Cracks detected"
    }

    for area, issue in issue_mapping.items():

        if area.lower() in inspection_text.lower():

            merged_data[area] = {
                "issue": issue,
                "thermal_status": "Thermal verification available"
            }

    temp_data = extract_temperature_data(thermal_text)

    merged_data["thermal_summary"] = temp_data

    return merged_data