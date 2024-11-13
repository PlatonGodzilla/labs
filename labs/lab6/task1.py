class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    
    def set_password(self, newpass):
        self.password = newpass

    def check_password(self, passw):
        if passw == self.password:
            return True
        else:
            return False
        


mydata = UserAccount('drochila228','sexynator@gmail.com','asd')
mypass = 'asd123'
print(mydata.check_password(mypass))
mydata.set_password('asd123')
print(mydata.check_password(mypass))