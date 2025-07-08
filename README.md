# 💰 TrackMyFunds

**TrackMyFunds** is a simple, fast, and offline-friendly command-line tool to manage personal finances.  
It helps you keep track of your **income**, **expenses**, **transfers**, and **net worth** across labeled accounts such as savings, loans, investments, and more — all stored in clean JSON files.

---

## 🔧 Features

- 📊 View categorized account balances by type (saving, loan, investment, etc.)
- ➕ Add transactions (income, expense, transfer) with date and note
- 🧠 Automatically organizes data by financial year
- 🗂️ JSON-based data structure (no external database needed)
- 🧾 Logs every transaction action with timestamp
- 🔍 Smart label matching (e.g., `credit-card` or `personal-loan`)
- 🧘 Works offline and fully in the terminal

---

## 📁 Folder Structure

```
TrackMyFunds/
├── Test_User/                # User-specific finance folder
│   ├── accounts.json         # Account list with balance and labels
│   ├── log.json              # All actions log
│   ├── summary.json          # Reserved for future summary
│   └── transactions/
│       ├── income/
│       ├── expenses/
│       └── transfers/
└── main.py                   # Application entry point
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/harshil-prajapati/TrackMyFunds.git
cd TrackMyFunds
```

### 2. Run the app

```bash
python main.py
```

You’ll be prompted to enter your name (used for creating your data folder) and then interact with the main menu.

### 📝 Managing Accounts and Users

#### 🔹 Account Setup

Currently, you need to manually enter your account data inside the `accounts.json` file. Here's the format:

```json
{
  "account": {
    "HDFC Bank": {
      "label": "saving-account",
      "balance": 125000.0,
      "note": "Main salary account"
    },
    "Axis Credit Card": {
      "label": "loan, credit-card",
      "balance": -7200.0,
      "limit": 50000,
      "note": "Personal credit card"
    },
    "Groww MF": {
      "label": "investments, mutual-funds",
      "balance": 18000.0,
      "note": "ELSS mutual fund"
    }
  }
}
```

- Use **kebab-case labels** (`saving-account`, `mutual-funds`, etc.)
- Add optional fields like `note`, `limit`, or `emi` for loans

---

#### 🔹 Managing Multiple Users

You can manage multiple users by simply entering different names when you start the program.  
Each user will get their own folder like:

```
TrackMyFunds/
├── Test_User/            ← Your personal data
│   ├── accounts.json
│   └── transactions/...
├── User_Test/            ← Another user
│   ├── accounts.json
│   └── transactions/...
```

When prompted:

```bash
Enter your name (folder will be created): Test_User
```

It will load or create the folder `TrackMyFunds/Test_User/` and work independently from others.

---

## 🧠 Account Labeling Examples

| Category         | Example Labels                                |
|------------------|------------------------------------------------|
| Saving Account   | `saving-account`, `savings-account`            |
| Loan             | `loan`, `credit-card`, `personal-loan`         |
| Investment       | `investments`, `stocks`, `mutual-funds`        |
| Personal         | `personal`, `personal-loan`                    |

These labels are used in filtering and summaries when viewing account balances.

---

## 📈 Planned Features

- Monthly & yearly financial summary reports
- Export data to CSV/Excel
- Visual charts using `matplotlib` or `rich`
- Smart CLI suggestions

---

## 👨‍💻 Author

Made with ❤️ by **Harshil Prajapati**  
If you find this project helpful, feel free to ⭐ star it and share!

---