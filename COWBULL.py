import random
def game():
    print("hello dear welcome to my game __đŽđšī¸đ°đ")
    name=input("Hello dear enter your name__đĨ°")
    print("welcome dear",name)
    num=set()
    i=1
    while i<=5:
        num.add(random.randint(0,9))
        if len(num)!=5:
            if len(num)==5:
                break
        i=i+1
    list1=list(num)
    print(list1)
    
    j=0
    chance=3
    cow=0
    bull=0
    li2=[]
    li3=[]
    while 1<=chance:
        user_choice=int(input("enter the guess number__"))
        user_position=int(input("enter the position__"))
        li3.append(user_position)
        print("aapke pass bs ",chance,"chances hi bche h__đđđđđđ")
        if user_choice in list1:
            li2.append(user_choice)  
            if li3[j]==list1.index(user_choice):
                bull+=1
                print(bull,"bull")
            else:
                cow+=1
                print(cow,"cow")
        if len(li2)==len(list1)==len(li3)==5:
            break
        chance-=1
        j+=1
    print(li2)
    print(li3)
    if cow<=1 :
        print("losser")
    else:
        print("* congratulations",name, "you have* ",bull,"bulls")
        print("dear",name,"aap jit gye")
    play=input("agr aap dobara khelna chahte ho to : yes/no me se ek dalo___")
    if play=="yes":
        game()
    else:
        return "exit , jab aapka mn kre tb khel lena đĨ°đĨ°đĨ° "
print(game())