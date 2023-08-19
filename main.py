class Bill:

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:

    def __init__(self, name, days_in):
        self.name = name
        self.days_in = days_in

    def pays(self, bill):
        daily_cost = bill.amount / bill.period
        return self.days_in * daily_cost

class GeneratePDF:

    def __init__(self, filename):
        self.filename = filename
