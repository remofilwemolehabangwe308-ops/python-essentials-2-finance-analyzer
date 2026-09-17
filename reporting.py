import os 
import datetime
import platform
from analytics import find_duplicates
from analytics import find_outliers
from analytics import category_totals


def monthly_summary(valid_transactions, rejections):
    with open("data/report.txt", "w") as file:
        file.write("===== Personal Finance Transaction Report =====\n")
        total_of_categories = category_totals(valid_transactions) 
        duplicates = find_duplicates(valid_transactions)
        outliers = find_outliers(valid_transactions)
        total_amount = 0
        for transaction in valid_transactions:
            total_amount += transaction.amount
        rejected_rows = len(rejections)

        os_name = platform.system()
        python_version = platform.python_version()
        current_working_directory = os.getcwd()
        file_exist = os.path.exists("data/statement.txt")
        if file_exist is True:
            file_size = os.path.getsize("data/statement.txt")
        else:
            file_size = 0

        today = datetime.datetime.now()
        formatted_date = today.strftime("%A, %d %B %Y")

        file.write(f"Total Amount: {total_amount}\n")

        file.write("=== Duplicates ===")
        for transaction in duplicates:
          file.write(f"{transaction}\n")

        file.write("=== Outliers ===")
        for transaction in outliers:
            file.write(f"{transaction}\n")

        file.write(f"Rejected rows: {rejected_rows}\n")

        for category, amount in total_of_categories.items():
            file.write(f"Category: {category}\n")
            file.write(f"Amount: {amount}\n")

        file.write(f"Date: {formatted_date}\n")
        file.write(f"OS name: {os_name}\n")
        file.write(f"Python Version: {python_version}\n")
        file.write(f"Current working directory: {current_working_directory}\n")
        file.write(f"File size: {file_size}\n")

    with open("data/activity.log", "a") as file:
        file.write(f"Timestamp: {formatted_date} - Report generated successfully\n")
