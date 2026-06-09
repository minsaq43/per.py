pwd = input("What is the master password: ")

def view():
 with open ("password.txt", "r") in f:
    for line in f.readlines():
      data = line.rstrip()
      user,passw = data.split("|")
      print("User:"+user)
def add():
 name = input("Account name: ")
 pwd = input("Password: ")

 with open("password.text" , "a") as f:
  f.write(name +"|"+ pwd + "\n")

while True:
 mode = input("Would you like to add a new password or view existing one or quit(view, add,q) :").lower()

 if mode == "view":
  pass
 elif mode == "add":
  pass
 elif mode == "q":
  quit()
 else:
  print("Invalid mode.")
  continue