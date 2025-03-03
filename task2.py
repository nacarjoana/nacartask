class Sample:
    def __init__(self):
        self._protected_var = "I am joana"

obj = Sample()
print(obj._protected_var)  
