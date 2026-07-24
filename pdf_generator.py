from weasyprint import HTML
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HTML_FILE = os.path.join(BASE_DIR, "report.html")
PDF_FILE = os.path.join(BASE_DIR, "report.pdf")


def generate_pdf():

    if not os.path.exists(HTML_FILE):
        print(f"{HTML_FILE} not found.")
        return

    try:
        HTML(HTML_FILE).write_pdf(PDF_FILE)
        print(f"PDF saved at {PDF_FILE}")

    except Exception as e:
        print(e)