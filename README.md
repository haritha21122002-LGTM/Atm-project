
# 🏦 ATM Management System using Python & MySQL

A console-based ATM application developed using **Python and MySQL**, simulating basic ATM operations such as balance inquiry, deposit, withdrawal, transaction history, and PIN change with database integration.

## 📌 Features

🔐 PIN Authentication

💰 Check Account Balance

➕ Deposit Money

➖ Withdraw Money (with balance validation)

📄 Transaction History

🔑 Change ATM PIN

🗄️ MySQL Database Integration

🧾 Transaction Records Storage

🚪 Exit ATM Application

## 🛠️ Technologies Used

- Python 3
- MySQL
- mysql-connector-python
- SQL

## 🗂️ Database Structure

### 📋 atm_account Table

```sql
CREATE DATABASE atm_db;

USE atm_db;

CREATE TABLE atm_account (
    id INT PRIMARY KEY,
    pin INT NOT NULL,
    balance DECIMAL(10,2) NOT NULL
);
```

### 📋 transactions Table

```sql
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transaction_type VARCHAR(20),
    amount DECIMAL(10,2),
    balance DECIMAL(10,2)
);
```

## ⚙️ Installation & Setup

### 1️⃣ Install Required Package

```bash
pip install mysql-connector-python
```

### 2️⃣ Configure Database

- Create a database named `atm_db`.
- Create `atm_account` and `transactions` tables.
- Insert sample account data.

```sql
INSERT INTO atm_account (id, pin, balance)
VALUES (1, 242506, 10000);
```

### 3️⃣ Update Database Credentials

Edit these values in the Python file if needed:

```python
host="localhost"
user="root"
password="YOUR_MYSQL_PASSWORD"
database="atm_db"
```

⚠️ **Security Note:** Do not upload your real MySQL password to GitHub.

## ▶️ How to Run

```bash
python atm.py
```

Follow the on-screen instructions to operate the ATM system.

## 📸 Sample Operations

🔐 PIN Authentication

💰 Balance Inquiry

➕ Deposit with real-time balance update

➖ Withdrawal with balance validation

📄 Transaction History

🔑 Secure PIN Change

## 🚀 Future Enhancements

🔐 Secure PIN hashing

🖥️ GUI using Tkinter or Web App using Flask

📊 Enhanced transaction history and reporting

👥 Multiple account management

🔒 Improved login attempt handling

📈 Data visualization using Power BI

## 👩‍💻 Author

Haritha .K

📊 Data Analyst & Data Scientist

🐍 Python | 🗄️ MySQL | 📈 Power BI

---

⭐ If you find this project useful, feel free to star the repository!
