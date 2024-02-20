#!/c/Users/anika/AppData/Local/Microsoft/WindowsApps/python3

import os

os.environ["FAV_COLOR"] = input('What is your favorite color? ')
os.environ["NUM_OF_SIBLINGS"] = input('How many siblings do you have? ')
os.environ["UVA_DS_MINOR"] = input('Are you a Data Science minor at UVA? ')

# FAV_COLOR = input('What is your favorite color? ')
# NUM_OF_SIBLINGS = input('How many siblings do you have? ')
# UVA_DS_MINOR = input('Are you a Data Science minor at UVA?' )

print(os.getenv("FAV_COLOR"))
print(os.getenv("NUM_OF_SIBLINGS"))
print(os.getenv("UVA_DS_MINOR"))