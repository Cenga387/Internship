class User():
    def __init__(self):
        self.email=input('Input your email: ')
        self.password=input('Input your password: ')
        self.birth_date=input('Input your birth date')

    def display_user(self):
        print('Email is', self.email, 'and your hashed password is', hash(self.password), '\nYour birthdate is', self.birth_date)
