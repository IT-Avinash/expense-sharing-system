class Expense_sharing:
    def __init__(self, friends):
        self.friends = friends
        self.balances = {friend: 0 for friend in friends}
        

    def calculate_expense(self, amount, payer, participants):
        split_amount = amount/len(participants)
        for participant in participants:
            self.balances[participant] -= split_amount
        self.balances[payer] += amount

            
    def settlement(self):
        creditors = []
        debitors = []
        for friend, balance in self.balances.items():
            if balance > 0 :
                creditors.append((friend, balance))
            elif balance < 0:
                debitors.append((friend, -balance))
        while creditors and debitors:
            debitor, debt_amount = debitors.pop()
            creditor, credit_amount = creditors.pop()
            payment = min(debt_amount, credit_amount)
            print(f"{debitor} owes {creditor}:RS.{payment:2f}")

            if debt_amount > payment: 
                debitors.append((debitor, debt_amount - payment))
            elif credit_amount > payment:
                creditors.append((creditor, credit_amount - payment))

if __name__ =="__main__":

    
    friends = input(
        "Enter your names, separated by commas: "
    ).split(",")
    friends = [friend.strip().title() for friend in friends]

    expense_sharing = Expense_sharing(friends)

    while True:
        payer = input("Name of the person who paid or 'done' to finish:")
        if payer.lower() == "done":
            break
        payer = payer.title()
        amount = float(input("Enter the amount paid"))

        participants = input(
            " Enter the name of the participants, seperated by commas:"
        ).split(",")
        participants = [participant.strip().title() for participant in participants]

        expense_sharing.calculate_expense(amount, payer, participants)

print("\n Final settlement")
expense_sharing.settlement()