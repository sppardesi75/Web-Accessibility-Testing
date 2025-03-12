import json
import csv

# Load JSON data
with open("accessibility_report.json", "r") as json_file:
    data = json.load(json_file)

# Extract violations
violations = data.get("violations", [])

# Create a CSV file
with open("accessibility_report.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Issue ID", "Severity", "Description", "Help URL"])

    for issue in violations:
        csv_writer.writerow([issue["id"], issue["impact"], issue["description"], issue["helpUrl"]])

print("CSV Report generated: accessibility_report.csv")
