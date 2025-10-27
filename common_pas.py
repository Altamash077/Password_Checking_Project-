import csv
def password_common(password,filename):
    password_set=set()
    with open (filename,newline='') as csvfile:
        reader=csv.reader(csvfile)
        for row in reader:
            password_set.add(row[0])
        return password in password_set