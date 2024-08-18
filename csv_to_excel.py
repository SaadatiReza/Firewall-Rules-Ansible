import pandas as pd
import sys

# Read the CSV file
csv_file = sys.argv[1]
excel_file = csv_file.replace('.csv', '.xlsx')

# Convert CSV to Excel
df = pd.read_csv(csv_file)
df.to_excel(excel_file, index=False)

print(f"Converted {csv_file} to {excel_file}")
