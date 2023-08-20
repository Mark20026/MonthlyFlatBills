import re

from flat import Bill, Flatmate
from pdf_report import GeneratePaymentPDF

bill_amount = float(input("How much is the bill?: "))

while True:
    bill_period = input("What month and year is it? (August 2023): ")

    # Regular expression pattern for "Month Year" format (e.g., August 2023)
    pattern = r"^(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}$"

    if re.match(pattern, bill_period):
        # Extract month and year
        month, year = bill_period.split()
        print("Month:", month)
        print("Year:", year)
        break
    else:
        print("Invalid input. Please provide the month and year in the format 'Month Year' (e.g., August 2023).")

flatmate_count = int(input("How many people live there?: "))

flatmates = []
for i in range(flatmate_count):
    flatmate_name = input(f"What is the name of the {i+1}. flatmate: ")
    flatmate_days_in = int(input(f"How many days was the {i+1}. flatmate been in: "))
    flatmates.append(Flatmate(flatmate_name, flatmate_days_in))

bill = Bill(bill_amount, year, month)

bill.days_in_period(month)

pdf_of_payment = GeneratePaymentPDF(filename=f"{bill.month + ' ' + bill.year}.pdf")
print("The bill of the payments is printing")
print(".")
print("..")
print("...")
pdf_of_payment.generate(flatmates, bill)
print("PDF was generated")