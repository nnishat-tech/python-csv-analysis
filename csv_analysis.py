# csv_analysis.py
import csv

# Sample CSV file name
filename = "data.csv"

# Create sample data if the file doesn't exist
try:
    with open(filename, 'x', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Score"])
        writer.writerow(["Alice", 85])
        writer.writerow(["Bob", 92])
        writer.writerow(["Charlie", 78])
except FileExistsError:
    pass  # File already exists

# Read and analyze CSV
with open(filename, newline='') as f:
    reader = csv.DictReader(f)
    scores = []
    for row in reader:
        scores.append(int(row["Score"]))

# Analysis
total = sum(scores)
count = len(scores)
average = total / count if count else 0
highest = max(scores) if scores else 0
lowest = min(scores) if scores else 0

print(f"Total students: {count}")
print(f"Average score: {average}")
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")
