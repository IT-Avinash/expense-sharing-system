# Expense Sharing System

A Python-based expense sharing system that calculates individual balances and generates a final settlement between friends.

## Project Overview

This project simplifies the process of splitting shared expenses among a group of people. Users can enter the people involved, specify who paid for an expense, enter the amount, and select the participants who shared that expense.

The program maintains each person's balance and finally determines who owes money to whom.

## Features

- Add multiple users/friends.
- Record expenses paid by different users.
- Split an expense equally among selected participants.
- Maintain the balance of every participant.
- Generate a final settlement between debtors and creditors.
- Accept multiple expenses before calculating the final settlement.
- Interactive command-line interface.

## How It Works

The application follows three main steps:

1. **Create the group**
   - Enter the names of all people participating in the expense sharing.

2. **Record expenses**
   - Enter the person who paid.
   - Enter the amount paid.
   - Enter the people who participated in that expense.
   - The amount is divided equally among the selected participants.

3. **Generate settlement**
   - Positive balances represent people who should receive money.
   - Negative balances represent people who owe money.
   - The program matches debtors with creditors and displays the required payments.

## Example

For a group containing:

- Avi
- Sonai
- Kanna
- Balu

If Balu pays `₹10,000` for Avi, Sonai, and Kanna, the expense is divided equally:

`₹10,000 / 3 = ₹3,333.33`

The final settlement is:

```text
Kanna owes Balu: RS.3333.33
Sonai owes Balu: RS.3333.33
Avi owes Balu: RS.3333.33
```

## Project Structure

```text
expense-sharing-system/
│
├── Gpay_exp_sharing.py
├── README.md
└── screenshots/
    └── output.png
```

## Technologies Used

- Python
- Jupyter Notebook
- Object-Oriented Programming
- Basic data processing and balance calculation

## Core Logic

The project uses an `Expense_sharing` class.

### Balance Calculation

For each expense, the amount is divided by the number of participants. Each participant's balance is reduced by their share, while the payer's balance is increased by the amount they paid.

### Settlement

After all expenses are recorded:

- Users with a positive balance are treated as creditors.
- Users with a negative balance are treated as debtors.
- The program matches debtors and creditors and calculates the payment required to settle the balances.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/IT-Avinash/expense-sharing-system.git
cd expense-sharing-system
```

### 2. Run the Python program

```bash
python Gpay_exp_sharing.py
```

### 3. Follow the prompts

Enter the names, payer, amount, and participants when requested.

To stop entering expenses, type:

```text
done
```

## Sample Input

```text
Enter your names, separated by commas: avi,Sonai,Kanna,Balu

Name of the person who paid or 'done' to finish: Balu
Enter the amount paid: 10000
Enter the name of the participants, separated by commas: Avi,Sonai,Kanna

Name of the person who paid or 'done' to finish: done
```

## Sample Output

```text
Final settlement

Kanna owes Balu:RS.3333.333333
Sonai owes Balu:RS.3333.333333
Avi owes Balu:RS.3333.333333
```

## Limitations

The current version has some limitations:

- Expenses are split equally among participants.
- There is no support for custom percentage or exact-amount splits.
- User input is handled through the command line.
- There is no persistent database for storing expenses.
- The current version does not provide graphical analytics.
- Input validation can be improved for invalid names, amounts, and participants.

## Future Improvements

Planned improvements include:

- Add unequal expense splitting.
- Add percentage-based splitting.
- Add persistent expense storage.
- Add CSV/database support.
- Add expense history.
- Add data visualizations.
- Add spending analysis and insights.
- Build a web interface similar to GPay/expense-sharing applications.
- Improve input validation and error handling.
- Optimize settlement transactions.

## Learning Outcomes

This project demonstrates practical use of:

- Python classes and objects.
- Dictionaries for maintaining user balances.
- Lists and tuples for tracking creditors and debtors.
- Loops and conditional statements.
- User input handling.
- Basic algorithmic problem solving.
- Expense settlement logic.

## Author

**Avinash M R**

GitHub: [IT-Avinash](https://github.com/IT-Avinash)

---

If you find this project useful, consider giving the repository a ⭐.
