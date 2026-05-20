import json

try:
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    print("Error: tasks.json not found. Please create the file first.")
    tasks = []

incomplete = [t for t in tasks if t["done"] == False]

print(f"You have {len(incomplete)} incomplete tasks:")

for t in incomplete:
    print("-", t["task"])