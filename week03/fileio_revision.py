"""
File I/O for Data Science
========================
Essential file operations for handling data in various formats
"""

import json
import csv
import os
from datetime import datetime
import pickle

# Sample data for demonstrations
sample_expenses = [
    {'id': 1, 'amount': 25.50, 'category': 'food', 'description': 'Lunch', 'date': '2024-01-15'},
    {'id': 2, 'amount': 15.75, 'category': 'transport', 'description': 'Bus fare', 'date': '2024-01-15'},
    {'id': 3, 'amount': 100.00, 'category': 'utilities', 'description': 'Electric bill', 'date': '2024-01-16'},
    {'id': 4, 'amount': 8.25, 'category': 'food', 'description': 'Coffee', 'date': '2024-01-16'},
]

print("=== FILE I/O FOR DATA SCIENCE ===")

# 1. JSON FILES - Most common for web APIs and configuration
print("\n1. JSON FILE OPERATIONS")


def save_to_json(data, filename):
    """Save data to JSON file with proper error handling"""
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        print(f"✅ Data saved to {filename}")
    except Exception as e:
        print(f"❌ Error saving to JSON: {e}")


def load_from_json(filename):
    """Load data from JSON file with error handling"""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"✅ Data loaded from {filename}")
        return data
    except FileNotFoundError:
        print(f"❌ File {filename} not found")
        return []
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON format: {e}")
        return []


# Save and load JSON
save_to_json(sample_expenses, 'sample_expenses.json')
loaded_expenses = load_from_json('sample_expenses.json')
print(f"Loaded {len(loaded_expenses)} expenses")

# 2. CSV FILES - Standard for tabular data
print("\n2. CSV FILE OPERATIONS")


def save_to_csv(data, filename):
    """Save list of dictionaries to CSV"""
    if not data:
        print("No data to save")
        return

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"✅ Data saved to {filename}")
    except Exception as e:
        print(f"❌ Error saving to CSV: {e}")


