import csv

def total_spent(rows):
  total = 0
  for row in rows:
    if row["Type"] != "Payment":
      total = total + float(row["Amount"])
  return -total
  
with open("transactions.csv") as f:
  reader = csv.DictReader(f)
  print(f"Total spent: ${total_spent(reader):,.2f}")