class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        """
        Add Two Ccmplex numbers
        :param other: complex object-type
        :return: sum of two complex number
        """

        result = Complex(0,0)
        result.real = self.real + other.real
        result.imaginary = self.imaginary + other.imaginary
        return result
    def __sub__(self, other):
        """
        Subtract Two complex numbers
        :param other:
        :return:
        """
        result = Complex(0,0)
        result.real = self.real-other.real
        result.imaginary = self.imaginary- other.imaginary
        return result
    def __mul__(self, other):
        """
        multiply two complex numbers
        :param other:
        :return:
        """
        result = Complex(0,0)
        j = self.imaginary*other.real+self.real*other.imaginary
        Realidad=(self.real*other.real)+(-1*(self.imaginary*other.imaginary))
        result.real = Realidad
        result.imaginary = j
        return result
    def  __divmod__(self, other):
        """
        divide two complex numbers
        :param other:
        :return:
        """
        result = Complex(0,0)
        k = self.imaginary/other.real+self.real/other.imaginary
        Realidad=(self.real/other.real)+(self.imaginary/other.imaginary)
        result.real = Realidad
        result.imaginary = k
        return result
    def __mod__(self, other):
        """
        Add Two Ccmplex numbers
        :param other: complex object-type
        :return: sum of two complex number
        """

        result = Complex(0,0)
        result.real = self.real % other.real
        result.imaginary = self.imaginary % other.imaginary
        return result
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
    C=Complex(6,9)
    D = Complex(4,4)
    print(C)
    print(D)
    print(divmod(C,D))
if __name__ == '__main__':
    main()