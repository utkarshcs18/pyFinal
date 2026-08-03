# sq, cube , sq root

class Calculator:

    @staticmethod
    def greet():
        print(":) Hey there , i hope you are doinn good ?")

    def square(self,num):
        sq = num ** 2 
        return sq


    def cube(self,num):
        cub = num ** 3
        return cub


    def sqRoot(self,num):
        root = num ** 0.5
        return root


a = Calculator()
a.greet()
print(a.square(5))
print(a.cube(5))
print(a.sqRoot(25))