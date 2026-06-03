# Bank Management System

A command-line banking application built with Python using Object-Oriented Programming and JSON-based data storage.

## Features

### Customer

* Create account
* Login
* View profile
* Edit profile
* Deposit money
* Withdraw money
* Transfer money
* Check balance
* View transaction history
* Delete account

### Admin

* Create admin account
* Login
* View profile
* Edit profile
* View all customer accounts
* Delete admin account

## 📂 Project Structure

```text
banking_system/
│
├── cli/
│   ├── admin.py
│   └── customer.py
│
├── models/
│   ├── bank.py
│   ├── accounts.py
│   └── admins.py
│
├── data/
│   ├── accounts.json
│   └── admins.json
│
└── main.py
```

## Data Storage

All data is stored locally using JSON files:

* `accounts.json`
* `admins.json`

Data persists between program runs.

##  Built With

* Python
* Object-Oriented Programming (OOP)
* JSON File Handling