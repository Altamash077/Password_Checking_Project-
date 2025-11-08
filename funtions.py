def strengt_of_password(pasw):
    sore=0
    if len(pasw)<=8:
        sore+=1
    if len(pasw)<=12:
        sore+=2
    if any(char.isupper()for char in pasw):
        sore+=1
    if any(char.islower()for char in pasw):
        sore+=1
    if any(char.isdigit()for char in pasw):
        sore+=1
    if any(not char.isalnum()for char in pasw):
        sore+=1
    return sore
