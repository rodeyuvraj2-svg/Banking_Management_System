class Account:
    def __init__(self,id,name,email,password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.balance = 0
        self.transactions = []

    def struct(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "email" : self.email,
            "password" : self.password,
            "balance" : self.balance,
            "transactions" : self.transactions
        }