class Math:
    def __init__(self,num):
        self.num = num

    def addtonum(self,n):
        return self.num + n

    @staticmethod
    def add(a,b):
        return a+b

a= Math(10)
print(a.num)
print(a.addtonum(5))
print(Math.add(2,3))