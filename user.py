class bank:


    def __init__ (self, accountNum, owner,balance):
        self.accountNum =accountNum
        self.owner=owner
        self.balance=balance
    

    def withdrawal (self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("We cannot process your withdrawal.")
            print(f"You currently have {self.balance}.")
            print(f"And you are trying to withdraw{amount}.")  


    def display_user_balance(self):
        print(f"Account balance: {self.owner}:{self.balance}.")



    def deposit (self, amount):
        self.balance+= amount
