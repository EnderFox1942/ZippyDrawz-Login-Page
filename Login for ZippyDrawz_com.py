import os

ownerusername = "Root"
ownerpassword = "Github"

# switchbord
menu = input("Sign up or login Or ownerlogin")

# sign up page
if menu == "Sign up":
  username = input("Please enter a username!")
  password = input("please enter a password!")
  file = open("user_data.txt", "a")
  file.write(username + ":" + password + "\n")
  file.close()
  print("Signup successful!")

elif menu == "login":
  usernamelogin = input("Please enter your username")
  passwordlogin = input("Please enter your password")

  # Check if the passwords file exists
  if os.path.exists("user_data.txt"):
    file = open("user_data.txt", "r")
    for line in file:
      # Split the line into username and password
      parts = line.strip().split(":")
      if len(parts) == 2:
        stored_username, stored_password = parts
        if usernamelogin == stored_username and passwordlogin == stored_password:
          print("Welcome to the system")
          file.close()
          break  # Exit the loop after successful login
    else:
      print("incorrect username or password")
      file.close()
  else:
    print("Error: Password file not found. Please sign up first.")

# owner login
if menu == "ownerlogin":
  print("please enter your login for the owner system")
  usernameownerlog = input("Please enter your username")
  passwordownerlog = input("please enter your password")
  if usernameownerlog == ownerusername and passwordownerlog == ownerpassword:
    print("Welcome to the Root system")
  else:
    print("Incorrect username or password")