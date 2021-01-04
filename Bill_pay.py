import random
names=input("Enter the names seperated by ','.\n")
list_names=names.split(",")
list_length=len(list_names)
random_num=(random.randint(0,(list_length-1)))
random_name=list_names[random_num]
print(f"{random_name} has to pay the bill")
