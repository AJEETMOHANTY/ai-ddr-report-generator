# AI-Powered DDR Report Generator

This project automates the creation of a **Detailed Diagnostic Report (DDR)** by analyzing:

- Inspection Report PDF
- Thermal Report PDF

The system extracts:

- Text observations
- Relevant images
- Thermal insights

Then merges both reports and generates a final structured DDR PDF using **Google Gemini AI**.
---

## Features

✅ Upload Inspection Report PDF  
✅ Upload Thermal Report PDF  
✅ Extract textual observations from both reports  
✅ Extract relevant images from PDFs  
✅ Merge inspection + thermal findings  
✅ Generate AI-powered DDR report  
✅ Create downloadable final PDF  
✅ Area-wise image placement in final report  
---

## Tech Stack

- Python
- Streamlit
- PyMuPDF (fitz)
- ReportLab
- Google Gemini API
- Python-dotenv
- Pillow
- NumPy
---

## Project Structure

```bash
project/
│
├── app.py                 # Streamlit UI
├── extract_text.py        # Extract text from PDFs
├── extract_images.py      # Extract relevant images
├── merge_reports.py       # Merge inspection + thermal findings
├── generate_ddr.py        # Generate DDR using Gemini
├── report_generator.py    # Generate final PDF
├── requirements.txt
├── .env
```
---

## Setup Instructions

### 1. Clone repository

```bash
git clone <your-repo-link>
cd project
```
---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```
---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```
---

## Environment Variables

Create a `.env` file:

```bash
GEMINI_API_KEY=your_api_key_here
```

Get API key from Google AI Studio.
---

## Run Project

```bash
streamlit run app.py
```
---

## Workflow

1. Upload inspection report PDF  
2. Upload thermal report PDF  
3. Extract text  
4. Extract images  
5. Merge findings  
6. Generate final DDR report  
7. Download final PDF  
---

## Output Includes

### Property Issue Summary
Overall issue summary

### Area-wise Observations
- Hall
- Bedroom
- Kitchen
- Parking
- etc.

### Root Cause Analysis

### Severity Assessment

### Recommendations

### Missing Information

### Area-wise Images
---

## Challenges Faced

### Image Filtering
PDFs contained logos and decorative images. Filtering logic was added to remove irrelevant images.

### Image Mapping
Some PDF pages contained multiple room observations, making exact image-to-room mapping challenging.
---

## Future Improvements

- Chunking
- OCR-based image mapping
- Better section-level image matching
- Improved thermal anomaly detection
- Multi-property support
- Better PDF formatting
---

## Demo

Loom video link:
https://drive.google.com/file/d/1clcW3eg3HcoJxtONg4brYDH0to3E1Hlf/view?usp=drive_link
---

## Author

Ajeet Mohanty
