# class A:
#     total = 0
#     a = 1
#     _b = 2
#     __c = 3
#     @classmethod
#     def __init__(cls):
#         cls.total += 1
#
#     @staticmethod
#     def num1():
#         print('111')
#
# b1 = A()
# c1 = A()
# # A.__init__(A)
# # A.__init__(A)
# # A.__init__(A)
# A.num1()
# print(A.a, A._b, A._A__c)
#
def minimal(a):
    list_for_minimal = []
    minimal = ''
    for i in a[2::3]:
        list_for_minimal.append(float(i))
    minimal = min(list_for_minimal)
    return minimal
list2_can_drive = ['0', '100', '2.40', '1', '300', '2.30', '2', '400', '2.50', '3', '500', '2.20', '4', '800', '2.60', '5', '1200', '2.50', '6', '1400', '2.40']
print(minimal(list2_can_drive))