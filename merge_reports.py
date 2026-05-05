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

    hotspots = [float(x) for x in hotspots]
    coldspots = [float(x) for x in coldspots]

    return {
        "min_coldspot": min(coldspots) if coldspots else "Not Available",
        "max_coldspot": max(coldspots) if coldspots else "Not Available",
        "max_hotspot": max(hotspots) if hotspots else "Not Available"
    }


def merge_reports(inspection_text, thermal_text):
    """
    Merge inspection report + thermal report

    This function:
    - identifies impacted areas
    - maps issue type
    - stores page number for image retrieval
    """

    merged_data = {}

    # Area → issue mapping
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

    # Page mapping for image extraction
    # Used only for report_generator.py
    page_mapping = {
        "Hall": 3,
        "Bedroom": 4,
        "Master Bedroom": 5,
        "Kitchen": 6,
        "Common Bathroom": 6,
        "Master Bathroom": 5,
        "Parking": 7,
        "External wall": 7
    }

    for area, issue in issue_mapping.items():

        if area.lower() in inspection_text.lower():

            merged_data[area] = {
                "issue": issue,
                "thermal_status": "Thermal verification available",
                "page": page_mapping.get(area)
            }

    # Add thermal summary
    temp_data = extract_temperature_data(thermal_text)

    merged_data["thermal_summary"] = {
        "issue": (
            f"Thermal analysis detected cold spots "
            f"between {temp_data['min_coldspot']}°C "
            f"and {temp_data['max_coldspot']}°C, "
            f"indicating possible hidden moisture."
        )
    }

    return merged_data