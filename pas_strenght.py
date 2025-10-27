def password_checking(pasw):
    has_length= len(pasw) >= 8
    has_upper=any(char.isupper()for char in pasw)
    has_lower=any(char.islower()for char in pasw)
    is_digit=any(char.isdigit()for char in pasw)
    has_special=any(char.isalnum()for char in pasw)             
    if all([has_length,has_upper,has_lower,is_digit,has_special]):
        print("PASSWORD FORMAT IS PROPER")
    else:
        print("PASSWORD FORMAT IS NOT GOOD")