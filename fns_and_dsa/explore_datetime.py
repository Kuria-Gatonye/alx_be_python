from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")


    print(formatted_date)

display_current_datetime()

from datetime import datetime, timedelta

def calculate_future_date(days):
    today = datetime.now()
    future_date = today + timedelta(days=days)
    print("Future Date:", future_date.strftime("%Y-%m-%d"))

# Ask user for input
days_input = int(input("Enter number of days: "))

# Call the function with the user input
calculate_future_date(days_input)
