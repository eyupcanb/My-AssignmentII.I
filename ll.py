__author__ = 'EyupcanBodur'

def square_input(a):
    for i in range(0,int(a)):
        print(int(a)*"*")


def triangle_input(c):
    for i in range(0,int(c)):
        b=i+1
        print(b*"*")


def rectangle_input(f,v): #a=row and b=column
    for i in range(0,f):
        print(int(v)*"*")

while True:

    question_for_shapes=raw_input("Which shape do you want: Triangle, Square or Rectangle?\n(You wanna exit? Enter E!)\n ")
    if question_for_shapes=="Square" or question_for_shapes=="square"  :
        que=input("How many rows do you want?\n(Row must be a number!)\n")
        print square_input(que)



        quex=raw_input("If you wanna continue:Please enter C!\n Or Wanna Exit:Please enter E!\n ")
        if quex == "E" or quex=="e" :
            print("See you!")
            break
        if quex=="C" or quex=="c":
            print("Knowledge is a wisdom!")
            continue
        else:
            print "Please enter the right key !!"



    elif question_for_shapes=="Triangle" or question_for_shapes=="triangle":
        que1=input("How many rows do you want?\n(Row must be a number!)\n")
        print triangle_input(que1)

        quex=raw_input("If you wanna continue:Please enter C!\n Or Wanna Exit:Please enter E!\n ")
        if quex == "E" or   quex=="e" :
            print("See you!")
            break
        if quex=="C" or quex=="c":
            print("Knowledge is a wisdom!")
            continue
        else:
            print "Please enter the right key !!"


    elif question_for_shapes=="Rectangle" or question_for_shapes=="rectangle":
        que2=input("Please enter the row.\n(Row must be a number!)\n")
        que3=input("Please enter the column.\n(Column must be a number!)\n")
        print rectangle_input(que2,que3)


        quex=raw_input("If you wanna continue:Please enter C!\nOr Wanna Exit:Please enter E!\n ")

        if quex == "E" or quex=="e" :
            print("See you!")
            break
        if quex=="C" or quex=="c":
            print("Knowledge is a wisdom!")
            continue
        else:
            print "Please enter the right key !!"

    elif    question_for_shapes=="E" or question_for_shapes=="e":
        print("See you again!")
        break
    
    else:
        print("Enter something right body!!")
