import random as r
import numpy as np
import turtle as birds

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

class MyBird(object):

    def __init__(self,number,flock):
        self.birdie = birds.Turtle()
        self.birdie.speed(10)
        self.number = number
        self.flock = flock
        d = (self.number+1)*10

        # spots when Flock.theta = 0
        self.xspot_o = self.flock.offset - d
        self.yspot_o = d if is_even(number) else -1*d

        # effective spots for arbitary theta
        # set in flock.set_spots
        self.xspot = self.xspot_o
        self.yspot = self.yspot_o



class Flock(object):

    def __init__(self,nbirds,theta=0,speed=300):
        colors  = ["red","green","blue","orange","purple","pink","yellow"]
        self.nbirds = nbirds
        self.offset = nbirds/2 + 1
        self.dummies = [MyBird(j,self) for j in range(nbirds)]
        for bird in self.dummies:
            bird.birdie.color(r.choice(colors))
            bird.birdie.shape('turtle')
        self.theta = theta
        self.speed = speed
        self.x = 0
        self.y = 0
        self.xcoords = None
        self.ycoords = None
        self.reset_coords()

    def reset_coords(self):
        positions = [bird.birdie.position() for bird in self.dummies]
        self.xcoords = [p[0] for p in positions]
        self.ycoords = [p[1] for p in positions]
        self.x = sum(self.xcoords)/float(self.nbirds)
        self.y = sum(self.ycoords)/float(self.nbirds)




    def set_spots(self):

        # get birds into V formation
        for bird in self.dummies:
            # rotation matrix
            bird.xspot = np.cos(self.theta)*bird.xspot_o - np.sin(self.theta)*bird.yspot_o
            bird.yspot = np.sin(self.theta)*bird.xspot_o + np.cos(self.theta)*bird.yspot_o



    def move(self,speed=None,theta=None):
        if speed is None:
            speed = abs(np.random.normal(1,1))
            self.speed = speed
        if theta is None:
            theta = self.theta - np.random.normal(0,.0015)
            self.theta = theta

        self.set_spots()

        flock_xv = speed*np.cos(theta)
        flock_yv = speed*np.sin(theta)

        positions = []
        for bird in self.dummies:
            bx, by = bird.birdie.position()
            to_spot = ((self.x+bird.xspot)/2.0-bx,(self.y+bird.yspot)/2.0-by)
            dbx = to_spot[0]+flock_xv + np.random.normal(30,10)
            dby = to_spot[1]+flock_yv + np.random.normal(30,10)
            bird.birdie.goto(bx+dbx,by+dby)


        self.reset_coords()

        # for bird in self.dummies:
        #     shapeshize = 500/float()
        #     bird.shapesize


            # btheta = theta - np.random.normal(0,10)
            # bspeed = np.random.normal(speed,15)
            # bird.right(btheta)
            # bird.forward(bspeed)


wn = birds.Screen()
wn.bgcolor("lightgreen")
wn.setworldcoordinates(-500,-500,500,500)

myFlock = Flock(10)
mx = max(myFlock.xcoords)
ix = min(myFlock.xcoords)
my = max(myFlock.ycoords)
iy = min(myFlock.ycoords)


xs = [myFlock.x]
ys = [myFlock.y]

while True:

    myFlock.move()
    xs.append(myFlock.x)
    ys.append(myFlock.y)
    mx = max(xs)
    ix = min(xs)
    my = max(ys)
    iy = min(ys)
    d = 300
    wn.setworldcoordinates(ix-d,iy-d,mx+d,my+d)

    # d = max([abs(mx-ix),abs(my-iy)])+10
    # wn.setworldcoordinates(-1*d+myFlock.x,-1*d+myFlock.y,d+myFlock.x,d+myFlock.y)


    #zoomin out
    # myFlock.move()
    # mx = max(myFlock.xcoords+[mx])
    # ix = min(myFlock.xcoords+[ix])
    # my = max([my]+myFlock.ycoords)
    # iy = min([iy]+myFlock.ycoords)
    #
    # d = max([abs(mx-ix),abs(my-iy)])+100
    # wn.setworldcoordinates(-1*d,-1*d,d,d)

    #stay on em
    # mx = myFlock.x+500
    # ix = myFlock.x-500
    # my = myFlock.y + 500
    # im = myFlock.y - 500
    # wn.setworldcoordinates(ix,im,mx,my)

    # mx = max(myFlock.xcoords)
    # ix = min(myFlock.xcoords)
    # my = max(myFlock.ycoords)
    # im = min(myFlock.ycoords)
    # d = max([mx,my,abs(im),abs(ix)]) + 500
    # wn.setworldcoordinates(-1*d,-1*d,d,d)
    # dmax = max([mx,my,dmax])+50
    # dmin = min([ix,im,dmin])-50
    # d = max([abs(dmin),dmax])
    # wn.setworldcoordinates(-1*d,-1*d,d,d)
