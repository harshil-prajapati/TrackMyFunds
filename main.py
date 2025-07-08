import os
import json
from datetime import datetime
from decimal import Decimal, InvalidOperation

# Convert input like '1125' → '01-01-25', '010125' → '01-01-25'
def format_and_validate_date(raw):
    if len(raw) == 4:
        raw = f"01-{raw[:2]}-{raw[2:]}"
    elif len(raw) == 6:
        raw = f"{raw[:2]}-{raw[2:4]}-{raw[4:]}"
    try:
        datetime.strptime(raw, "%d-%m-%y")
        return raw
    except ValueError:
        print("❌ Invalid date format. Use DDMMYY, DD-MM-YY, or 6-digit format like 010125.")
        return None

# Convert date to financial year
def get_financial_year(date_str):
    date_obj = datetime.strptime(date_str, "%d-%m-%y")
    year = date_obj.year
    return f"{year-1}-{year}" if date_obj.month < 4 else f"{year}-{year+1}"

# Setup required folder and file structure
def setup_data_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)
    for file_name in ["accounts.json", "summary.json", "log.json"]:
        file_path = os.path.join(folder_path, file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                json.dump([] if file_name == "log.json" else {}, f, indent=2)
    for tx_type in ["income", "expenses", "transfers"]:
        os.makedirs(os.path.join(folder_path, "transactions", tx_type), exist_ok=True)

# Write a log entry
def write_log(folder_path, action, date, file_path):
    log_file = os.path.join(folder_path, "log.json")
    timestamp = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    log_entry = {"timestamp": timestamp, "user_date": date, "action": action, "file": file_path}
    with open(log_file, 'r+') as f:
        logs = json.load(f)
        logs.append(log_entry)
        f.seek(0)
        json.dump(logs, f, indent=2)
        f.truncate()

# Show all account balances
def display_balances(folder_path):
    accounts_file = os.path.join(folder_path, "accounts.json")
    with open(accounts_file) as f:
        accounts = json.load(f).get("account", {})

    print("\n🔍 Select Account Category :")
    print("1. Saving Account")
    print("2. Loan")
    print("3. Investment")
    print("4. Personal Networth")
    print("5. Total Networth")
    print("6. Enter your own")

    choice = input("Choose an option : ").strip()

    # Normalize user-friendly labels into kebab-case
    category_map = {
        "1": "saving-account",
        "2": "loan",
        "3": "investment",
        "4": "personal"
    }

    if choice == "6":
        user_label = input("Enter category label : ").strip().lower().replace(" ", "-")
    elif choice == "5":
        user_label = "all"
    else:
        user_label = category_map.get(choice)

    if not user_label:
        print("❌ Invalid option.")
        return

    total = 0
    matched_accounts = []

    for account_name, details in accounts.items():
        raw_label = details.get("label", "").lower()
        balance = details.get("balance", 0)

        # Split label by commas and clean
        labels = [lbl.strip() for lbl in raw_label.split(",")]

        if user_label == "all":
            matched = True
        else:
            matched = any(user_label in lbl for lbl in labels)

        if matched:
            total += balance
            matched_accounts.append((account_name, balance))

    if not matched_accounts:
        print("⚠️ No matching accounts found.")
        return

    title = "Net Worth" if user_label == "all" else user_label.replace("-", " ").title()
    print(f"\n📊 {title} :")
    for idx, (name, bal) in enumerate(matched_accounts, 1):
        print(f"{idx}. {name} : ₹ {bal}")

    print(f"💰 Total {title} : ₹ {total}\n")


# Add new transaction (income, expense, transfer)
def add_transaction(folder_path):
    print("\n📥 Transaction Type\n1. Income\n2. Expense\n3. Transfer")
    choice = input("Choose type: ").strip()
    tx_type_map = {"1": "income", "2": "expenses", "3": "transfers"}
    tx_type = tx_type_map.get(choice)
    if not tx_type:
        print("❌ Invalid choice.")
        return

    raw_date = input("Transaction date : ").strip()
    date = format_and_validate_date(raw_date)
    if not date:
        return

    financial_year = get_financial_year(date)
    transaction = {"date": date}

    # Input accounts and amount
    try:
        if tx_type == "income":
            to_acc = input("To Account : ").strip()
            amount = Decimal(input("Amount (₹) : ").strip())
            if amount <= 0: raise InvalidOperation
            transaction.update({"to": to_acc, "amount": float(amount)})

        elif tx_type == "expenses":
            from_acc = input("From Account : ").strip()
            amount = Decimal(input("Amount (₹) : ").strip())
            if amount <= 0: raise InvalidOperation
            transaction.update({"to": from_acc, "amount": float(amount)})

        elif tx_type == "transfers":
            from_acc = input("From Account : ").strip()
            to_acc = input("To Account : ").strip()
            amount = Decimal(input("Amount (₹) : ").strip())
            if amount <= 0: raise InvalidOperation
            transaction.update({"from": from_acc, "to": to_acc, "amount": float(amount)})
    except (InvalidOperation, ValueError):
        print("❌ Invalid amount. Use a positive number.")
        return

    # Optional fields
    for field in ["category", "subcategory", "note"]:
        value = input(f"{field.capitalize()} (optional): ").strip()
        if value:
            transaction[field] = value

    # Save transaction
    tx_file = os.path.join(folder_path, "transactions", tx_type, f"{financial_year}.json")
    os.makedirs(os.path.dirname(tx_file), exist_ok=True)
    if not os.path.exists(tx_file):
        with open(tx_file, 'w') as f:
            f.write("[]")

    with open(tx_file, 'r+') as f:
        data = json.load(f)
        data.append(transaction)
        f.seek(0)
        json.dump(data, f, indent=2)
        f.truncate()

    # Update balances
    acc_file = os.path.join(folder_path, "accounts.json")
    with open(acc_file, 'r+') as f:
        acc_data = json.load(f)
        accounts = acc_data.get("account", {})

        if tx_type == "income":
            if to_acc in accounts:
                accounts[to_acc]["balance"] += float(amount)
            else:
                print(f"⚠️ Account '{to_acc}' not found.")
        elif tx_type == "expenses":
            if from_acc in accounts:
                accounts[from_acc]["balance"] -= float(amount)
            else:
                print(f"⚠️ Account '{from_acc}' not found.")
        elif tx_type == "transfers":
            if from_acc in accounts:
                accounts[from_acc]["balance"] -= float(amount)
            else:
                print(f"⚠️ From account '{from_acc}' not found.")
            if to_acc in accounts:
                accounts[to_acc]["balance"] += float(amount)
            else:
                print(f"⚠️ To account '{to_acc}' not found.")

        f.seek(0)
        json.dump(acc_data, f, indent=2)
        f.truncate()

    write_log(folder_path, f"{tx_type.capitalize()} added", date, tx_file)
    print("✅ Transaction saved.")

# Main menu
def main_menu():
    print("📋 Main Menu\n1. View Balance\n2. Add Transaction\n3. Exit")
    return input("Choose an option : ")

# App Start
if __name__ == "__main__":
    username = input("Enter your name : ").strip().replace(" ", "_")
    user_folder = os.path.join(os.getcwd(), username)
    setup_data_folder(user_folder)

    while True:
        option = main_menu()
        if option == '1':
            display_balances(user_folder)
        elif option == '2':
            add_transaction(user_folder)
        elif option == '3':
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid option.")