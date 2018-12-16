"""
 Project 3 - MCS 260
 Clayton Smiley
 OOP - construct the Triangle class

            Method Synopsis:

Area, which returns the area of a triangle,
Perimeter, which returns the perimeter of a triangle,
Barycenter, which returns the center of a triangle,
LongestSide, which returns the length of the longest side in the triangle,
and IsRightTriangle, which returns True if a triangle is a right
triangle or False if it is not a right triangle.
"""

import math


# Triangle((Ax,Ay),(Bx,By),(Cx,Cy))
class Triangle(object):

    # init fn takes 3 vertices split by their x-y values
    def __init__(self, a1, a2, b1, b2, c1, c2):
        self.A1 = a1
        self.A2 = a2
        self.B1 = b1
        self.B2 = b2
        self.C1 = c1
        self.C2 = c2

    def area(self):
        return (1/2)*abs(self.A1*self.B2+self.B1*self.C2+self.C1*self.A2
                         - self.A1*self.C2 - self.B1*self.A2 - self.C1*self.B2)

    def perimeter(self):
        # between a and b
        AandB = math.sqrt((self.B1-self.A1)**2 + (self.B2-self.A2)**2)
        BandC = math.sqrt((self.C1-self.B1)**2 + (self.C2-self.B2)**2)
        CandA = math.sqrt((self.A1-self.C1)**2 + (self.A2-self.C2)**2)
        return AandB + BandC + CandA

    def barycenter(self):
        xval = (1/3)*(self.A1 + self.B1 + self.C1)
        yval = (1/3)*(self.A2 + self.B2 + self.C2)
        return (xval, yval)

    def longestSide(self):
        AandB = math.sqrt((self.B1-self.A1)**2 + (self.B2-self.A2)**2)
        BandC = math.sqrt((self.C1-self.B1)**2 + (self.C2-self.B2)**2)
        CandA = math.sqrt((self.A1-self.C1)**2 + (self.A2-self.C2)**2)
        sideLengths = [AandB, BandC, CandA]
        sidesDict = {"A and B": AandB, "B and C": BandC, "A and C": CandA}
        maxside = max(sidesDict, key=sidesDict.get)
        maxval  = None
        for key in sidesDict.items():
            if key[0] in maxside:
                maxside, maxval = key[0], key[1]

        return maxside, maxval


    # uses Pythagorean's Theorem to determine if sides   A^2 + B^2  =?=  C^2
    def isRightTriangle(self):
        AandB = math.sqrt((self.B1-self.A1)**2 + (self.B2-self.A2)**2)
        BandC = math.sqrt((self.C1-self.B1)**2 + (self.C2-self.B2)**2)
        CandA = math.sqrt((self.A1-self.C1)**2 + (self.A2-self.C2)**2)
        print("A to B: %f\nB to C: %f\nC to A: %f" % (AandB, BandC, CandA))
        # print(math.sqrt(AandB**2 + BandC**2) , "   ", math.sqrt(CandA**2))  # troubleshooting stmt
        if (math.sqrt(AandB**2 + BandC**2)) == (math.sqrt(CandA**2)):
            return True
        if(math.sqrt(CandA**2 + BandC**2)) == (math.sqrt(AandB**2)):
            return True
        if(math.sqrt(CandA**2 + AandB**2)) == (math.sqrt(BandC**2)):
            return True
        return False


def main():

    T = Triangle(3, -5, 15, 4, -6, 10)
    area = T.area()
    print("The area of the triangle T is %f units squared" % area)
    print("The perimeter of the triangle is", T.perimeter(), "units")
    print("The barycenter of the triangle T is located at", T.barycenter())
    print("The longest side of the triangle is between points "
          "%s and is %s units long." % (T.longestSide()[0], T.longestSide()[1]))
    print("Is Triangle T a right triangle?", T.isRightTriangle())


main()
