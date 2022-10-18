import socket
import random
import string

hostname = socket.gethostname()
hostip = socket.gethostbyname(hostname)
# print(f"{hostname} ip is {hostip}")

# mylist = list(string.ascii_lowercase+string.ascii_uppercase + string.digits+"!@#$%^&*()")
# length_pswd = int(input("Enter Length of Input"))
#
# password = []
# for i in range(length_pswd):
#     password.append(random.choice(mylist))
#
# random.shuffle(password)
# print("".join(password))

fruit = ["mango" , "apple" , "grapes" , "water melon" , "melon" , "papaya"]
print(random.random())
print(random.randint(1,10))
print(random.randrange(1,10,2))
random.shuffle(fruit)
print(fruit)
print(random.choice(fruit))





# for i in range(0,10,2):
#     print(i)
#     if i == "apple":
#         print("Loop Terminated")
#         break
# else:
#     print("Loop Ended")


