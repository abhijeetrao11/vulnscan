from weasyprint import HTML
import os

def generate_pdf():

    if not os.path.exists("report.html"):
        print("[-] HTML report not found.")
        return 
    

    try:
        HTML("report.html").write_pdf("report.pdf")
        print("[+] PDF report generated successfully.")
    except Exception as e:
        print(f"[-] Error generating PDF: {e}")