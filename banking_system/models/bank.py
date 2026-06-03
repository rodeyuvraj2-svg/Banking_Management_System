from models.accounts import Account
from models.admins import Admins
import json

class Bank:
    def __init__(self, name="SBI"):
        self.name = name
        self.accounts = {}
        self.admins = {}
        self.next_account = 1
        self.next_account_admin = 1

        self.load_data()
        self.next_account = max(self.accounts.keys(), default=0) + 1
        self.next_account_admin = max(self.admins.keys(), default=0) + 1


    def load_data(self):
        try:
            with open("data/accounts.json", "r") as file:
                accounts = json.load(file)

                for acc in accounts:

                    account = Account(
                        acc["id"],
                        acc["name"],
                        acc["email"],
                        acc["password"]
                    )

                    account.balance = acc["balance"]
                    account.transactions = acc["transactions"]

                    self.accounts[account.id] = account

            with open("data/admins.json", "r") as file1:
                admins = json.load(file1)

                for acc in admins:

                    admin = Admins(
                        acc["id"],
                        acc["name"],
                        acc["email"],
                        acc["password"]
                    )

                    self.admins[admin.id] = admin
        except:
            pass

    
    def store(self):
        accounts =[]

        for account in self.accounts.values():
            accounts.append(account.struct())

        with open("data/accounts.json","w") as file:
            json.dump(accounts,file,indent=4)

        admins =[]

        for admin in self.admins.values():
            admins.append(admin.struct_admin())

        with open("data/admins.json","w") as file1:
            json.dump(admins,file1,indent=4)


    def create_account(self,name,email,password):
        for account in self.accounts.values():
            if account.email == email:
                return "Same email account exists."
        
        account = Account(self.next_account,name,email,password)
        self.accounts[account.id] = account
        self.next_account += 1
        self.store()
        return "Account Created."
       
    
    def create_account_admin(self,name,email,password):
        for admin in self.admins.values():
            if admin.email == email:
                return "Same Admin exists."
        
        admin = Admins(self.next_account_admin,name,email,password)
        self.admins[admin.id] = admin
        self.next_account_admin += 1
        self.store()
        return "Account Created."
                

    def find_account(self, email):
        for account in self.accounts.values():
            if account.email == email:
                return account
        return None
            

    def find_account_admin(self, email):
        for account in self.admins.values():
            if account.email == email:
                return account
        return None    
            
    
    def find_by_id(self,id):
        for account in self.accounts.values():
            if account.id == id:
                return account
        return None
            

    def login_customer(self, email, password):
        account = self.find_account(email)
        if account and account.password == password:
            return account
        else:
            return None
        
    
    def login_admins(self, email, password):
        account = self.find_account_admin(email)
        if account and account.password == password:
            return account
        else:
            return None
    

    def delete_account(self,email):
        account = self.find_account(email)
        if account:
            del self.accounts[account.id]
            print("\nAccount deleted.")
            self.store()
        else:
            print("\nFailed to delete Account.")
        

    def delete_account_admin(self,email):
        account = self.find_account_admin(email)
        if account:
            del self.admins[account.id]
            print("\nAccount deleted.")
            self.store()
        else:
            print("\nFailed to delete Account.")


    def transfer_money(self, from_id, to_id, amount):
        s_account = self.find_by_id(from_id)
        r_account = self.find_by_id(to_id)

        if s_account and r_account:
            if s_account.balance >= amount:
                s_account.balance -= amount 
                r_account.balance += amount
                print("\nSucessfully transferred money.")
                s_account.transactions.append(f"Transferred {amount} to {r_account.name}")
                r_account.transactions.append(f"Recieved {amount} from {s_account.name}")
                self.store()
            else:
                print("\nBalance Insufficient.")
        else:
            print("\nAccount not found.")
        

    def show_all_accounts(self):
        if not self.accounts:
            print("\nNo Accounts.")
            return

        print("\nAll accounts: ")
        for account in self.accounts.values():
            print(f"\nId : {account.id}\nName : {account.name}\nEmail : {account.email}\nBalance : {account.balance}")


    def deposit(self,id,amount):
        account = self.find_by_id(id)
        if amount <0:
            print("\nAmount cant be negative.")
        elif account:
            account.balance += amount
            print(f"\nBalance updated.\nCurrent Balance : {account.balance}")
            account.transactions.append(f"Deposited {amount}")
            self.store()
        else:
            print("\nAccount not found.")

    
    def withdraw(self, id, amount):
        account = self.find_by_id(id)
        if account:
            if account.balance < amount:
                print("\nInsufficient Balance.")
            else:
                account.balance -= amount
                print(f"\nBalance updated.\nCurrent Balance : {account.balance}")
                account.transactions.append(f"Withdrawed {amount}")
                self.store()
        else:
            print("\nAccount not found.")


    def check_balance(self,id):
        account = self.find_by_id(id)
        if account:
            print(f"\nCurrent Balance : {account.balance}")
        else:
            print("\nAccount not found.")

    
    def show_transactions(self,id):
        account = self.find_by_id(id)
        if account:
            print("\nAll Transactions : ")
            for i in account.transactions:
                print(i)
        else:
            print("\nAccount not found.")