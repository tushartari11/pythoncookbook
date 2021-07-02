class MyEditor:

    def execute(self):
        print("Spellcheck")
        print("Convention check")
        print("Executing")


class PyCharm:

    def execute(self):
        print("Executing")


class Laptop:

    def code(self, ide):
        print("Ide is ", ide)


ide = MyEditor()

ide = PyCharm()

lap1 = Laptop()
lap1.code(ide)
