class UserAccount:
    def  __init__(self, username, email):
        self.username = username
        self.email = email
        self.__password = None

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, word):
        return True if word == self.__password else False

user1 = UserAccount('Name', 'main@mail.com')

user1.set_password(input(f'{user1.username} set password: '))
print(user1.check_password(input(f'{user1.username} enter password: ')))
