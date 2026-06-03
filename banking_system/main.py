from cli.customer import Customer

c = Customer()

while True:
    print("\n------- Banking System -------\n")
    try:
        ch = int(input("Select your choice\n1. Create Account\n2. Login\n3. Exit\n\nyour choice : "))
    except ValueError:
        print("\nEnter a Valid number.")
        continue

    
    if ch == 1:
        choice = int(input("\n1. Admin\n2. Customer\nyour choice : "))
        
        if choice == 1:
            c.signup_a()
        elif choice == 2:
            c.signup()
        else:
            print("\nEnter a Valid choice.")
    
    elif ch == 2 :
        print("\n----- Login -----")
        user = int(input("\n1. Admin\n2. Customer\nyour choice : "))

        if user == 1:
            c.login_a()
        elif user == 2:
            c.login()
        else:
            print("\nInvalid Choice.")


    elif ch ==3:
        print("\nThank you for visiting.")
        break

    
    else:
        print("\nInvalid Choice.")