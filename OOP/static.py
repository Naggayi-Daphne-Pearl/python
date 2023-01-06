# Static methods that are specific to an instance 
class Math:
    """Static methods are specfic to an instance"""
    @staticmethod
    def add5(x):
        return x +5

    @staticmethod
    def add2(x):
        return x + 2

print(Math.add5(5))
print(Math.add2(10))


