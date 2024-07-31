import csv
import pandas as pd

def read_transactions():
    with open('transactions.csv', mode='r', newline='') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)

        # Skip the header row
        next(csv_reader)
        
        # Create a list to store the transactions
        transactions = []

        # Iterate over each row in the CSV file
        for row in csv_reader:

            # Clean all rows
            row = [cell.strip() for cell in row]

            transactions.append({
                "date": row[0],
                "type": row[1],
                "productType": row[2],
                "productName": row[3],
                "productId": row[4],
                "units": int(row[5]) if row[5] else None,
                "total": float(row[6]) if row[5] else None,
            })

    return transactions

# Read transactions
transactions = read_transactions()

# Convert transactions to a DataFrame
df = pd.DataFrame(transactions)

# Display the DataFrame
print(df)

