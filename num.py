def div5(x):
    if(x%5==0):
        return "Divisible by 5"
def div9(x):
    if(x%9==0):
        return "Divisible by 9"
def div10(x):
    if(x%10==0):
        return "Divisible by 10"
def div7(x):
    if(x%7==0):
        return "Divisible by 7"


if __name__=="__main__":
    x=int(input("ENter x"))



    Divisibleby5=div5(x)
    Divisibleby9=div9(x)
    Divisibleby10=div10(x)
    Divisibleby7=div7(x)


    print(Divisibleby5)
    print(Divisibleby9)
    print(Divisibleby10)
    print(Divisibleby7)
