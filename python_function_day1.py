import random
import math
import os
import sys


def greeting(name):
	if name == name:
		print("Hello..",name)
	else:
		print("Oh,Then whats your name")

greeting("Nasheeba")

def login(userid, password):
	if userid == "admin" :
		print("Login Successfull")
	elif password == 123:
		print("Your entered password is correct,{}".format("Please Check your user name"))
	else:
		print("Login Failed")

login("admi",12)