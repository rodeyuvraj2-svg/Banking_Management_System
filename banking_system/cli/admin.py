from models.bank import Bank

class Admin(Bank):
    def signup_a(self):
        print("\n----- Create Account -----")

        name = input("\nEnter your name : ")
        email = input("Enter your email : ")
        password = input("Enter your password : ")

        print(self.create_account_admin(name,email,password))

    
    def login_a(self):
        
        print("\n----- Login -----")
        email = input("Enter email : ")
        password = input("Enter password : ")

        admin = self.login_admins(email,password)

        if admin:
            while True:
                c = int(input("\n1. Profile\n2. View Accounts\n3. Delete Account \n4. Exit\nEnter your choice : "))

                if c == 1:
                    while True:
                        print(f"\nAccount no : {admin.id}\nName : {admin.name}\nEmail : {admin.email}")

                        ch = int(input("\n1. Edit Profile \n2. Logout\n3. Exit Profile\nEnter your choice : "))

                        if ch == 1:
                            new_name = input("Enter New name : ")
                            self.admins[admin.id].name = new_name
                            print("\nName Updated.")
                        
                        elif ch == 2:
                            return

                        elif ch == 3:
                            break
                        
                        else:
                            print("\nInvalid Choice.")

                elif c == 2:
                    self.show_all_accounts()

                elif c == 3:
                    self.delete_account_admin(admin.email)
                    return

                elif c == 4:
                    return

                else:
                    print("\nInvalid Choice.")
                
        else:
            print("\nAdmin not found.")
