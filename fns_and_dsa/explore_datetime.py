from  datetime import datetime, timedelta

def display_current_datetime():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")


    def calculate_future_date():
        number_of_days = int(input("Enter the number of days to add to the current date:"))
        future_date = datetime.now() + timedelta(days=number_of_days)
        formatted_futuredate = future_date.strftime("%Y-%m-%d ")
        print(f"future date: {formatted_futuredate}")
    calculate_future_date()
display_current_datetime()
