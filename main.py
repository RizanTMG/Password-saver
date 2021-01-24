# All the needed library and file classes
import sys
import os
import random
import time
from resources.text_color import *

# Global Variables
holder = 0 # Used to stop printing Unknown input later
"""
def write_key():
	key = Fernet.generate_key()
	with open("key.key", "wb") as key_file:
		key_file.write(key)

def load_key():
	return open("key.key", "rb").read()
"""

# Banner
def banner():
	print (bcolors.OKGREEN +  """
      ____
 _ __/ ___|  __ ___   _____ _ __
| '_ \___ \ / _` \ \ / / _ \ '__|
| |_) |__) | (_| |\ V /  __/ |
| .__/____/ \__,_| \_/ \___|_|
|_|				v0.1
	""" + bcolors.ENDC)

# If the user does not have a account
def account_no():
	# Clears the screen
	os.system('clear')

	# banner
	banner()

	# Asks the user to creat a usrrname
	print (bcolors.OKGREEN + "Creat a username: ")
	username = input("> ")

	# Makes directory of the user
	try:
		os.chdir("accounts")

		# makes directory of the user
		os.mkdir(f"{username}")
		os.chdir(f"{username}")

		# Asks the user to creat a password
		print (bcolors.OKGREEN + "Creat a password: ")
		password = input("> ")


		# Creates a file and adds the uswrname and password to it
		with open("." + f"{username}.txt", "a") as crediantial:
			crediantial.write(password)
		print (bcolors.ENDC)

		os.chdir("..")
		os.chdir("..")

 		# Asks user about login
		account_yes()

		os.system("clear")
	except FileExistsError:
		print(bcolors.WARNING + "Username already exists!" + bcolors.ENDC)
		time.sleep(1)
		os.chdir("..")
		ask_user()

# If user has a accoount
def account_yes():
	# Clears the screen
	os.system('clear')

	# Banner
	banner()

	# Asks the user to enter username and  password
	print (bcolors.OKGREEN + "Enter username: ")
	username = input("> ")

	# gathers username
	os.chdir("accounts")
	files = os.listdir()


	# if username is correct
	if username in files:
		print ("Enter password: ")
		password = input("> ")

		os.chdir(username)
		# reads password and checks it
		with open("." + f"{username}.txt", "r") as checkPass:
			getPass = checkPass.read()

			# Checks the password
			if password == getPass:
				time.sleep(1)
				print (bcolors.OKBLUE + "Login Sucessfull!" + bcolors.ENDC)
				time.sleep(1)
				os.system("clear")

				# Lists the options
				listOptions()
			else:
				time.sleep(1)
				print (bcolors.WARNING + f"Wrong" + bcolors.ENDC)
				os.chdir("..")
				os.chdir("..")
				time.sleep(2)
				os.system("clear")

				ask_user()
	else:
		print (bcolors.WARNING + f"No username named {username}!!!" + bcolors.ENDC)
		os.chdir("..")
		time.sleep(2)
		ask_user()

	# delets variable for low memory usages
	del files

	os.chdir("..")
	os.chdir("..")

# Ask about seeing contents
def listOptions():
	os.system("clear")

	banner()
	print (bcolors.OKGREEN + """What would you like to do:
[1] Save password.
[2] See saved password.
[3] Remove saved password.

[Q] Quit
""")
	answer = input("> ")
	answer = answer.upper()

	if answer == "1":
		saveContent()
	elif answer == "2":
		seeContent()
	elif answer == "3":
		rmContent()
	elif answer == "Q":
		print (bcolors.WARNING + "Quitting!!" + bcolors.ENDC)
		time.sleep(1)
		sys.exit(0)
	else:
		print (bcolors.WARNING + "Unknown Input!!" + bcolors.ENDC)
		listOptions()

# See Contents and password
def seeContent():
	os.system("clear")
	files = os.listdir()
	noFiles = len(files)
	folder = []

	for i in range(0, noFiles):
		item = files[i]
		if "." in item:
			pass
		else:
			folder.append(item)
			del item

	for i in folder:
		print (bcolors.OKGREEN + i)

	print ("\n" + """
[0] Go back.
[Q/q] Exit.
Or Enter site/app to view password!!
""")

	answer = input("> " + bcolors.ENDC)
	answer = answer.title()

	# checks if the input is site or app
	try:
		os.chdir(f"{answer}")

		# Shows password and username
		with open(f"{answer}", "r") as content:
			passwords = content.read()
			print (passwords)

		# stops from printing unknown input
		holder = 1

		# options
		print ("""[1] Go back
[Q/q] Quit
""")
		answer = input(bcolors.OKGREEN + "> ")
		answer = answer.upper()
		if answer == "1":
			os.chdir("..")
			listOptions()
		elif anwer == "Q":
			print (bcolors.WARNING + "Quitting!!" + bcolors.ENDC)
			time.sleep(1)
			sys.exit(0)
		else:
			print (bcolors.WARNING + "Unknown Input!!" + bcolors.ENDC)
			time.sleep(1)
	except:
		pass

	# Checks the answer
	if answer == "0":
		listOptions()
	elif answer == "Q":
		print (bcolors.WARNING + "Quitting!!" + bcolors.ENDC)
		time.sleep(1)
		sys.exit(0)
	else:
		if holder == 0:
			print (bcolors.WARNING + "Unknown Input!!" + bcolors.ENDC)
			time.sleep(1)
		seeContent()

# remove content and password
def rmContent():
	pass

# Save apps/site
def saveContent():
	os.system("clear")
	banner()

	print (bcolors.OKGREEN + ("Enter app/site name: "))
	site = input("> ")
	site = site.title()

	# creat a folder with the name
	try:
		os.mkdir(f"{site}")
	except:
		pass
	os.chdir(f"{site}")

	# ask for username
	print ("Enter your username: ")
	name = input("> ")

	# ask for password
	print("Enter your password: ")
	passW = input("> ")

	# creat a file with the usetname
	with open(f"{site}", "w") as file:
		file.write(f"Username: {name}" + "\n")
		file.write(f"Password: {passW}" + "\n" + "\n")

	# come back to parent directory
	os.chdir("..")

	# Lists options
	listOptions()
# Ask for account
def ask_user():
	os.system("clear")
	# banner
	banner()

	# Asks user if he/she has an account
	print (bcolors.WARNING + "Enter q/Q to exit!")
	print (bcolors.OKGREEN + "Do you have a account(Y/N)?")

	# Stores input in variable answer and turns into upper case
	answer = input("> ")
	answer = answer.upper()

	# Checks the answer
	if answer == "Y":
		account_yes()
	elif answer == "N":
		account_no()
	elif answer == "Q":
		print (bcolors.WARNING + "Quiting!!" + bcolors.ENDC)
		time.sleep(1)
		sys.exit(0)
	else:
		print (bcolors.WARNING + "Enter Y/N only!" + bcolors.ENDC)
		time.sleep(1)
		ask_user()

ask_user()

