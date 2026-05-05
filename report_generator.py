from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet
import os


def generate_pdf(report_text):
    """
    Convert final DDR text into PDF
    """

    os.makedirs("output", exist_ok=True)

    output_path = "output/final_ddr_report.pdf"

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(output_path)

    story = []

    # Add each line into PDF
    for line in report_text.split("\n"):

        if line.strip():
            story.append(
                Paragraph(
                    line,
                    styles["Normal"]
                )
            )

            story.append(Spacer(1, 12))

    doc.build(story)

    return output_path