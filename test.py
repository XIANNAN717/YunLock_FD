
class D():
    def d(self):
        self.o  = 10
        print('xian')


class A():
    def __init__(self):
        self.a  =1
        print(111111111111111111)


    def b(self):
        self.qq = self.c()
        D1 = D()
        return D1

    def c(self):
        print('cccccccccccc')
        return 'c'

A1 = A()
print(A1.a)
A1.b().d()
D1 = D()

def liaihua():
    print('111')



def xiann(arge):
    arge.d()

l = liaihua

l()