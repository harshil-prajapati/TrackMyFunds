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
├── YOUR_NAME/                # User-specific finance folder
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
