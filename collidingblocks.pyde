
add_library("sound")
m = 1
M = 1e10
vM = -0.1
vm = 0.0
xm = 0.0
xM = 100
Mdraw = xM
mdraw = xm
width = 480;
height = 480;
collisions = 0

def setup():
    global clack
    size(width, height)
    frameRate(1e5)
    clack = SoundFile(this, "C:\Users\DELL\Downloads\clack.mp3")

def change_velocities():
    global vM, vm, M, m
    oldvm = vm
    oldvM = vM
    vm = (2*M*oldvM+(m-M)*oldvm)/(M+m)
    vM = (2*m*oldvm+(M-m)*oldvM)/(M+m)

def check_collisions():
    global xm, xM, vm, vM, collisions, mdraw, Mdraw, clack
    if(xm<=-width/2):
        collisions +=1
        vm = -vm
        #clack.play()
        return 0
    if(xM<=xm+40):
        collisions+=1
        #xM = xm+40+1
        change_velocities()
        #clack.play()
        return 0
    mdraw = xm
    Mdraw = xM
    
def draw():
    global xm, xM, vM, vm, collisions, mdraw, Mdraw
    check_collisions()
    background(255)
    fill(255, 0, 0)
    text("Collisions: "+str(collisions), 20, 20)
    text("xM: "+str(xM), 20, 40)
    text("Mdraw: "+str(Mdraw), 20, 60)
    translate(height/2, width/2)
    fill(200)
    #draw small box
    rect(mdraw, -40, 40, 40)
    
    #draw big box
    rect(Mdraw, -100, 100, 100);
    xm += vm
    xM += vM
