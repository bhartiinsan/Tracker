# Python program to print a dictionary in table format

# Sample dictionaries
sample_dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400}

person_dict = {
    'Name': 'John',
    'Age': 25,
    'City': 'New York',
    'Job': 'Engineer',
    'Salary': 50000
}

list_of_dicts = [
    {'id': 1, 'name': 'Alice', 'age': 25, 'city': 'NYC'},
    {'id': 2, 'name': 'Bob', 'age': 30, 'city': 'LA'},
    {'id': 3, 'name': 'Charlie', 'age': 35, 'city': 'Chicago'},
    {'id': 4, 'name': 'Diana', 'age': 28, 'city': 'Boston'}
]

print("="*60)
print("METHOD 1 - Simple String Formatting")
print("="*60)
print()

print("Dictionary:", sample_dict)
print()
print("Key".ljust(10) + "Value")
print("-" * 15)
for key, value in sample_dict.items():
    print(str(key).ljust(10) + str(value))
print()

print("="*60)
print("METHOD 2 - Using Format String with Borders")
print("="*60)
print()

print("+-------+-------+")
print("| Key   | Value |")
print("+-------+-------+")
for key, value in sample_dict.items():
    print(f"| {str(key):5} | {str(value):5} |")
print("+-------+-------+")
print()

print("="*60)
print("METHOD 3 - Using tabs")
print("="*60)
print()

print("Key\tValue")
print("-" * 20)
for key, value in sample_dict.items():
    print(f"{key}\t{value}")
print()

print("="*60)
print("METHOD 4 - Better Formatting with Column Width")
print("="*60)
print()

print("Key".ljust(15) + "Value".ljust(15))
print("-" * 30)
for key, value in sample_dict.items():
    print(str(key).ljust(15) + str(value).ljust(15))
print()

print("="*60)
print("METHOD 5 - Dictionary with Multiple Columns")
print("="*60)
print()

print("Attribute".ljust(20) + "Value".ljust(20))
print("-" * 40)
for key, value in person_dict.items():
    print(str(key).ljust(20) + str(value).ljust(20))
print()

print("="*60)
print("METHOD 6 - List of Dictionaries in Table Format")
print("="*60)
print()

# Print headers
headers = list(list_of_dicts[0].keys())
col_width = 15

header_row = ""
for header in headers:
    header_row += header.ljust(col_width) + "|"
print(header_row)
print("-" * (col_width * len(headers) + len(headers)))

# Print rows
for item in list_of_dicts:
    row = ""
    for header in headers:
        row += str(item[header]).ljust(col_width) + "|"
    print(row)
print()

print("="*60)
print("METHOD 7 - Using tabulate library (if available)")
print("="*60)
print()

try:
    from tabulate import tabulate

    # For single dictionary
    table_data = [[key, value] for key, value in sample_dict.items()]
    print("Single Dictionary:")
    print(tabulate(table_data, headers=['Key', 'Value'], tablefmt='grid'))
    print()

    # For list of dictionaries
    print("List of Dictionaries:")
    print(tabulate(list_of_dicts, headers='keys', tablefmt='grid'))
    print()
except ImportError:
    print("tabulate library not installed. Install with: pip install tabulate")
    print()

print("="*60)
print("METHOD 8 - Using pandas (if available)")
print("="*60)
print()

try:
    import pandas as pd

    # For single dictionary
    df = pd.DataFrame(list(sample_dict.items()), columns=['Key', 'Value'])
    print("Single Dictionary:")
    print(df)
    print()

    # For list of dictionaries
    df = pd.DataFrame(list_of_dicts)
    print("List of Dictionaries:")
    print(df)
    print()
except ImportError:
    print("pandas library not installed. Install with: pip install pandas")
    print()

print("="*60)
print("METHOD 9 - ASCII Art Table (Manual)")
print("="*60)
print()

data = sample_dict
col_width = 12

# Top border
print("+" + "-" * (col_width + 2) + "+" + "-" * (col_width + 2) + "+")
# Header
print("| " + "Key".center(col_width) + " | " + "Value".center(col_width) + " |")
# Middle border
print("+" + "-" * (col_width + 2) + "+" + "-" * (col_width + 2) + "+")
# Data rows
for key, value in data.items():
    print("| " + str(key).center(col_width) + " | " + str(value).center(col_width) + " |")
# Bottom border
print("+" + "-" * (col_width + 2) + "+" + "-" * (col_width + 2) + "+")
print()

print("="*60)
print("METHOD 10 - Custom Table Function")
print("="*60)
print()

def print_dict_table(data, title="Table"):
    """Print dictionary as a formatted table"""
    print(f"\n{title}")
    print("-" * 40)

    if isinstance(data, dict):
        # Single dictionary
        max_key_len = max(len(str(k)) for k in data.keys()) if data else 10
        max_val_len = max(len(str(v)) for v in data.values()) if data else 10

        print(f"{'Key'.ljust(max_key_len + 2)} | {'Value'.ljust(max_val_len + 2)}")
        print("-" * (max_key_len + max_val_len + 7))

        for key, value in data.items():
            print(f"{str(key).ljust(max_key_len + 2)} | {str(value).ljust(max_val_len + 2)}")

    elif isinstance(data, list):
        # List of dictionaries
        if not data:
            return

        headers = list(data[0].keys())
        col_width = 15

        # Print headers
        header_row = " | ".join(h.ljust(col_width) for h in headers)
        print(header_row)
        print("-" * len(header_row))

        # Print rows
        for item in data:
            row = " | ".join(str(item.get(h, '')).ljust(col_width) for h in headers)
            print(row)

print("Single Dictionary:")
print_dict_table(person_dict, "Person Information")

print("\n\nList of Dictionaries:")
print_dict_table(list_of_dicts, "Employee Data")
