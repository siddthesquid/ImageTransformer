from ImageHandler import *
from Filter import *
from scipy import fftpack
from scipy import signal

def padKernal(width,length,kernel):
    xL = length - len(kernel)
    xW = width - len(kernel[0])
    wPadLeft = xW/2
    wPadRight = xW-wPadLeft
    lPadUp = xL/2
    lPadDown = xL - lPadUp
    nkernal = np.array(kernel)
    npad = ((lPadUp,lPadDown),(wPadLeft,wPadRight))
    newkernel = np.pad(kernel, pad_width=npad, mode='constant', constant_values=0)
    return newkernel


if __name__ == '__main__':

    runCode = 14


    if(runCode==0):
        im = ImageHandler("pics/vertsine.gif")
        im.image.show()
        im.showFourier()
    elif(runCode==1):
        im = ImageHandler("pics/sin4h.gif")
        im.image.show()
        im.showFourier()
    elif(runCode==2):
        im = ImageHandler("pics/diagonalsine.jpg")
        im.image.show()
        im.showFourier()
    elif(runCode==3):
        im = ImageHandler("pics/s2.jpg")
        im.image.show()
        im.showFourier()
    elif(runCode==4):
        im = ImageHandler("pics/s3.jpg")
        im.image.show()
        im.showFourier()
    elif(runCode==5):
        im = ImageHandler("pics/s4.png")
        im.image.show()
        im.showFourier()
    elif(runCode==6):
        im = ImageHandler("pics/flowers8.jpg")
        im.image.show()
        im.showFourier()
    elif(runCode==7):
        im = ImageHandler("pics/lines2.gif")
        im.image.show()
        im.showFourier()
    elif(runCode==8):
        im = ImageHandler("pics/flowersHD.jpg")
        cf = CircleFilter(20,outside=False)
        im.applyFilter(cf)
        im.showFourier()
        im.image.show()
    elif(runCode==9):
        im = ImageHandler("pics/flowersHD.jpg")
        im.image.show()
        im.showFourier()
        cf = CircleFilter(200,outside=False)
        im.applyFilter(cf)
        im.showFourier()
        im.image.show()
    elif(runCode==10):
        im = ImageHandler("pics/flowersHD.jpg")
        #im.image.show()
        #im.showFourier()
        cf = CircleFilter(30,200,outside=False)
        im.applyFilter(cf)
        im.showFourier()
        im.image.show()
    elif(runCode==11):
        im = ImageHandler("pics/flowersHD.jpg")
        im.image.show()
        im.showFourier()
        cf = CircleFilter(30,80,outside=True)
        im.applyFilter(cf)
        im.showFourier()
        im.image.show()
    elif(runCode==12):
        im = ImageHandler("pics/flowersgray.jpg")
        im.image.show()
        im.showFourier()
        (height, width) = im.four.shape
        l = LineFilter(width,height)
        for i in range(83):
            if(i!=41):
                l.addLine(int(23.41*i)-1,0,int(23.41*i)-1,1200,3)
        for i in range(83):
            if (i != 41):
                l.addLine(0, int(14.65 * i) - 1, 1920, int(14.65 * i) - 1, 3)
        im.applyFilter(l)
        im.showFourier()
        im.image.show()
    elif (runCode==13):
        im = ImageHandler("pics/flowersHD.jpg")
        cf = CircleFilter(80,outside=False)
        bigH = cf.showMultImage(im.four)
        im2 = ImageHandler("pics/flowersHD.jpg")
        im2.image = Image.fromarray(np.multiply(bigH,255))
        im2.four = im2.fourier()
        im2.image.show()
        im2.showFourier()
        #im2.showFourier()
        #im2.inverseFourier()
        #im2.image.show()
        #print(np.max(im2.image))
    elif (runCode==14):
        kernel = [[0,0,1.0/13,0,0],[0,1.0/13,1.0/13,1.0/13,0],[1.0/13,1.0/13,1.0/13,1.0/13,1.0/13],[0,1.0/13,1.0/13,1.0/13,0],[0,0,1.0/13,0,0]]
        im = ImageHandler("pics/flowers.jpg")
        im.showImage()
        im.convolve(kernel)
        im.showImage()
        im.showFourier()

        im2 = ImageHandler("pics/flowers.jpg")
        (height,width) = im2.four.shape
        kernelih = ImageHandler()
        kernelih.loadImage(Image.fromarray(padKernal(width,height,kernel)))
        kernelih.showImage()
        kernelih.showFourier()

        #im2.showFourier()
        final = ImageHandler()
        Image.fromarray(signal.fftconvolve(im2.image,kernel)).show()


        final.loadImage(Image.fromarray(np.array([[0]])))
        #final.four=np.multiply(np.fliplr(np.flipud(kernelih.four)),im2.four)
        final.four = np.multiply(kernelih.four, im2.four)
        final.inverseFourier()
        final.showFourier()
        final.showImage()



