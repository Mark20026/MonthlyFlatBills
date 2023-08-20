from fpdf import FPDF


MONTHS = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31, "August": 31,
          "September": 30, "October": 31, "November": 30, "December": 31}


class Bill:

    def __init__(self, amount, year, month):
        self.amount = amount
        self.month = month
        self.year = year

    def days_in_period(self, month):
        if month == "February":
            if int(self.year) % 4 == 0:
                return 29
        else:
            return MONTHS[month]


class Flatmate:

    def __init__(self, name, days_in_flat):
        self.name = name
        self.days_in_flat = days_in_flat

    def pays(self, flatmates, bill):
        total_days = sum(flatmate.days_in_flat for flatmate in flatmates)
        one_day_payment = (bill.amount / total_days) * self.days_in_flat

        return one_day_payment


class GeneratePaymentPDF:

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmates, bill):
        pdf = FPDF()
        pdf.add_page()
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
            pdf.cell(100, 10, f"Amount to pay: {flatmate.pays(flatmates, bill):.2f}", ln=True)
            pdf.ln(5)

        pdf.output(self.filename)


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