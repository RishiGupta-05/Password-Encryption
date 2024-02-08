from cryptography.fernet import Fernet



def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as keyFile:
        keyFile.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    return key

key = load_key()
fer = Fernet(key)
def view():
    with open("password.txt","r") as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("|")
            print("User: ", user + " | Password: ", fer.decrypt(passw.encode()).decode())
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("password.txt","a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")



while True:
    mode = input("Add a new password or view existing ones (view,add & q to quit)").lower()

    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode")
        continue
