from abc import ABCMeta, abstractmethod
import math
import numpy as np
from PIL import Image

class Filter:
    __metaclass__ = ABCMeta

    def __init__(self,c=0):
        self.color = c
        self.points = set()

    def getPoints(self):
        return self.points

    @abstractmethod
    def modify(self,image):
       pass

class CircleFilter(Filter):

    def __init__(self,radiusI,radiusO=-1,outside=True,c=0):
        Filter.__init__(self,c)
        self.innerRadius = radiusI
        self.outerRadius = radiusO
        self.outside = outside

    def showMultImage(self,image):
        (height, width) = image.shape
        if (self.outside):
            mult = [[1 for i in range(width)] for j in range(height)]
            if (self.outerRadius != -1):
                self.fillCircle(mult, 0, self.outerRadius, width, height)
                self.fillCircle(mult, 1, self.innerRadius, width, height)
            else:
                self.fillCircle(mult, 0, self.innerRadius, width, height)

        else:
            mult = [[0 for i in range(width)] for j in range(height)]
            if (self.outerRadius != -1):
                self.fillCircle(mult, 1, self.outerRadius, width, height)
                self.fillCircle(mult, 0, self.innerRadius, width, height)
            else:
                self.fillCircle(mult, 1, self.innerRadius, width, height)
        return np.array(mult)

    def modify(self,image):
        (height,width) = image.shape
        if(self.outside):
            mult = [[1 for i in range(width)] for j in range(height)]
            if(self.outerRadius!=-1):
                self.fillCircle(mult,0,self.outerRadius,width,height)
                self.fillCircle(mult,1,self.innerRadius,width,height)
            else:
                self.fillCircle(mult,0,self.innerRadius,width,height)

        else:
            mult = [[0 for i in range(width)] for j in range(height)]
            if(self.outerRadius!=-1):
                self.fillCircle(mult,1,self.outerRadius,width,height)
                self.fillCircle(mult,0,self.innerRadius,width,height)
            else:
                self.fillCircle(mult,1,self.innerRadius,width,height)
        return np.multiply(image,mult)

    def fillCircle(self,arr,num,radius,width,height):
        center = (width/2,height/2)
        for i in range(height):
            for j in range(width):
                if((float(i)-center[1])**2+(float(j)-center[0])**2<float(radius)**2):
                    arr[i][j]=num

class LineFilter(Filter):

    def __init__(self,width,height,c=0):
        Filter.__init__(self,c)
        self.width=width
        self.height=height
        self.mult = [[1 for i in range(width)] for j in range(height)]


    def addLine(self,x1,y1,x2,y2,pixelWidth=1):

        if (abs((x1 - x2) + 1) / abs((y1 - y2) + 1) > 1):
            wdown = True
        else:
            wdown = False

        if wdown:

            if (x1 < x2):
                p1 = (x1, y1)
                p2 = (x2, y2)
            else:
                p2 = (x1, y1)
                p1 = (x2, y2)

            for x in range(p1[0], p2[0] + 1):

                y = (p2[1] - p1[1]) * (x - p1[0]) / (p2[0] - p1[0]) + (p1[1])

                if (y >= 0 and y < self.height and x >= 0 and x < self.width):
                    self.mult[y][x] = 0

                ny2 = y
                pw = pixelWidth
                while (pw > 1):
                    ny2 = ny2 + 1
                    if (ny2 >= 0 and ny2 < self.height and x >= 0 and x < self.width):
                        self.mult[ny2][x] = 0
                    pw = pw - 1

        else:

            if (y1 < y2):
                p1 = (x1, y1)
                p2 = (x2, y2)
            else:
                p2 = (x1, y1)
                p1 = (x2, y2)

            for y in range(p1[1], p2[1] + 1):

                x = (p2[0] - p1[0]) * (y - p1[1]) / (p2[1] - p1[1]) + (p1[0])

                if (y >= 0 and y < self.height and x >= 0 and x < self.width):
                    self.mult[y][x] = 0

                nx2 = x
                pw = pixelWidth
                while (pw > 1):
                    nx2 = nx2 + 1
                    if (y >= 0 and y < self.height and nx2 >= 0 and nx2 < self.width):
                        self.mult[y][nx2] = 0
                    pw = pw - 1

    def modify(self,image):
        return np.multiply(image,self.mult)

