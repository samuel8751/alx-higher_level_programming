#!/usr/bin/python3
"""
Module: 101-add_attribute

Defines the add_attribute function.
"""

def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute is added.
        attribute (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    
    setattr(obj, attribute, value)

# Example usage
if __name__ == "__main__":
    class MyClass():
        pass

    mc = MyClass()
    add_attribute(mc, "name", "John")
    print(mc.name)

    try:
        a = "My String"
        add_attribute(a, "name", "Bob")
        print(a.name)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

