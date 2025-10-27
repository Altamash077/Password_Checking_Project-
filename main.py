from common_pas import password_common
from pas_strenght import password_checking
user_password = input("Enter password: ")
password_checking(user_password)
if password_common(user_password, 'user.csv'):
    print("Password is Common....Found Online")
else:
    print("NOT A COMMON PASSWORD")

