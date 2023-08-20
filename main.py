import webbrowser

from fpdf import FPDF


MONTHS = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31,
          "September": 30, "October": 31, "November": 30, "December": 31}


class Bill:
    """
    A class to represent a bill for a specific period.

    Attributes:
        amount (float): The amount of the bill.
        year (str): The year of the period.
        month (str): The month of the period.
    """

    def __init__(self, amount, year, month):
        """
        Initializes a Bill object.

        Args:
            amount (float): The amount of the bill.
            year (str): The year of the period.
            month (str): The month of the period.
        """
        self.amount = amount
        self.month = month
        self.year = year

    def days_in_period(self, month):
        """
        Calculate the number of days in a specific month of the period.

        Args:
            month (str): The month for which to calculate the days.

        Returns:
            int: The number of days in the specified month.
        """
        if month == "February":
            if int(self.year) % 4 == 0:
                return 29
        else:
            return MONTHS[month]


class Flatmate:
    """
    A class to represent a flatmate and their payment calculations.

    Attributes:
        name (str): The name of the flatmate.
        days_in_flat (int): The number of days the flatmate stayed in the flat.
    """

    def __init__(self, name, days_in_flat):
        """
        Initializes a Flatmate object.

        Args:
            name (str): The name of the flatmate.
            days_in_flat (int): The number of days the flatmate stayed in the flat.
        """
        self.name = name
        self.days_in_flat = days_in_flat

    def pays(self, flatmates, bill):
        """
        Calculate the amount a flatmate needs to pay based on their stay and the bill.

        Args:
            flatmates (list): List of all flatmates.
            bill (Bill): The bill for the period.

        Returns:
            float: The amount the flatmate needs to pay.
        """
        total_days = sum(flatmate.days_in_flat for flatmate in flatmates)
        one_day_payment = (bill.amount / total_days) * self.days_in_flat

        return one_day_payment


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
            bill (Bill): The bill for the period.
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
        pdf.output(self.filename)

        webbrowser.open(self.filename)


bill_amount = float(input("How much is the bill?: "))
bill_period = input("What month and year is it? (August 2023): ").split()

period_month = bill_period[0]
period_year = bill_period[1]

flatmate_count = int(input("How many people live there?: "))

flatmates = []
for i in range(flatmate_count):
    flatmate_name = input(f"What is the name of the {i+1}. flatmate: ")
    flatmate_days_in = int(input(f"How many days was the {i+1}. flatmate been in: "))
    flatmates.append(Flatmate(flatmate_name, flatmate_days_in))

bill = Bill(bill_amount, period_year, period_month)

bill.days_in_period(period_month)

pdf_of_payment = GeneratePaymentPDF("bill_report.pdf")
print("The bill of the payments is printing")
print(".")
print("..")
print("...")
pdf_of_payment.generate(flatmates, bill)
print("PDF was generated")