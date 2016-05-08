from PIL import Image
import numpy as np
from scipy import fftpack
from Filter import *
import pylab as py
from math import pi
import scipy as sp
from scipy import signal

class ImageHandler:

    def __init__(self,fName=None,extend=False):
        if fName!=None:
            self.orig = Image.open(fName).convert('L')
            self.image = Image.open(fName).convert('L')
            self.extend = False
            self.four = self.fourier()

    def loadImage(self,image,extend=False):
        self.image=image
        self.four = self.fourier()

    def fourier(self):
        F1 = fftpack.fft2(self.image)
        F2 = fftpack.fftshift(F1)
        return F2

    def showFourier(self):
        psd2D = np.log(np.abs(self.four)**2+1)
        (height,width) = psd2D.shape
        py.figure(figsize=(10,10*height/width),facecolor='white')
        py.clf()
        py.rc('text',usetex=True)
        py.xlabel(r'$\omega_1$',fontsize=24)
        py.ylabel(r'$\omega_2$',fontsize=24)
        py.xticks(fontsize=16)
        py.yticks(fontsize=16)
        py.imshow( psd2D, cmap='Greys_r',extent=[-pi,pi,-pi,pi],aspect='auto')
        py.show()

    def showImage(self):
        self.image.show()

    def inverseFourier(self):
        self.image = Image.fromarray(np.round(np.real(fftpack.ifft2(fftpack.ifftshift(self.four)))))

    def applyFilter(self,fil):
        self.four = fil.modify(self.four)
        self.inverseFourier()

    def applyKernel(self,kernel):
        pass

    def getImage(self):
        return self.image

    def getOriginal(self):
        return self.orig

    def convolve(self,kernel):
        self.convolveH(np.array(self.image),kernel)

    def convolveH(self,matrix,kernel):
        newmatrix = []
        for y in range(len(matrix)):
            newrow = []
            newmatrix.append(newrow)
            for x in range(len(matrix[0])):
                newvalue = 0
                for ky in range(len(kernel)):
                    for kx in range(len(kernel[0])):
                        yind = y + (ky - len(kernel)/2)
                        xind = x + (kx - len(kernel[0])/2)
                        if(yind>=0 and yind<len(matrix) and xind>=0 and xind<len(matrix[0])):
                            newvalue+=matrix[yind][xind]*kernel[ky][kx]
                newrow.append(newvalue)
        self.image=Image.fromarray(np.array(newmatrix))
        self.four = self.fourier()



