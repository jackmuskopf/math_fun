from __future__ import division
from Tkinter import Tk, Canvas
from PIL import ImageTk, Image, ImageDraw
from random import randint
from math import sin, cos, pi, sqrt
import datetime
import operator

timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

def mean(L):
    w0 = 1
    wn = .01
    return sum(L)/len(L)

def unpack(L, xl, xh, yl, yh):
    r = []
    for j in range(yl, yh):
        for i in range(xl, xh):
            try:
                r.append(L[i][j])
            except IndexError:
                pass
    return r

class Pixel(object):

    def __init__(self,x,y,RGB):
        self.x = x
        self.y = y
        self.red = RGB[0]
        self.green = RGB[1]
        self.blue = RGB[2]
        self.tup = (self.red, self.green, self.blue)

    def gshift(self,delta):
        self.green += int(delta)

    def bshift(self,delta):
        self.blue += int(delta)

    def rshift(self,delta):
        self.red += int(delta)


    def rand_noise(self,amp):
        if abs(amp) < 2:
            pass
        else:
            self.red += randint(-1*amp,amp)
            self.blue += randint(-1*amp,amp)
            self.green += randint(-1*amp,amp)

    def morph(self,thresh):
        if max(self.tup) - min(self.tup) > thresh:
            print 'o'
            self.green = int((1*self.green + .5*self.blue + .5*self.red)/2)
            self.blue = int((1*self.blue + .5*self.green + .5*self.red)/2)
            self.red = int((1*self.red + .5*self.green + .5*self.blue)/2)

        # I think this should be an image method, not pixel
    # def norm_blur(self, img, rad):
    #     rad = int(rad)
    #     xl = self.x - rad
    #     xh = self.x+rad
    #     yl = self.y - rad
    #     yh =self.y+rad
    #
    #     obj_map = img.obj_map
    #     neighbors = unpack(obj_map, xl, xh, yl, yh)
    #     red_avg = int(mean([n.red for n in neighbors]))
    #     green_avg = int(mean([n.green for n in neighbors]))
    #     blue_avg = int(mean([n.blue for n in neighbors]))
    #     self.red = red_avg
    #     self.green = green_avg
    #     self.blue = blue_avg


class IMG(object):

    def __init__(self,filename):

        global timestamp

        # Load the image file
        im = Image.open(filename)
        im = im.convert('RGB')
        width, height = im.size


        name = filename.replace('_'+timestamp,'')
        self.img = im
        self.width = width
        self.height = height
        self.filename = filename
        self.mapname = '.'.join([ name.split('.')[0]+'_map', filename.split('.')[1] ])
        self.objname = '.'.join([ name.split('.')[0]+'_'+timestamp, filename.split('.')[1] ])
        self.raw_pix = im.load()

        # save original; not sure if this is aliasing
        self.orig_pixels = self.init_pix()
        self.orig_map = self.init_map()

        # obj to edit, might be aliasing
        self.pixels = self.init_pix()
        self.obj_map = [[self.pixels[i+j] for j in range(self.height)] for i in range(self.width)]

        self.map = self.init_map()


