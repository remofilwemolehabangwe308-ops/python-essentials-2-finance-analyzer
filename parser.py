import random
from models import Transaction

description_category = [
        ("Groceries", "Food"),
        ("Uber driver", "Transport"),
        ("Monthly salary", "Income"),
        ("Airtime", "Communication"),
        ("Electricity", "Bills"),
        ("Netflix", "Entertainment"),
        ("Resturants", "Food"),
        ("Products", "SkinCare"),
        ("Pharmacy", "Health"),
        ("School supplies", "Education"),
        ("Rent payment", "Housing"),
        ("Freelance", "Income")
    ]

def generate_sample_file():
    dates = [
        "2026-08-01",
        "2026-08-02",
        "2026-08-03",
        "2026-08-04",
        "2026-08-05",
        "2026-08-06",
        "2026-08-07",
        "2026-08-08",
        "2026-08-09",
        "2026-08-10",
        "2026-08-11",
        "2026-08-12"
    ]

    with open ("data/statement.txt", "w") as file:
            for i in range(12):
                amount = random.randint(50, 5000)
                descriptions_categories = random.choice(description_category)
                description = descriptions_categories[0]
                category = descriptions_categories[1]
                transaction_dates = random.choice(dates)
                if "Income" in category:
                     amount = amount
                else:
                     amount = -amount

                transaction_reports = f"{transaction_dates},{description},{amount},{category}"
                file.write(f"{transaction_reports}\n")

            clean_record = f"2026-08-07,Uber driver,-100,Transport"
            file.write(f"{clean_record}\n")

            messy_transaction = f'2026/08/01,Netflix,-500,Entertainment' 
            file.write(f"{messy_transaction}\n")

            missing_record = f" 2026-08-10,Pharmacy,-250"
            file.write(f"{missing_record}\n") 

            transaction = "THIS IS NOT A TRANSACTION"
            file.write(f"{transaction}\n")

            non_numeric_amount = f"2026-08-04,Electricity,xyz,Bills"
            file.write(f"{non_numeric_amount}\n")

            duplicate_transaction = f"2026-08-07,Uber driver,-100,Transport"
            file.write(f"{duplicate_transaction}\n")

            whitespace_transaction = f" 2026-08-06,Airtime,-150,Communication  "
            file.write(f"{whitespace_transaction}\n")

            mismatched_transaction1 = f"2026-08-11,School supplies,-500,Health"
            file.write(f"{mismatched_transaction1}\n")

            mismatched_transaction2 = f"2026-08-11,School supplies,500,Education"
            file.write(f"{mismatched_transaction2}\n")


def load_transactions(path):
     valid_transactions = []
     rejections = []
     has_data = False
     try:
           with open(path,"r") as file:
                    for index, transaction in enumerate(file, start = 1):
                        has_data = True 
                        cleaned_transaction = []
                        transaction_split = transaction.split(",")
                        if len(transaction_split) == 4:
                                        for item in transaction_split:
                                                                          whitespace_transaction = item.strip()
                                                                          cleaned_transaction.append(whitespace_transaction)
                                        try:
                                                                            tidy_amount = float(cleaned_transaction[2])
                                                                            cleaned_transaction[2] = tidy_amount
                                        except ValueError:
                                                                            rejections.append(f"row {index}: this is not a float")
                                                                            continue
          
                                        tidy_date = cleaned_transaction[0].replace("/", "-")
                                        cleaned_transaction[0] = tidy_date
                                        match_found = False
                                        for description_pair in description_category:
                                                if description_pair[0] == cleaned_transaction[1]:
                                                        match_found = True
                                                        if description_pair[1] == cleaned_transaction[3]:
                                                                if cleaned_transaction[2] > 0 and cleaned_transaction[3] != "Income":
                                                                         rejections.append(f"row {index}: sign mismatched")
                                                                else:
                                                                         transaction1 =Transaction(cleaned_transaction[0],cleaned_transaction[1],cleaned_transaction[2],cleaned_transaction[3])
                                                                         valid_transactions.append(transaction1)
                                                                        
                                                        else:
                                                                rejections.append(f"row {index}: category mismatched")
                                                                continue
                                        if match_found == False:
                                                rejections.append(f"row {index}: description mismatched")
                  
          
                        else:
                                            rejections.append(f"row {index}: not enough fields" )
                    if has_data == False:
                            rejections.append("The file is empty")
     except FileNotFoundError:
                    rejections.append("No file was found")
     return valid_transactions, rejections                             

             
    
                                  
              
                      
                                          
                                        
                        
                                                                                                                                                                                                                                                                                                                                                                                     


             

              
                      
                
              

            
          
                

    
    

        
        

    