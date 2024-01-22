"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """
        Takes in the starting number for the serial 
        numbers and also creates a variable to store 
        the orginal number
        """
        self.start = start - 1
        self.orig = start - 1

    def __repr__(self):
        return f"SerialGenerator start={self.start+1} Next={self.start+2}"

    def generate(self):
        """Adds one and returns the serial"""
        self.start += 1
        return self.start
    
    def reset(self):
        """uses the stored starting number to reset the serial"""
        self.start = self.orig

