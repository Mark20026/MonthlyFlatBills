from flat import Bill, Flatmate
from pdf_report import GeneratePaymentPDF

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

pdf_of_payment = GeneratePaymentPDF(filename=f"{bill.month + ' ' + bill.year}.pdf")
print("The bill of the payments is printing")
print(".")
print("..")
print("...")
pdf_of_payment.generate(flatmates, bill)
print("PDF was generated")