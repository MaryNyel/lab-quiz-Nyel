import datetime

now = datetime.datetime.now()

print("Full Name: Mary Nyel S. Llabres")
print("Student ID: 211-1098")
print(f"Date and Time: {now}")

issue = input("Networking issue: ")

file = open("./networking_issue.txt", "a")
file.write(issue + " ")
file.close()


