"""LOGIN"""

dict = {"dhruv":"admin123","lucky":"hellolucky", "tirth":"tirth"}

print("Enter you username : ")
username = input()
print("Enter you password : ")
password = input()

pass_fetch = dict[username]

if(password==pass_fetch):
    print("\nLogin Successfull")
    print("\nWelcome ",username)
else:
    print("Wrong Password")