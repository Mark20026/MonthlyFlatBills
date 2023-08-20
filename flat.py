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
        MONTHS = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31,
                  "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}

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
