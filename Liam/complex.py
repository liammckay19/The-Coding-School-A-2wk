""" Complex.py
Input Format:

One line of input: The real and imaginary part of a number separated by a space.
1 2
3 6

1 + 2i
3 + 6i

Output Format:

For two complex number C and D, the output should be in the following sequence on separate lines:
• C+D
• C-D
• C*D
• C/D
• mod(C)
• mod(D)
"""


# real + imaginary(i)
# i = sqrt(-1)
# i^2 = -1


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other):
        """
        Add two complex numbers
        :param other: Complex object-type
        :return: sum of two complex number
        """
        result = Complex(0, 0)
        result.real = self.real + other.real  # add like terms
        result.imaginary = self.imaginary + other.imaginary
        return result
    
    # TODO: these methods
    def __sub__(self, other):
        pass
    
    def __mul__(self, other):
        pass
    
    def __truediv__(self, other):
        return 'hi'
    
    def __mod__(self):
        # Square root of the sum of the squares.
        # 3+4i mod(3+4i) = sqrt(3^2 + (4i)^2)
        # sqrt(9 - 16)
        # sqrt(-7)
        # = 0 + sqrt(7)i
        # Complex(0, sqrt(7)*i)
        pass
    
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % self.real
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % self.imaginary
            else:
                result = "0.00−%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f−%.2fi" % (self.real, abs(self.imaginary))
        return result


def main():
    C = Complex(2, 4)
    D = Complex(1, 5)
    print(C / D)
    # TODO: • C+D
    # TODO: • C-D
    # TODO: • C*D
    # TODO: • C/D
    # TODO: • mod(C)
    # TODO: • mod(D)


if __name__ == '__main__':
    main()
