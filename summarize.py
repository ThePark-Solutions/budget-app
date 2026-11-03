import csv

total = 0
with open("transactions.csv") as f:
  reader = csv.DictReader(f)
  for row in reader:
    if row["Type"] != "Payment":
      total = total + float(row["Amount"])
  
print(f"Total spent: ${-total:,.2f}")