############ init helpers #######################

    def count(self):
        return self.height * self.width

    def init_pix(self):
        l = []
        for y in range(self.height):
            for x in range(self.width):
                l.append(Pixel(x,y,self.raw_pix[x,y]))
        return l

    def init_map(self):
        #pix map
        pix_map = [[0 for i in range(self.height)] for j in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                pix_map[x][y] = self.raw_pix[x, y]
        return pix_map

    def save_map(self):
        for x in range(self.width):
            for y in range(self.height):
                self.raw_pix[x, y] = self.map[x][y]
        self.img.save(self.mapname)

    def save_obj(self):
        for p in self.pixels:
            self.img.load()[p.x, p.y] = (p.red, p.green, p.blue)
        self.img.save(self.objname)
        return self.objname

    def save_obj_map(self):
        for col in self.obj_map:
            for p in col:
                self.img.load()[p.x,p.y] = (p.red, p.green, p.blue)
        self.img.save(self.objname)
        return self.objname

############### base level transforms #######################
    def gsintrans(self, mag, freq, rand):
        mag0 = mag
        for i in range(self.count()):
            mag = abs(int(mag0*sin(2*freq*pi*i/(self.count()))))
            if rand:
                mag += randint(-1*rand, rand)
            try:
                self.pixels[i].green = self.pixels[i+mag].green
            except IndexError:
                self.pixels[i].green = self.pixels[(i+mag)%self.count()].green

    def bsintrans(self, mag, freq, rand):
        mag0 = mag
        for i in range(self.count()):
            mag = abs(int(mag0*sin(2*freq*pi*i/(self.count()))))
            if rand:
                mag += randint(-1*rand, rand)
            try:
                self.pixels[i].blue = self.pixels[i+mag].blue
            except IndexError:
                self.pixels[i].blue = self.pixels[(i+mag)%self.count()].blue

    def rsintrans(self, mag, freq, rand):
        mag0 = mag
        for i in range(self.count()):
            mag = abs(int(mag0*sin(2*freq*pi*i/(self.count()))))
            if rand:
                mag += randint(-1*rand, rand)
            try:
                self.pixels[i].red = self.pixels[i+mag].red
            except IndexError:
                self.pixels[i].red = self.pixels[(i+mag)%self.count()].red

    def gtrans(self, mag):
        for i in range(self.count()):
            try:
                self.pixels[i].green = self.pixels[i+mag].green
            except IndexError:
                self.pixels[i].green = self.pixels[(i+mag)%self.count()].green

    def btrans(self, mag):
        for i in range(self.count()):
            try:
                self.pixels[i].blue = self.pixels[i+mag].blue
            except IndexError:
                self.pixels[i].blue = self.pixels[(i+mag)%self.count()].blue

    def rtrans(self, mag):
        for i in range(self.count()):
            try:
                self.pixels[i].red = self.pixels[i+mag].red
            except IndexError:
                self.pixels[i].red = self.pixels[(i+mag)%self.count()].red




############## Complete filters #####################

    def rotate(self,theta):
        name = self.save_obj()
        img = Image.open(name)
        img = img.rotate(theta)
        img.save(name)
        self.__init__(name)




    def PixelShift(self, amp, stagger = None):
        if not stagger:
            stagger = {'g':1,'r':1,'b':1}
        g_amp = amp * stagger['g']
        r_amp = amp * stagger['r']
        b_amp = amp * stagger['b']
        self.gtrans(g_amp)
        self.rtrans(r_amp)
        self.btrans(b_amp)

    def sinePixelShift(self, amp, freq, amp_stagger = None, freq_stagger = None, rand = False):
        if not amp_stagger:
            amp_stagger = {'g':1,'r':1,'b':1}
        if not freq_stagger:
            freq_stagger = amp_stagger
        g_amp = amp * amp_stagger['g']
        r_amp = amp * amp_stagger['r']
        b_amp = amp * amp_stagger['b']
        g_freq = freq * freq_stagger['g']
        r_freq = freq * freq_stagger['r']
        b_freq = freq * freq_stagger['b']
        self.gsintrans(g_amp, g_freq, int(rand))
        self.rsintrans(r_amp, r_freq, int(rand))
        self.bsintrans(b_amp, b_freq, int(rand))

    def colorShiftA(self):
        for p in self.pixels:
            r = p.red
            g = p.green
            b = p.blue
            p.red = g
            p.blue = r
            p.green = b

    def colorShiftB(self):
        for p in self.pixels:
            r = p.red
            g = p.green
            b = p.blue
            p.red = b
            p.blue = g
            p.green = r

    def randNoise(self, amp=10):
        namp = -1*amp
        for p in self.pixels:
            p.green += randint(namp,amp)
            p.red += randint(namp,amp)
            p.blue += randint(namp,amp)

    def sineNoise(self, amp=10, freq=10):
        namp = -1*amp
        norm = sqrt(self.height**2 + self.width**2)
        for p in self.pixels:
            pp = p.x + p.y  #pixel phase, makes the sine functions vary by pixel position
            p.green += int(randint(namp,amp)*sin(pi*freq*pp/norm))
            p.red += int(randint(namp,amp)*sin(pi*freq*pp/norm))
            p.blue += int(randint(namp,amp)*sin(pi*freq*pp/norm))

    def cosNoise(self, amp=10, freq=10):
        namp = -1*amp
        norm = sqrt(self.height**2 + self.width**2)
        for p in self.pixels:
            pp = sqrt(p.x**2 + p.y**2)  #pixel phase, makes the sine functions vary by pixel position
            p.green += int(randint(namp,amp)*cos(pi*freq*pp/norm))
            p.red += int(randint(namp,amp)*cos(pi*freq*pp/norm))
            p.blue += int(randint(namp,amp)*cos(pi*freq*pp/norm))

    def contrast(self, percent = 30):
        pct = percent/100
        for p in self.pixels:
            mid = max(p.tup) - (max(p.tup) - min(p.tup))/2
            p.green += int((p.green - mid)*pct)
            p.red += int((p.red - mid)*pct)
            p.blue += int((p.blue -mid)*pct)
            if p.blue < 0:
                p.blue = 0
            elif p.blue > 255:
                p.blue = 255
            if p.green < 0:
                p.green = 0
            elif p.green > 255:
                p.green = 255
            if p.red < 0:
                p.red = 0
            elif p.red > 255:
                p.red = 255


    def brighten(self,amount = 30):
        for p in self.pixels:
            p.green += amount
            p.red += amount
            p.blue += amount

            if p.green > 255:
                p.green = 255
            if p.blue > 255:
                p.blue = 255
            if p.red > 255:
                p.red = 255

    def filterColor(self,rgb):
        if rgb == 'g':
            for p in self.pixels:
                p.green = 0
        elif rgb == 'r':
            for p in self.pixels:
                p.red = 0
        elif rgb == 'b':
            for p in self.pixels:
                p.blue = 0



    def randSwap(self,range):
        for p in self.pixels:
            pass


    # ugh, has weird diagonal divide, why?
    def colorBlur(self):
        for p in self.pixels:
            neighbors = []
            for i in range(-1,2):
                for j in range(-1,2):
                    if i != 0 and j != 0:
                        try:
                            neighbors.append(self.obj_map[p.x+i][p.y+j])
                        except:
                            pass
            l = len(neighbors)
            green = sum([n.green for n in neighbors])/l
            red = sum([n.red for n in neighbors])/l
            blue = sum([n.blue for n in neighbors])/l
            p.green = int((p.green + .5*green)/1.5)
            p.red = int((p.red + .5*red)/1.5)
            p.blue = int((p.blue + .5*blue)/1.5)


    # make sure no pixels turn out like (400,3434,45345) i.e. all over 255
    def reducePix(self):
        for p in self.pixels:
            if max(p.tup) > 255:
                divisor = max(p.tup)/255
                p.green = int(p.green/divisor)
                p.red = int(p.red/divisor)
                p.blue = int(p.blue/divisor)
        # didn't seem to fix white bands that sometimes show up


def clear(canvas):
    canvas.delete('all')

def do_blur(pix, blur, boo):
    global height
    if boo and blur != 0:
        return pix+randint(-1*blur,blur)
    else:
        return pix

def blur_pix(pix, blur, red, green, blue):
    return (do_blur(pix[0], blur ,red), do_blur(pix[1], blur, blue), do_blur(pix[2], blur, green))



def get_pixel(x,y):
    global im
    return im.load()[x,y]

def set_pixel(x,y,val):
    global filename
    global im
    im.load()[x,y] = val
    im.save(filename)

def draw_line(x1,y1,x2,y2,color):
    global canvas; global draw; global im; global filename
    canvas.create_line(x1, y1, x2, y2)
    draw.line((x1, y1, x2, y2), color)
    im.save(filename)

def new_wsltt():
    global canvas
    global draw
    clear()
    im = Image.open('wsltt.jpg')
    draw = ImageDraw.Draw(im)

    # Load the image file
    im = Image.open('wsltt.jpg')

    draw = ImageDraw.Draw(im)

    # Put the image into a canvas compatible class, and stick in an
    # arbitrary variable to the garbage collector doesn't destroy it
    canvas.image = ImageTk.PhotoImage(im)
    # Add the image to the canvas, and set the anchor to the top left / north west corner
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')


def filter_pic(fname):
    # init image object
    img = IMG(fname)

    # transformations ##################
    img.colorShiftA()
    # img.cosNoise(200,30)
    img.sinePixelShift(5,.5,amp_stagger = {'b':0,'g':10, 'r':10},freq_stagger = {'b':2,'r':2,'g':2})
    img.rotate(180)
    img.sinePixelShift(5,.5,amp_stagger = {'b':20,'g':10, 'r':0},freq_stagger = {'b':2,'r':2,'g':20})
    img.rotate(180)
    # img.filterColor('r')
    #####################################

    # save image
    f = img.save_obj()
    #
    # #Create a canvas
    root = Tk()
    im = Image.open(f)
    canvas = Canvas(root, width=im.width, height=im.height)
    canvas.pack()
    # Put the image into a canvas compatible class, and stick in an
    # arbitrary variable to the garbage collector doesn't destroy it
    canvas.image = ImageTk.PhotoImage(im)
    # Add the image to the canvas, and set the anchor to the top left / north west corner
    canvas.create_image(0, 0, image=canvas.image, anchor='nw')
    raw_input('done')

filter_pic('jj.jpg')


# pdict = {}
# for p in img.pixels:
#     if p.tup not in pdict:
#         pdict[p.tup] = 1
#     else:
#         pdict[p.tup] += 1
# mpix = max(pdict.iteritems(), key=operator.itemgetter(1))[0]
# print mpix,pdict[mpix]


# for i in range(img.count()):
#     p = img.pixels[i]
#     p.bshift(200*sin(sin(randint(-3,3))*100*pi*i/img.count()))
#     p.gshift(200*sin(sin(randint(-3,3))*100*pi*i/img.count()))


# img.gtrans(img.height*60.2)
# img.rtrans(img.height*30.2)
# img.btrans(img.height*90.6)


#
# for pix in img.pixels:
#     pix.morph(0)

# img.btrans(150)


# Load the image file

# Add the image to the canvas, and set the anchor to the top left / north west corner



#### first pass at init ############
# filename = 'newsltt.jpg'
#
# white = (255, 255, 255)
# black = (0, 0, 0)
# blue = (0, 0, 255)
# red = (255, 0, 0)
# green = (0,128,0)
#
# root = Tk()
#
# #Create a canvas
# canvas = Canvas(root, width=582, height=584)
# canvas.pack()
#
# # Load the image file
# im = Image.open('wsltt.jpg')
#
# draw = ImageDraw.Draw(im)
#
# # Put the image into a canvas compatible class, and stick in an
# # arbitrary variable to the garbage collector doesn't destroy it
# canvas.image = ImageTk.PhotoImage(im)
# # Add the image to the canvas, and set the anchor to the top left / north west corner
# canvas.create_image(0, 0, image=canvas.image, anchor='nw')
#
# pix = im.load()
#
# width, height = im.size
#
# amp = 200
#
#
# for x in range(width):
#     for y in range(height):
#         blur = amp*sin(100*pi*(y/height))*cos(100*pi*(x/width)) #+ amp*cos(25*pi*(x+y)/(width+height)) - amp
#         blur = abs(int(blur))
#         if blur < 2:
#             blur = 0
#         red, green, blue = False, True, True
#         pix[x,y] = blur_pix(pix[x,y], blur, red, green, blue)
#
# im.save(filename)
# clear()
# im = Image.open(filename)
#
# draw = ImageDraw.Draw(im)
# # Put the image into a canvas compatible class, and stick in an
# # arbitrary variable to the garbage collector doesn't destroy it
# canvas.image = ImageTk.PhotoImage(im)
# # Add the image to the canvas, and set the anchor to the top left / north west corner
# canvas.create_image(0, 0, image=canvas.image, anchor='nw')
#
# input()
###########################
