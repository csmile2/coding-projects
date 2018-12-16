# project1.py
# Clayton Smiley - 09/29/2018
# MCS 275 - Project 1:
# create a rendition of Sierpinski's Triangle
# reminder to convert to txt when turning in

from matplotlib import pyplot as plt
import random
import numpy as np


#  class which takes implicit argument, and changes the
#  object's value between 1 and 6 inclusive
class DiceRoll(object):
    def __init__(self):
        self.value = random.choice([1, 2, 3, 4, 5, 6])


class Sierpinski(DiceRoll):
    coming_from_point = []
    starting_x_options = [1, 21, 41]
    starting_y_options = [1, 21, 1]

    def __init__(self, pointA, pointB, pointC, iterations, currentX, currentY):
        self.iterations = iterations
        self.currentX = currentX
        self.currentY = currentY
        self.pointA = pointA
        self.pointB = pointB
        self.pointC = pointC
        DiceRoll.__init__(self)  # extend DiceRoll for random vertex to be applied

    def generate_data(self):
        x = 0
        y = 0
        pointsList = []  # empty list for storing all points
        # selects the point based off a randomly generated self.value
        if self.value < 3:
            # x and y two-d list
            x = self.starting_x_options[0]
            y = self.starting_y_options[0]
        elif (self.value < 5) and (self.value > 2):
            x = self.starting_x_options[1]
            y = self.starting_y_options[1]
        else:
            x = self.starting_x_options[2]
            y = self.starting_y_options[2]

        xchoice = []
        ychoice = []
        for i in range(self.iterations):
            xchoice = random.choice(self.starting_x_options)
            index_x = self.starting_x_options.index(xchoice)
            ychoice = self.starting_y_options[index_x]
            x = (xchoice + x) / 2.0
            y = (ychoice + y) / 2.0
            pointsList.append((x, y))

            xlist = []  # add to the list of x points
            ylist = []  # add to the list of y points
            for i in range(len(pointsList)):
                xlist.append(pointsList[i])
                ylist.append(pointsList[i])

        return pointsList

    def plot_data(self, pointsList):
        # print("Instance value: ", self.value)
        # print("iterations is %d" % self.iterations)
        xlist = []
        ylist = []
        pointsList = np.array(pointsList)
        for i in range(len(pointsList)):
            xpoint = pointsList[i][0]
            ypoint = pointsList[i][1]
            xlist.append(xpoint)
            ylist.append(ypoint)


        # plotting the x comma y values in the array
        plt.plot(xlist, ylist, 'k.')

        plt.grid()
        plt.show()


def main():
    # S = Sierpinski([0,0], [20,20], [40,0], 10, 1, 1)
    # print(S.generate_data())
    S = Sierpinski([0, 0], [20, 20], [40, 0], 2500, 1, 1)
    pointsList = S.generate_data()  # returning the points as a list
    S.plot_data(pointsList)


main()
