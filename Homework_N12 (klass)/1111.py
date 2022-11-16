class A:
    total = 0
    a = 1
    _b = 2
    __c = 3
    @classmethod
    def __init__(cls):
        cls.total += 1

    @staticmethod
    def num1():
        print('111')

b1 = A()
c1 = A()
# A.__init__(A)
# A.__init__(A)
# A.__init__(A)
A.num1()
print(A.a, A._b, A._A__c)


