import os
import joblib

os.system("clear")
os.system("tput setaf 1")
print("\t\t\t\t\t\t  Welcome to Salary Predictor Application")
print("\t\t\t\t\t\t *****************************************")


os.system("tput setaf 2")
print("\n\nHow many years of experience does the employee has?")

ask=float(input("Type Here(Experience): "))

model=joblib.load('trained_model.pk1')
print("\nPredicted Salary: ",model.predict([[ask]]))
os.system("tput setaf 9")
