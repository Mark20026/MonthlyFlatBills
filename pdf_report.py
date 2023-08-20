import webbrowser
import os

from fpdf import FPDF


class GeneratePaymentPDF:
    """
    A class to generate a PDF report for flatmate bills.

    Attributes:
        filename (str): The name of the PDF file to be generated.
    """

    def __init__(self, filename):
        """
        Initializes a GeneratePaymentPDF object.

        Args:
            filename (str): The name of the PDF file to be generated.
        """
        self.filename = filename

    def generate(self, flatmates, bill):
        """
        Generate a PDF report with flatmate payment information.

        Args:
            flatmates (list): List of all flatmates.
            bill (flat.Bill): The bill for the period.
        """
        pdf = FPDF()
        pdf.add_page()

        # Set up PDF content
        pdf.set_font("Arial", "B", 25)
        pdf.image("files/house.png", x=10, y=10, w=30)
        pdf.cell(200, 10, "Flatmates Bill Report", ln=True, align='C')
        pdf.ln(5)
        pdf.set_font("Arial", "B", 15)
        pdf.cell(200, 10, f"Period: {bill.month}, {bill.year}", ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Arial", size=12)
        for flatmate in flatmates:
            pdf.cell(100, 10, f"Flatmate: {flatmate.name}", ln=True)
            pdf.cell(100, 10, f"Amount to pay: {flatmate.pays(flatmates, bill):.2f}$", ln=True)
            pdf.ln(5)

        # Save the PDF to the specified filename
        os.chdir("bills")

        pdf.output(self.filename)

        webbrowser.open(self.filename)
