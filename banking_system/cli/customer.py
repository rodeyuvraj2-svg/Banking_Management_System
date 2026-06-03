from cli.admin import Admin

class Customer(Admin):
    def signup(self):
        print("\n----- Create Account -----")

        name = input("\nEnter your name : ")
        email = input("Enter your email : ")
        password = input("Enter your password : ")

        print(self.create_account(name,email,password))


    def login(self):
        
        print("\n----- Login -----")
        email = input("Enter email : ")
        password = input("Enter password : ")

        customer = self.login_customer(email,password)

        if customer:
            while True:
                c = int(input("\n1. Profile\n2. Deposit\n3. Withdraw \n4. Transfer Money\n5. Check Balance\n6. View Transactions\n7. Exit\nEnter your choice : "))


                if c == 1:
                    while True:
                        print(f"\nAccount no : {customer.id}\nName : {customer.name}\nEmail : {customer.email}")

                        ch = int(input("\n1. Edit Profile \n2. Logout\n3. Delete Account\n4. Exit Profile\nEnter your choice : "))

                        if ch == 1:
                            new_name = input("Enter New name : ")
                            self.accounts[customer.id].name = new_name
                            print("\nName Updated.")
                        
                        elif ch == 2:
                            return
                        
                        elif ch == 3:
                            self.delete_account(customer.email)
                            return

                        elif ch == 4:
                            break
                        
                        else:
                            print("\nInvalid Choice.")

                elif c == 2:
                    amount = int(input("\nEnter Amount to deposit : "))
                    self.deposit(customer.id,amount)

                elif c == 3:
                    amount = int(input("\nEnter Amount to withdraw : "))
                    self.withdraw(customer.id,amount)

                elif c == 4:
                    amount = int(input("\nEnter Amount to Transfer : "))
                    id_r = int(input("\nEnter Recievers Id : "))
                    self.transfer_money(customer.id,id_r,amount)

                elif c == 5:
                    self.check_balance(customer.id)

                elif c == 6:
                    self.show_transactions(customer.id)

                elif c == 7:
                    return

                else:
                    print("\nInvalid Choice.")

        else:
            print("\nCustomer Not Found.")
