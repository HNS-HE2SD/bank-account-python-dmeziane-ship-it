class Client:
    def __init__(self, cin, firstName, lastName, tel=""):
        self.__CIN = cin
        self.__firstName = firstName
        self.__lastName = lastName
        self.__tel = tel
        self.__accounts = []  
    def get_CIN(self):
        return self.__CIN
    def get_firstName(self):
        return self.__firstName
    def get_lastName(self):
        return self.__lastName
    def get_tel(self):
        return self.__tel
    def set_tel(self, tel):
        self.__tel = tel
    def display(self):
        print("CIN:", self.__CIN, ", Name:", self.__firstName, self.__lastName, ", Tel:", self.__tel)
    # Add account
    def add_account(self, account):
        self.__accounts.append(account)
    # all accounts 
    def list_accounts(self):
        print("Accounts of", self.__firstName, self.__lastName)
        if len(self.__accounts) == 0:
            print(" - No accounts.")
        else:
            for acc in self.__accounts:
                print(" - Account", acc.get_code(), "Balance:", acc.get_balance(), "DA")
class Account:
    __nbAccounts = 0  
    def __init__(self, owner):
        Account.__nbAccounts = Account.__nbAccounts + 1
        self.__code = Account.__nbAccounts
        self.__balance = 0
        self.__owner = owner
        self.__transactions = []   
        owner.add_account(self)
    def get_code(self):
        return self.__code
    def get_balance(self):
        return self.__balance
    def get_owner(self):
        return self.__owner
    def credit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
            self.__transactions.append("Credited " + str(amount) + " DA")
        else:
            print("hello , dear client make sure to set a positive amount , even if you are broken money can not be negative")
    # SIMPLE debit
    def debit(self, amount):
        if amount <= 0:
            print("hello , dear client make sure to set a positive amount , even if you are broken money can not be negative hhhh")
        else:
            if self.__balance >= amount:
                self.__balance = self.__balance - amount
                self.__transactions.append("Debited " + str(amount) + " DA")
            else:
                print("Insufficient balance.")
    # SIMPLE transfer
    def transfer(self, amount, otherAccount):
        if amount <= 0:
            print("hello , dear client make sure to set a positive amount , even if you are broken money can not be negative hhhh")
        else:
            if self.__balance >= amount:
                self.__balance = self.__balance - amount
                otherAccount.__balance = otherAccount.__balance + amount
                self.__transactions.append("Transferred " + str(amount) + " DA to Account " + str(otherAccount.get_code()))
                otherAccount.__transactions.append("Received " + str(amount) + " DA from Account " + str(self.__code))
            else:
                print("Insufficient balance ")
    # Display
    def display(self):
        print("Account Code:", self.__code)
        print("Owner:", self.__owner.get_firstName(), self.__owner.get_lastName())
        print("Balance:", self.__balance, "DA")
    #  display transactions
    def displayTransactions(self):
        print("Transactions for Account", self.__code)
        if len(self.__transactions) == 0:
            print(" - No transactions.")
        else:
            for t in self.__transactions:
                print(" -", t)
    @staticmethod
    def displayNbAccounts():
        print("Total accounts created:", Account.__nbAccounts)
