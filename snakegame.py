import random



print("welcome to the game")


mylist=["snake","water","gun"]

a=random.choice(mylist)

n=input("enter your name:")

print(f"welcome \n {n}")

print("choices are: snake, water, gun ")
user=input("enter your choice:")
if user==a:
    print(f"its a draw  computer choose \n {a}")
elif user=="snake" and a=="water":
    print(f"you won  comp choose \n {a}")

elif user=="water" and a=="snake":
    print(f"you loose  comp choose \n {a}")

elif user=="gun" and a=="snake":
    print(f"you won  comp choose \n {a}")


elif user=="snake" and a=="gun":
    print(f"you loose  comp choose \n{a}")

elif user=="water" and a=="gun":
    print(f"you won  comp choose \n {a}")

elif user=="gun" and a=="water":
    print(f"you loose  comp choose \n {a}")

else:
    print("something went wrong")










