class MyClass:
    def __init__(self):
        self.__private_var = "I am joana"

    def get_private_var(self):
        return self.__private_var

obj = MyClass()
print(obj.get_private_var()) 