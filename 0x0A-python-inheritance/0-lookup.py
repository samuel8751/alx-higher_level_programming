def lookup(obj):
    """
    Function: lookup

    This function returns a list of available attributes and methods of an object.

    :param obj: The object to inspect
    :return: A list of strings representing attributes and methods of the object

    Example usage:
    ```python
    class MyClass:
        my_attr = 42

        def my_method(self):
            pass

    obj = MyClass()
    print(lookup(obj))
    ```
    """
    return [attr for attr in dir(obj)]

# Example usage
class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))

