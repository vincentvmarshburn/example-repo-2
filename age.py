__author__ = 'noomatik'
from datetime import datetime
YEAR = datetime.now().year
name = input("What is your name? ")
birth = input("What is your year of birth? ")
age = YEAR - int(birth)
print("Hello %s! You are about %s years old." % (name, str(age)))
