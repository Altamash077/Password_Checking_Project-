from common_pas import password_common
from funtions import strengt_of_password
user_password=input("ENTER YOUR PASSWORD TO CHECK ITS STRENGTH: ")
strength_score=strengt_of_password(user_password)
print(f"YOUR PASSWORD STRENGTH SCORE IS: {strength_score}/8")

