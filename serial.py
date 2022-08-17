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
        """Start of generator, makes a new round of serial numbers starting at start"""
        self.start = self.next = start

    def __repr__(self):
        """Shows readable representation of result"""
        print (f"start={self.start} and next={self.next}")

    def generate(self):
        """Returns next number in the sequence"""
        self.next += 1
        return self.next-1

    def reset(self):
        """resets the current number to the originally set start"""
        self.next = self.start

