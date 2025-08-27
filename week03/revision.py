"""
Python Data Structures for Data Science
=======================================
Essential data structures you'll use constantly in data science and ML
"""

# 1. LISTS - Dynamic arrays, most versatile
print("=== LISTS ===")
expenses = [25.50, 15.75, 100.00, 8.25]
categories = ['food', 'transport', 'utilities', 'food']

# List comprehensions - very important for data processing
squared_expenses = [x ** 2 for x in expenses]
food_expenses = [expenses[i] for i, cat in enumerate(categories) if cat == 'food']

print(f"Original expenses: {expenses}")
print(f"Squared expenses: {squared_expenses}")
print(f"Food expenses only: {food_expenses}")

# Advanced list operations
expenses.extend([45.20, 12.30])  # Add multiple items
total_expenses = sum(expenses)
avg_expense = total_expenses / len(expenses)
print(f"Total: ${total_expenses:.2f}, Average: ${avg_expense:.2f}")

# 2. DICTIONARIES - Key-value pairs, like JSON
print("\n=== DICTIONARIES ===")
expense_record = {
    'id': 1,
    'amount': 25.50,
    'category': 'food',
    'description': 'Lunch at restaurant',
    'date': '2024-01-15'
}

# Dictionary comprehensions
category_totals = {}
for i, amount in enumerate(expenses):
    cat = categories[i] if i < len(categories) else 'other'
    category_totals[cat] = category_totals.get(cat, 0) + amount

print(f"Expense record: {expense_record}")
print(f"Category totals: {category_totals}")

# Accessing and modifying
expense_record['tags'] = ['restaurant', 'lunch']
amount = expense_record.get('amount', 0)  # Safe access
print(f"Amount: ${amount}")

# 3. TUPLES - Immutable sequences, good for coordinates, records
print("\n=== TUPLES ===")
expense_tuple = (25.50, 'food', '2024-01-15')  # amount, category, date
coordinates = (40.7128, -74.0060)  # latitude, longitude for location-based analysis

# Tuple unpacking - very useful in data science
amount, category, date = expense_tuple
lat, lon = coordinates
print(f"Unpacked: ${amount} spent on {category} on {date}")

# Named tuples - structured data
from collections import namedtuple

Expense = namedtuple('Expense', ['amount', 'category', 'date', 'description'])
expense1 = Expense(25.50, 'food', '2024-01-15', 'Lunch')
print(f"Named tuple: {expense1.amount} for {expense1.category}")

# 4. SETS - Unique collections, great for data cleaning
print("\n=== SETS ===")
all_categories = ['food', 'transport', 'food', 'utilities', 'food', 'transport']
unique_categories = set(all_categories)
print(f"All categories: {all_categories}")
print(f"Unique categories: {unique_categories}")

# Set operations for data analysis
set1 = {'food', 'transport', 'utilities'}
set2 = {'food', 'entertainment', 'healthcare'}
common = set1 & set2  # intersection
all_cats = set1 | set2  # union
different = set1 - set2  # difference

print(f"Common categories: {common}")
print(f"All categories: {all_cats}")
print(f"Only in set1: {different}")

# 5. COLLECTIONS MODULE - Advanced data structures
print("\n=== ADVANCED COLLECTIONS ===")
from collections import Counter, defaultdict, deque

# Counter - frequency counting (very useful in data analysis)
category_counter = Counter(all_categories)
print(f"Category frequencies: {category_counter}")
print(f"Most common: {category_counter.most_common(2)}")

# defaultdict - automatic default values
expenses_by_category = defaultdict(list)
for i, amount in enumerate(expenses[:len(categories)]):
    expenses_by_category[categories[i]].append(amount)
print(f"Expenses by category: {dict(expenses_by_category)}")

# deque - efficient queue operations (useful for streaming data)
recent_expenses = deque(maxlen=5)  # Keep only last 5 expenses
for expense in expenses:
    recent_expenses.append(expense)
print(f"Recent expenses (last 5): {list(recent_expenses)}")

# 6. PRACTICAL EXAMPLE - Data processing pipeline
print("\n=== DATA PROCESSING EXAMPLE ===")
raw_data = [
    {'amount': 25.50, 'category': 'food', 'date': '2024-01-15'},
    {'amount': 15.75, 'category': 'transport', 'date': '2024-01-15'},
    {'amount': 100.00, 'category': 'utilities', 'date': '2024-01-16'},
    {'amount': 8.25, 'category': 'food', 'date': '2024-01-16'},
]

# Process data using various structures
processed_data = {
    'total_by_category': defaultdict(float),
    'daily_totals': defaultdict(float),
    'all_amounts': [],
    'unique_categories': set()
}

for record in raw_data:
    amount = record['amount']
    category = record['category']
    date = record['date']

    processed_data['total_by_category'][category] += amount
    processed_data['daily_totals'][date] += amount
    processed_data['all_amounts'].append(amount)
    processed_data['unique_categories'].add(category)

print("Processed data:")
for key, value in processed_data.items():
    if isinstance(value, (defaultdict, set)):
        print(f"  {key}: {dict(value) if isinstance(value, defaultdict) else value}")
    else:
        print(f"  {key}: {value}")

# Statistics using built-in functions
amounts = processed_data['all_amounts']
print(f"\nStatistics:")
print(f"  Min: ${min(amounts):.2f}")
print(f"  Max: ${max(amounts):.2f}")
print(f"  Sum: ${sum(amounts):.2f}")
print(f"  Average: ${sum(amounts) / len(amounts):.2f}")
