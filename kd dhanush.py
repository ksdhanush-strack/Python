#PYTHON
#BREAK STAEMENT
1) for i in range(1, 21):
    print(i)
    if i ==10:
        break


2) correct_password ="python123"
for i in range(10):
    password =input("enter password")
    print("access granted")
    break



3) for i in range(100):
    num=int(input("enter number:"))
    if num ==0:
        break


4) numbers =(10, 20,30,40,50)
search =40
for num in numbers:
    if num ==search:
        print("found")
        break


5) for i in range(1 ,101):
    print(i)
    if i %17 ==0:
        break

6) while True:
    print("1,add")
    print("2,delete")
    print("3,exit")
    choise = input("enter choise:")
    if choise =="3":
        break


7) for i in range(100):
    text =input("enter text:")
    if text. lower()=="quit":
        break


8) numbers =(1,3,5,8,10)
for num in numbers:
    if num%2==0:
        print("first even number:",num)
        break


#CONTINUE STATEMENT

1) for i in range(1,21):
    if i ==10:
        continue
    print(i)


2) for i in range(1,51):
    if i%2==0:
        continue
    print(i)


3) for i in range(1,51):
    if i %2!=0:
        continue
    print(i)


4) for i in range(1,101):
    if i %5 ==0:
        continue
    print(i)


5) name="dhanush"
for ch in name:
    if ch.lower()in "aeiou":
        print(ch)
        

6) for i in range(1,31):
    if i %3==0:
        continue
    print(i)


7) numbers =(10,-5,20,-8,30)
for num< 0:
    continue
print(num)


8) for i in range(1,21):
    if i %2==0:
        continue
    print(i)



#PASS STATEMENT


1) def student_details():
    pass


2) class employee:
    pass


3) i=1
while i<=5:
    pass
    break
    

4) for i in range(5):
    pass


5) def calculator():
    pass


6) class bank account:
    pass
    

7) choise =1
if choise==1:
    pass
elif choise ==2:
    pass


8) x=10
if x>5:
    pass

#MIXED QUESTION

1) for i in range(1,51):
    if i %4==0:
        continue
    if i==40:
        break
    print(i)
    

2) correct_user ="admin"
correct_pass="1234"
for i in range(3):
    user=input("username:")
    pwd=input("password:")
    if user == correct_user and pwd ==correct:
        print("login successful")
        break



3) for i in range(1,101):
    if i %10==0:
        continue
    if i ==75:
        break
    print(i)


4) while True:
    print("1. balance")
    print("2. withdraw")
    print("3. exit")
    choise = input("enter choise:")
    if choise =="1":
        pass
    elif choise =="2":
        pass
    elif choise =="3":
        break


5) for  i in range(1,31):
    if i %2==0:
        continue
    if i ==25:
        break
    print(i)

#WHILE LOOP BREAK

1) i=1
while i <=10:
    print(i)
    if i ==5:
        break
    i+=1


2) i=1
while i<=20:
    print(i)
    if i == 15:
        break
    i+=1


3) while True:
    num=int(input("enter number :")

    if num ==0:
            break


4) correct ="python123"
while True:
    password =input("enter password:")
    if password==correct:
        print("correct password")
        break


5)i=1
while i <=100:
    print(i)
    if i==50:
        break
    i+=1


#WHILE LOOP CONTINUE


1) i=0
while i<10:
    i+=1
    if i ==5:
        continue
    print(i)

2) i=0
while i<20:

    i+=1
    if i ==10:
        continue
    print(i)


3) i=0
while i<20:
    i+=1
    if i %2==0:
        continue
    print(i)


4) i=0
while i< 20:
    i+=1
    if1%2!=0:
        continue
    print(i)


i=0
while i<30:
    i+=1
    if i %3 ==0:
        continue
    print(i)

#WHILE LOOP PASS

1) i=1
while i <=5:
    pass
    break

2) i=1
while i<=5:
    if i ==3:
        pass
    else:
        print(i)
        i +=1


3) while False:
    pass


4) i=1
while i<=5:
    if i ==3:
        pass
    else:
        print(i)

        i+=1  


5) running =True
while running:
    pass
    break



#MIXED QUESTION

1) i=1
while i <=20:
    if i==5:
        i+=1
        continue
    if i==15:
        break
    print(i)
    i+=1


2) i=1
while i <=30:
    if i%4==0:
        i+=1
        continue
    if i ==25:
        break
    print(i)
    i+=1
        

3) correct = "admin"
while True:
    password =input("enter password:")

    if password ==correct:
        print("login successful")
        break


4) i=1
while  i<=20:
    if i %2==0:
        i+=1
        continue
    print(i)
    i+=1


while True:
    print("1.add")
    print("2.delete")
    print("3.exit")
    choise = int (input("enter choise:"))

    if choise ==1:
        pass
    elif choise ==2:
        pass
    elif choise ==3:
        break




    

















  































