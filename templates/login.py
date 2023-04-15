import streamlit as st
import pandas as pd
import time
from signup import make_hashes

# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

def login_user(c, username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

def create_usertable(c):
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def view_all_users(c):
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

def login(c):
	st.subheader("Login Section")
	username = st.text_input("User Name")
	password = st.text_input("Password",type='password')
	if st.button("Login"):
		create_usertable(c)
		hashed_pswd = make_hashes(password)
		result = login_user(c, username,check_hashes(password,hashed_pswd))
		if result:
			st.success("Logged In as {}".format(username))
			return True
		else:
			st.warning("Incorrect Username/Password")
			return False
		


