class Admins:
    def __init__(self,id,name,email,password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def struct_admin(self):
        return{
            "id" : self.id,
            "name" : self.name,
            "email" : self.email,
            "password" : self.password
        }