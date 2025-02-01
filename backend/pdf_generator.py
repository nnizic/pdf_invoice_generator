from fpdf import FPDF
from database import dynamodb

def generate_pdf():
    table = dynamodb.Table("Invoices")
    response = table.scan()
    invoices = response.get("Items", [])

    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
    pdf.set_font("DejaVu", size=12)
    
    pdf.cell(200, 10, txt="Popis računa", ln=True, align='C')
    for invoice in invoices:
        pdf.cell(200, 10, txt=f"Kupac: {invoice['customer_name']}", ln=True)
        pdf.cell(200, 10, txt=f"Datum: {invoice['date']}", ln=True)
        pdf.cell(200, 10, txt=f"Ukupno: {invoice['total']} kn", ln=True)
        pdf.cell(200, 10, txt="", ln=True)

    filename = "racuni.pdf"
    pdf.output(filename)
    return filename