def load_from_csv(filename):
    """Load data from CSV file"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            # Convert numeric fields
            for row in data:
                row['id'] = int(row['id'])
                row['amount'] = float(row['amount'])
        print(f"✅ Data loaded from {filename}")
        return data
    except FileNotFoundError:
        print(f"❌ File {filename} not found")
        return []
    except Exception as e:
        print(f"❌ Error loading CSV: {e}")
        return []


# Save and load CSV
save_to_csv(sample_expenses, 'sample_expenses.csv')
loaded_csv_data = load_from_csv('sample_expenses.csv')
print(f"Loaded {len(loaded_csv_data)} expenses from CSV")

# 3. TEXT FILES - For logs, reports, and simple data
print("\n3. TEXT FILE OPERATIONS")


def generate_expense_report(expenses, filename):
    """Generate a formatted text report"""
    try:
        with open(filename, 'w') as file:
            file.write("EXPENSE REPORT\n")
            file.write("=" * 50 + "\n")
            file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            total = 0
            categories = {}

            for expense in expenses:
                amount = expense['amount']
                category = expense['category']

                file.write(f"${amount:>8.2f} | {category:<12} | {expense['description']}\n")
                total += amount
                categories[category] = categories.get(category, 0) + amount

            file.write("-" * 50 + "\n")
            file.write(f"TOTAL: ${total:.2f}\n\n")

            file.write("BY CATEGORY:\n")
            for cat, amt in sorted(categories.items()):
                percentage = (amt / total) * 100
                file.write(f"{cat:<12}: ${amt:>8.2f} ({percentage:>5.1f}%)\n")

        print(f"✅ Report generated: {filename}")
    except Exception as e:
        print(f"❌ Error generating report: {e}")


generate_expense_report(sample_expenses, 'expense_report.txt')

# Read and display the report
try:
    with open('expense_report.txt', 'r') as file:
        content = file.read()
        print("Report content:")
        print(content[:200] + "..." if len(content) > 200 else content)
except Exception as e:
    print(f"Error reading report: {e}")

# 4. BINARY FILES - For Python objects (pickle)
print("\n4. BINARY FILE OPERATIONS (PICKLE)")


def save_python_object(obj, filename):
    """Save any Python object using pickle"""
    try:
        with open(filename, 'wb') as file:
            pickle.dump(obj, file)
        print(f"✅ Object saved to {filename}")
    except Exception as e:
        print(f"❌ Error saving object: {e}")


def load_python_object(filename):
    """Load Python object from pickle file"""
    try:
        with open(filename, 'rb') as file:
            obj = pickle.load(file)
        print(f"✅ Object loaded from {filename}")
        return obj
    except FileNotFoundError:
        print(f"❌ File {filename} not found")
        return None
    except Exception as e:
        print(f"❌ Error loading object: {e}")
        return None


# Save complex Python object
complex_data = {
    'expenses': sample_expenses,
    'metadata': {
        'created': datetime.now(),
        'version': '1.0',
        'categories': set(['food', 'transport', 'utilities'])
    },
    'statistics': {
        'total': sum(exp['amount'] for exp in sample_expenses),
        'count': len(sample_expenses)
    }
}

save_python_object(complex_data, 'complex_data.pkl')
loaded_object = load_python_object('complex_data.pkl')
if loaded_object:
    print(f"Loaded object with {len(loaded_object['expenses'])} expenses")

# 5. FILE SYSTEM OPERATIONS
print("\n5. FILE SYSTEM OPERATIONS")


def analyze_directory(path='.'):
    """Analyze files in directory"""
    try:
        files = os.listdir(path)
        file_info = []

        for filename in files:
            filepath = os.path.join(path, filename)
            if os.path.isfile(filepath):
                size = os.path.getsize(filepath)
                modified = datetime.fromtimestamp(os.path.getmtime(filepath))
                file_info.append({
                    'name': filename,
                    'size': size,
                    'modified': modified,
                    'extension': os.path.splitext(filename)[1]
                })

        return file_info
    except Exception as e:
        print(f"Error analyzing directory: {e}")
        return []


# Analyze current directory
file_info = analyze_directory()
print(f"Found {len(file_info)} files:")
for info in file_info[:5]:  # Show first 5 files
    print(f"  {info['name']:<20} | {info['size']:>8} bytes | {info['extension']}")

# 6. CONTEXT MANAGERS AND BEST PRACTICES
print("\n6. ADVANCED FILE HANDLING")


class FileManager:
    """Context manager for safe file operations"""

    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except Exception as e:
            print(f"Error opening file: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"Error occurred: {exc_val}")
        return False


# Using custom context manager
try:
    with FileManager('sample_expenses.json', 'r') as file:
        data = json.load(file)
        print(f"Successfully read {len(data)} records using custom context manager")
except Exception as e:
    print(f"Failed to read file: {e}")

# 7. STREAMING LARGE FILES
print("\n7. HANDLING LARGE FILES")


def process_large_csv_streaming(filename, chunk_size=1000):
    """Process large CSV files in chunks"""
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            chunk = []
            total_processed = 0

            for row in reader:
                chunk.append(row)

                if len(chunk) >= chunk_size:
                    # Process chunk
                    total_processed += len(chunk)
                    print(f"Processed chunk of {len(chunk)} records (total: {total_processed})")
                    chunk = []

            # Process remaining records
            if chunk:
                total_processed += len(chunk)
                print(f"Processed final chunk of {len(chunk)} records")

            return total_processed
    except Exception as e:
        print(f"Error processing file: {e}")
        return 0


# Demonstrate with our small file
total = process_large_csv_streaming('sample_expenses.csv', chunk_size=2)
print(f"Total records processed: {total}")

# 8. DATA VALIDATION AND CLEANING
print("\n8. DATA VALIDATION")


def validate_expense_data(data):
    """Validate expense data structure"""
    required_fields = ['id', 'amount', 'category', 'date']
    valid_records = []
    errors = []

    for i, record in enumerate(data):
        record_errors = []

        # Check required fields
        for field in required_fields:
            if field not in record:
                record_errors.append(f"Missing field: {field}")

        # Validate data types and values
        if 'amount' in record:
            try:
                amount = float(record['amount'])
                if amount <= 0:
                    record_errors.append("Amount must be positive")
            except (ValueError, TypeError):
                record_errors.append("Invalid amount format")

        if 'id' in record:
            try:
                int(record['id'])
            except (ValueError, TypeError):
                record_errors.append("Invalid ID format")

        if record_errors:
            errors.append(f"Record {i}: {', '.join(record_errors)}")
        else:
            valid_records.append(record)

    return valid_records, errors


# Validate our data
valid_data, validation_errors = validate_expense_data(loaded_expenses)
print(f"Validation results: {len(valid_data)} valid, {len(validation_errors)} errors")
for error in validation_errors:
    print(f"  ❌ {error}")

print("\n=== FILE I/O SUMMARY ===")
print("Key concepts covered:")
print("• JSON for structured data and APIs")
print("• CSV for tabular data and spreadsheets")
print("• Text files for reports and logs")
print("• Pickle for Python objects")
print("• File system operations")
print("• Context managers for safe file handling")
print("• Streaming for large files")
print("• Data validation and error handling")
