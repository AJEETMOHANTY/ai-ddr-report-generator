import fitz  # PyMuPDF library for reading PDFs


def extract_text(pdf_path):
    """
    Extracts all text from the given PDF.

    Parameters:
        pdf_path (str): path of uploaded PDF file

    Returns:
        str: complete extracted text
    """

    # Open PDF file
    doc = fitz.open(pdf_path)

    extracted_text = ""

    # Loop through all pages
    for page_num in range(len(doc)):

        # Get current page
        page = doc[page_num]

        # Extract text from current page
        text = page.get_text()

        # Add page separator
        extracted_text += f"\n--- Page {page_num+1} ---\n"

        # Append extracted text
        extracted_text += text

    # Close file after reading
    doc.close()

    return extracted_text