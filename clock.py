#clock
from pygame import*
from math import*
from datetime import datetime

def clock(hours,minutes,seconds):
    hour_ang=30*hours-90 #gets the angles of the three hands
    minute_ang=6*minutes-90
    second_ang=6*seconds-90
    hour_x=int(105+60*cos(radians(hour_ang))) #gets the coordinates of each hand
    hour_y=int(105+60*sin(radians(hour_ang)))
    minute_x=int(105+75*cos(radians(minute_ang)))
    minute_y=int(105+75*sin(radians(minute_ang)))
    second_x=int(105+90*cos(radians(second_ang)))
    second_y=int(105+90*sin(radians(second_ang)))
    draw.line(screen,hour_hand,(105,105),(hour_x,hour_y),4) #draws lines
    draw.line(screen,minute_hand,(105,105),(minute_x,minute_y),3)
    draw.line(screen,second_hand,(105,105),(second_x,second_y),2)

def clock_frame():
    draw.circle(screen,hour_hand,(105,105),100,1) #draws frame
    for o in range(0,360,6):
        x=int(105+100*cos(radians(o)))
        y=int(105+100*sin(radians(o)))
        draw.line(screen,hour_hand,(105,105),(x,y),1) #draws the minute incriments
    draw.circle(screen,w,(105,105),95,0)#overlaps a circle to cover center
    for i in range(0,360,30):
        x=int(105+100*cos(radians(i)))
        y=int(105+100*sin(radians(i)))
        draw.line(screen,hour_hand,(105,105),(x,y),2) #draws the 5 minute incriments
    draw.circle(screen,w,(105,105),85,0) #overlaps a circle to cover center

screen=display.set_mode((210,210))

hour_hand=(0,0,0)
minute_hand=(0,0,255)
second_hand=(255,0,0)

w=(255,255,255)
screen.fill(w)

run=True
while run:
    for evt in event.get():
        if evt.type==QUIT:
            run=False
            
    screen.fill(w)
    clock_frame() #draws clock frame
    now=datetime.now() #gets current time on pc
    clock(now.hour,now.minute,now.second) #displays current time on pc
    display.flip()
    time.wait(100)#waits one second before next update
    
quit()

