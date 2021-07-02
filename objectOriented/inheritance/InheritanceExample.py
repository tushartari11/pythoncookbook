class A:
    def __init__(self):
        print("In Init of A")

    def feature1(self):
        print("In feature1 of A")


    def feature2(self):
        print("In feature2 of A")


class B:

    def __init__(self):
        print("In Init of B")

    def feature1(self):
        print("In feature1 of B")


    def feature2(self):
        print("In feature2 of B")

class C(A, B):

    def __init__(self):
        super().__init__()
        print("In Init of C")

    def feature1(self):
        super().feature1()
        print("In feature1 of C")


    def feature2(self):
        print("In feature2 of C")

a1 = C()
a1.feature1()
