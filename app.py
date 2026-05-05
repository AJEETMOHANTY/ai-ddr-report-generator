import streamlit as st
import os

from extract_text import extract_text
from extract_images import extract_images
from merge_reports import merge_reports
from generate_ddr import generate_ddr
from report_generator import generate_pdf


# App title
st.title("AI DDR Report Generator")

# Upload inspection PDF
inspection_file = st.file_uploader(
    "Upload Inspection Report",
    type=["pdf"]
)

# Upload thermal PDF
thermal_file = st.file_uploader(
    "Upload Thermal Report",
    type=["pdf"]
)


if st.button("Generate Report"):

    if inspection_file and thermal_file:

        os.makedirs("temp", exist_ok=True)

        # Save uploaded files locally
        inspection_path = f"temp/{inspection_file.name}"
        thermal_path = f"temp/{thermal_file.name}"

        with open(inspection_path, "wb") as f:
            f.write(inspection_file.read())

        with open(thermal_path, "wb") as f:
            f.write(thermal_file.read())

        st.write("Extracting inspection report text...")
        inspection_text = extract_text(inspection_path)

        st.write("Extracting thermal report text...")
        thermal_text = extract_text(thermal_path)

        st.write("Extracting images...")
        extract_images(
            inspection_path,
            "output/inspection_images"
        )

        extract_images(
            thermal_path,
            "output/thermal_images"
        )

        st.write("Merging findings...")
        merged_data = merge_reports(
            inspection_text,
            thermal_text
        )

        st.write("Generating DDR...")
        final_report = generate_ddr(
            merged_data
        )

        st.write(final_report)

        st.write("Generating PDF...")
        pdf_path = generate_pdf(
            final_report
        )

        # Download button
        with open(pdf_path, "rb") as f:
            st.download_button(
                "Download Final Report",
                f,
                file_name="DDR_Report.pdf"
            )