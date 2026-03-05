# Banking System

A command-line based **banking management system** developed in Python using **Object-Oriented Programming (OOP)** principles.
This project simulates core banking operations such as account creation, deposits, withdrawals, interest calculation, and transaction tracking.

The system also demonstrates **data persistence using JSON**, allowing account information and transaction history to be stored and reloaded between program executions.

---

## Project Overview

The Smart Banking System is designed to simulate basic banking operations while showcasing important programming concepts such as:

* Object-Oriented Programming
* Encapsulation and Inheritance
* File Handling
* Data Persistence
* Transaction Logging
* Error Handling

This project is intended as a **learning-oriented backend system** that demonstrates how financial transactions can be modeled programmatically.

---

## Key Features

* Create new customer bank accounts
* Deposit funds into an account
* Withdraw funds with balance validation
* Check account balance and details
* Savings account with automatic interest calculation
* Transaction history tracking
* Persistent storage using JSON files
* Delete existing accounts
* Input validation and error handling

---

## Technologies Used

* **Python 3**
* **Object-Oriented Programming (OOP)**
* **JSON for data storage**
* **Datetime module for transaction tracking**

---

## System Design

The project is built using a modular class-based design:

**BankAccount**

* Base class representing a standard bank account
* Handles deposits, withdrawals, and balance management

**SavingsAccount**

* Inherits from `BankAccount`
* Adds interest calculation functionality

**BankSystem**

* Manages multiple customer accounts
* Handles account creation, deletion, and data persistence

---

## Example Workflow

1. Create a new bank account
2. Deposit funds
3. Withdraw funds
4. View account details
5. Track transaction history
6. Save account data to JSON
7. Reload stored account data when restarting the program

---

## How to Run the Project

Clone the repository:

```bash
git clone https://github.com/Tejokrishna-v/smart-banking-system.git
```

Navigate into the project directory:

```bash
cd smart-banking-system
```

Run the program:

```bash
python banking_system.py
```

---

## Learning Outcomes

This project demonstrates understanding of:

* Python class design
* Inheritance and encapsulation
* File persistence using JSON
* Structuring a command-line application
* Managing program state and user input

---

## Author

**Tejo Krishna**

Python Developer | Software Engineering 
