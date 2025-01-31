# String Upper case
class fun1():
    def __init__(self):
        self.str1 = ""
    def enter(self):
        self.str1 = input("Enter String : ")
    def printfun(self):
        print("Result is :", self.str1.upper())

str1 = fun1()
str1.enter()
str1.printfun()