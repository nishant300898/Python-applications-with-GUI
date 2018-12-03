class Turtle:
    def __init__(self):
        import project2
class Word:
    def __init__(self):
        import project1
class Calculate:
    def __init__(self):
        import Calculator
class form1:
    def __init__(self):
        import form2
print("Press 1 to play Turtle race")
print("Press 2 to play Word game")
print("Press 3 to use Calculator")
print("Press 4 to submit Form")
print("Press 5 for exit")
a=int(input())
while(a!=5):
    if(a==1):
       turtle=Turtle()
       a = int(input())
    elif(a==2):
       word=Word()
       a = int(input())
    elif (a == 3):
        calculat = Calculate()
        a = int(input())
    elif (a == 4):
        forme = form1()
        a = int(input())
    elif(a==5):
       break
    else:
       print("Invalid Choice")
       a=int(input())