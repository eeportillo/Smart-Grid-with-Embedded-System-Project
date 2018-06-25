import Tkinter as tk
from Tkinter import *
from serial import *
import Image, ImageTk, time, smbus, pyfirmata
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

pgrid = []
ptime = []
totalS = 0

def plotGraph():
    global ax1
    style.use('fivethirtyeight')
    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)
    ani = animation.FuncAnimation(fig, updateGraph, interval=1000)
    plt.show()

def updateGraph(i):
    global ax1
    ax1.clear()
    ax1.plot(ptime, pgrid)

#ADDITION Serial
serialPort = '/dev/ttyACM0'#"COM4" # subject to change on RPi
baudRate = 9600     # Standard on UNO
ser = Serial(serialPort, baudRate, timeout = 0, writeTimeout = 0)   #non-blocking
serBuffer = ""


# Create a new board, specifying serial port
try:
    board = pyfirmata.ArduinoMega('/dev/ttyACM0') # Raspberry Pi
except:
    print("Arduino connection failed")
    try:
         board = pyfirmata.ArduinoMega('/dev/ttyACM1') # Raspberry Pi
    except:
        print("Second Arduino connection failed")
#bus declaration
bus = smbus.SMBus(1)
#open city image
im = Image.open('/home/pi/Desktop/CityFinal.png')
#im = Image.open('///home/pi/Desktop/CityNew.jpg')
#secondary image
im2 = Image.open('/home/pi/Desktop/CityPhotoSmall.png') 

root = tk.Tk() #root window
canvas = Canvas(root,width = 551,height = 369) #canvas holds map and data labels
canvas.grid(row = 0, column = 0,columnspan = 5, rowspan = 10)
# convert images to TKphoto
tkimage = ImageTk.PhotoImage(im)
tkimage2 = ImageTk.PhotoImage(im2)
#add background image
canvas.create_image(0, 0, image = tkimage, anchor = NW)
#industrial power output labels
ind1 = tk.Label(canvas, text = "0.00VA")
#ind1.place(x=15, y=30)
ind2 = tk.Label(canvas, text = "0.00VA")
#ind2.place(x=90, y=30)
ind3 = tk.Label(canvas, text = "0.00VA")
#ind3.place(x=50, y=300)
#commercial power output labels
com1 = tk.Label(canvas, text = "0.00VA")
com1.place(x=255, y=30)
com2 = tk.Label(canvas, text = "0.00VA")
com2.place(x=325, y=30)
com3 = tk.Label(canvas, text = "0.00VA")
com3.place(x=395, y=30)
com4 = tk.Label(canvas, text = "0.00VA")
com4.place(x=465, y=30)
com5 = tk.Label(canvas, text = "0.00VA")
com5.place(x=360 ,y=220)
com6 = tk.Label(canvas, text = "0.00VA")
com6.place(x=465 ,y=320)
#residential power output labels
res1 = tk.Label(canvas, text = "0.00VA")
#res1.place(x=155, y=105)
res2 = tk.Label(canvas, text = "0.00VA")
#res2.place(x=175, y=315)
res3 = tk.Label(canvas, text = "0.00VA")
#res3.place(x=465, y=250)
res4 = tk.Label(canvas, text = "0.00VA")
#res4.place(x=265, y=155)
res5 = tk.Label(canvas, text = "0.00VA")
#res5.place(x=360, y=125)
res6 = tk.Label(canvas, text = "0.00VA")
res6.place(x=360, y=155)
res7 = tk.Label(canvas, text = "0.00VA")
#res7.place(x=465, y=210)
res8 = tk.Label(canvas, text = "0.00VA")
#res8.place(x=210 ,y=220)
res9 = tk.Label(canvas, text = "0.00VA")
res9.place(x=465 ,y=125)
res10 = tk.Label(canvas, text = "0.00VA")
#res10.place(x=465 ,y=155)
res11 = tk.Label(canvas, text = "0.00VA")
#res11.place(x=360 ,y=320)
res1.place(x=465, y=125)
res2.place(x=465, y=155)
res3.place(x=465, y=210)
res4.place(x=465, y=250)
res5.place(x=405, y=315)
res6.place(x=345, y=315)
res7.place(x=175, y=315)
res8.place(x=210 ,y=220)
res9.place(x=175 ,y=105)
res10.place(x=360 ,y=155)
res11.place(x=360 ,y=125)

#variables for relays
varman=BooleanVar()
viewMode = IntVar()
var3 = BooleanVar()
var4 = BooleanVar()
var5 = BooleanVar()
var6 = BooleanVar()
var7 = BooleanVar()
var8 = BooleanVar()
var9 = BooleanVar()
var10 = BooleanVar()
var11 = BooleanVar()
var12 = BooleanVar()
var13 = BooleanVar()
var22 = BooleanVar()
var23 = BooleanVar()
var24 = BooleanVar()
var25 = BooleanVar()
var26 = BooleanVar()
var27 = BooleanVar()
var28 = BooleanVar()
var29 = BooleanVar()
var30 = BooleanVar()
var31 = BooleanVar()
var32 = BooleanVar()
var33 = BooleanVar()
var34 = BooleanVar()
var35 = BooleanVar()
var36 = BooleanVar()
var37 = BooleanVar()
var38 = BooleanVar()
var39 = BooleanVar()
var40 = BooleanVar()
var41 = BooleanVar()
var42 = BooleanVar()
var43 = BooleanVar()
var44 = BooleanVar()
var45 = BooleanVar()
var46 = BooleanVar()
var47 = BooleanVar()
var48 = BooleanVar()
var49 = BooleanVar()
var50 = BooleanVar()
var51 = BooleanVar()
var52 = BooleanVar()
var53 = BooleanVar()

#variables for readings, initialized at 0
#mcontroller 1
r1_0=0
r1_1=0
r1_2=0
r1_3=0
r1_4=0
r1_5=0
r1_6=0
r1_7=0
#mcontroller 2
r2_0=0
r2_1=0
r2_2=0
r2_3=0
r2_4=0
r2_5=0
r2_6=0
r2_7=0
#mcontroller 3
r3_0=0
r3_1=0
r3_2=0
r3_3=0
r3_4=0
r3_5=0
r3_6=0
r3_7=0
#mcontroller 4
r4_0=0
r4_1=0
r4_2=0
r4_3=0
r4_4=0
r4_5=0
r4_6=0
r4_7=0
#mcontroller 5
r5_0=0
r5_1=0
r5_2=0
r5_3=0
r5_4=0
r5_5=0
r5_6=0
r5_7=0
#mcontroller 6
r6_0=0
r6_1=0
r6_2=0
r6_3=0
r6_4=0
r6_5=0
r6_6=0
r6_7=0
#mcontroller 7
r7_0=0
r7_1=0
r7_2=0
r7_3=0
r7_4=0
r7_5=0
r7_6=0
r7_7=0
#mcontroller 8
r8_0=0
r8_1=0
r8_2=0
r8_3=0
r8_4=0
r8_5=0
r8_6=0
r8_7=0
#mcontroller 9
r9_0=0
r9_1=0
r9_2=0
r9_3=0
r9_4=0
r9_5=0
r9_6=0
r9_7=0
#mcontroller 10
r10_0=0
r10_1=0
r10_2=0
r10_3=0
r10_4=0
r10_5=0
r10_6=0
r10_7=0
#mcontroller 11
r11_0=0
r11_1=0
r11_2=0
r11_3=0
r11_4=0
r11_5=0
r11_6=0
r11_7=0
#mcontroller 12
r12_0=0
r12_1=0
r12_2=0
r12_3=0
r12_4=0
r12_5=0
r12_6=0
r12_7=0
#mcontroller 13
r13_0=0
r13_1=0
r13_2=0
r13_3=0
r13_4=0
r13_5=0
r13_6=0
r13_7=0
#mcontroller 14
r14_0=0
r14_1=0
r14_2=0
r14_3=0
r14_4=0
r14_5=0
r14_6=0
r14_7=0
#mcontroller 15
r15_0=0
r15_1=0
r15_2=0
r15_3=0
r15_4=0
r15_5=0
r15_6=0
r15_7=0
#mcontroller 16
r16_0=0
r16_1=0
r16_2=0
r16_3=0
r16_4=0
r16_5=0
r16_6=0
r16_7=0
#power variables
#commercial
compow1=0
compow2=0
compow3=0
compow4=0
compow5=1
compow6=1
#residential
respow1=0
respow2=0
respow3=0
respow4=0
respow5=0
respow6=0
respow7=0
respow8=0
respow9=0
respow10=0
respow11=0
#industrial
indpow1=0
indpow2=0
#indpow3=0
#indpow4=0
dummy = 1

#Variables for N-1 correction
CORRECTION_THRESHOLD = 0.005 # 10mA minimum
nminus1_state = BooleanVar()
nminus1_state.set(0)


#voltage variables

#measurement ground
MGvolt=0
#residential voltages
V1_res1=0
V1_res2=0
V1_res3=0
V1_res4=0
V1_res5=0
V1_res6=0
V1_res7=0
V1_res8=0
V1_res9=0
V1_res10=0
V1_res11=0
V2_res1=0
V2_res2=0
V2_res3=0
V2_res4=0
V2_res5=0
V2_res6=0
V2_res7=0
V2_res8=0
V2_res9=0
V2_res10=0
V2_res11=0
#commercial voltages
V1_com1=0
V1_com2=0
V1_com3=0
V1_com4=0
V1_com5=0
V1_com6=0
V2_com1=0
V2_com2=0
V2_com3=0
V2_com4=0
V2_com5=0
V2_com6=0
V1list_com1 = list({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21})
V1list_com2 = list({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21})
V1list_com3 = list({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21})
V1list_com4 = list({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21})
V1list_com5 = list({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21})
V1list_com6 = list({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21})
V2list_com1 = list({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0.3})
V2list_com2 = list({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0.3})
V2list_com3 = list({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0.3})
V2list_com4 = list({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0.3})
V2list_com5 = list({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0.3})
V2list_com6 = list({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 0.3})
#print(V1list_com5)
#industrial voltages
V1_ind1=0
V1_ind2=0
V1_ind3=0
V1_ind4=0
V2_ind1=0
V2_ind2=0
V2_ind3=0
V2_ind4=0

#Current variables
#residential currents
I_res1=0
I_res2=0
I_res3=0
I_res4=0
I_res5=0
I_res6=0
I_res7=0
I_res8=0
I_res9=0
I_res10=0
I_res11=0
#commercial currents
I_com1=0
I_com2=0
I_com3=0
I_com4=0
I_com5=0
I_com6=0
#industrial currents
I_ind1=0
I_ind2=0
I_ind3=0
I_ind4=0
#commercial PF
PF_com1=1
PF_com2=1
PF_com3=1
PF_com4=1
PF_com5=1
PF_com6=1

#attempt to define pins
try:
    pin3 = board.get_pin('d:3:o')
    pin4 = board.get_pin('d:4:o')
    pin5 = board.get_pin('d:5:o')
    pin6 = board.get_pin('d:6:o')
    pin7 = board.get_pin('d:7:o')
    pin8 = board.get_pin('d:8:o')
    pin9 = board.get_pin('d:9:o')
    pin10 = board.get_pin('d:10:o')
    pin11 = board.get_pin('d:11:o')
    pin12 = board.get_pin('d:12:o')
    pin13 = board.get_pin('d:13:o')
    pin22 = board.get_pin('d:22:o')
    pin23 = board.get_pin('d:23:o')
    pin24 = board.get_pin('d:24:o')
    pin25 = board.get_pin('d:25:o')
    pin26 = board.get_pin('d:26:o')
    pin27 = board.get_pin('d:27:o')
    pin28 = board.get_pin('d:28:o')
    pin29 = board.get_pin('d:29:o')
    pin30 = board.get_pin('d:30:o')
    pin31 = board.get_pin('d:31:o')
    pin32 = board.get_pin('d:32:o')
    pin33 = board.get_pin('d:33:o')
    pin34 = board.get_pin('d:34:o')
    pin35 = board.get_pin('d:35:o')
    pin36 = board.get_pin('d:36:o')
    pin37 = board.get_pin('d:37:o')
    pin38 = board.get_pin('d:38:o')
    pin39 = board.get_pin('d:39:o')
    pin40 = board.get_pin('d:40:o')
    pin41 = board.get_pin('d:41:o')
    pin42 = board.get_pin('d:42:o')
    pin43 = board.get_pin('d:43:o')
    pin44 = board.get_pin('d:44:o')
    pin45 = board.get_pin('d:45:o')
    pin46 = board.get_pin('d:46:o')
    pin47 = board.get_pin('d:47:o')
    pin48 = board.get_pin('d:48:o')
    pin49 = board.get_pin('d:49:o')
    pin50 = board.get_pin('d:50:o')
    pin51 = board.get_pin('d:51:o')
    pin52 = board.get_pin('d:52:o')
    pin2 = board.get_pin('d:2:o')
except:
    print("Cannot define pins")

#initial state all relays open
try:
    pin3.write(1)
    pin4.write(1)
    pin5.write(1)
    pin6.write(1)
    pin7.write(1)
    pin8.write(1)
    pin9.write(1)
    pin10.write(1)
    pin11.write(1)
    pin12.write(1)
    pin13.write(1)
    pin22.write(1)
    pin23.write(1)
    pin24.write(1)
    pin25.write(1)
    pin26.write(1)
    pin27.write(1)
    pin28.write(1)
    pin29.write(1)
    pin30.write(1)
    pin31.write(1)
    pin32.write(1)
    pin33.write(1)
    pin34.write(1)
    pin35.write(1)
    pin36.write(1)
    pin37.write(1)
    pin38.write(1)
    pin39.write(1)
    pin40.write(1)
    pin41.write(1)
    pin42.write(1)
    pin43.write(1)
    pin44.write(1)
    pin45.write(1)
    pin46.write(1)
    pin47.write(1)
    pin48.write(1)
    pin49.write(1)
    pin50.write(1)
    pin51.write(1)
    pin52.write(1)
    pin2.write(1)
    time.sleep(1)
    pin53 = board.get_pin('d:53:o')
    pin53.write(1)
except:
    #error message
    print("Failed to write initial pin condition")

#Define functions for Relay pin control

def set_relay1():  # switch relay on/off
    try:
        relay_val = not var3.get()
        pin3.write(relay_val)
    except:
        print("Pin write failed")

def set_relay2():  # switch relay on/off
    try:
        relay_val = not var4.get()
        pin4.write(relay_val)
    except:
        print("Pin write failed")

def set_relay3():  # switch relay on/off
    try:
        relay_val = not var5.get()
        #print(relay_val)
        if(not relay_val):
            a.deselect()
            j.deselect()
            set_relay1()
            set_relay10()
            time.sleep(0.6)
        #write to relay
        pin5.write(relay_val)
    except:
        print("Pin write failed")

def set_relay4():  # switch relay on/off
    try:
        relay_val = not var6.get()
        pin6.write(relay_val)
    except:
        print("Pin write failed")

def set_relay5():  # switch relay on/off
    try:
        relay_val = not var7.get()
        pin7.write(relay_val)
    except:
        print("Pin write failed")

def set_relay6():  # switch relay on/off
    try:
        relay_val = not var8.get()
        #print(relay_val)
        if(not relay_val):
            m.deselect()
            p.deselect()
            set_relay13()
            set_relay16()
            time.sleep(0.6)
        #write to relay
        pin8.write(relay_val)
    except:
        print("Pin write failed")

def set_relay7():  # switch relay on/off
    try:
        relay_val = not var9.get()
        pin9.write(relay_val)
    except:
        print("Pin write failed")

def set_relay8():  # switch relay on/off
    try:
        relay_val = not var10.get()
        pin10.write(relay_val)
    except:
        print("Pin write failed")

def set_relay9():  # switch relay on/off
    try:
        relay_val = not var11.get()
        #print(relay_val)
        if(not relay_val):
            u.deselect()
            x.deselect()
            set_relay21()
            set_relay24()
            time.sleep(0.6)
        #write to relay
        pin11.write(relay_val)
    except:
        print("Pin write failed")

def set_relay10():  # switch relay on/off
    try:
        relay_val = not var12.get()
        pin12.write(relay_val)
    except:
        print("Pin write failed")

def set_relay11():  # switch relay on/off
    try:
        relay_val = not var13.get()
        pin13.write(relay_val)
    except:
        print("Pin write failed")

def set_relay12():  # switch relay on/off
    try:
        relay_val = not var22.get()
        #print(relay_val)
        if(not relay_val):
            z.deselect()
            kk.deselect()
            set_relay26()
            set_relay37()
            time.sleep(0.6)
        #write to relay
        pin22.write(relay_val)
    except:
        print("Pin write failed")

def set_relay13():  # switch relay on/off
    try:
        relay_val = not var23.get()
        pin23.write(relay_val)
    except:
        print("Pin write failed")

def set_relay14():  # switch relay on/off
    try:
        relay_val = not var24.get()
        pin24.write(relay_val)
    except:
        print("Pin write failed")

def set_relay15():  # switch relay on/off
    try:
        relay_val = not var25.get()
        #print(relay_val)
        if(not relay_val):
            mm.deselect()
            set_relay39()
            time.sleep(0.6)
        #write to relay
        pin25.write(relay_val)
    except:
        print("Pin write failed")

def set_relay16():  # switch relay on/off
    try:
        relay_val = not var26.get()
        pin26.write(relay_val)
    except:
        print("Pin write failed")

def set_relay17():  # switch relay on/off
    try:
        relay_val = not var27.get()
        pin27.write(relay_val)
    except:
        print("Pin write failed")

def set_relay18():  # switch relay on/off
    try:
      #  relay_val = not var28.get()
        relay_val = not var43.get()
        pin28.write(relay_val)
    except:
        print("Pin write failed")

def set_relay19():  # switch relay on/off
    try:
       # relay_val = not var29.get()
       relay_val = not var39.get()
       pin29.write(relay_val)
    except:
        print("Pin write failed")

def set_relay20():  # switch relay on/off
    try:
        relay_val = not var30.get()
        #print(relay_val)
        if(not relay_val):
            aa.deselect()
            set_relay27()
            time.sleep(0.6)
        #write to relay
        pin30.write(relay_val)
    except:
        print("Pin write failed")

def set_relay21():  # switch relay on/off
    try:
        relay_val = not var31.get()
        pin31.write(relay_val)
    except:
        print("Pin write failed")

def set_relay22():  # switch relay on/off
    try:
        relay_val = not var32.get()
        pin32.write(relay_val)
    except:
        print("Pin write failed")

def set_relay23():  # switch relay on/off
    try:
        relay_val = not var33.get()
        #print(relay_val)
        if(not relay_val):
            b.deselect()
            e.deselect()
            set_relay2()
            set_relay5()
            time.sleep(0.6)
        #write to relay
        pin33.write(relay_val)
    except:
        print("Pin write failed")

def set_relay24():  # switch relay on/off
    try:
        relay_val = not var34.get()
        pin34.write(relay_val)
    except:
        print("Pin write failed")

def set_relay25():  # switch relay on/off
    try:
        relay_val = not var35.get()
        #print(relay_val)
        if(not relay_val):
            h.deselect()
            k.deselect()
            set_relay11()
            set_relay8()
            time.sleep(0.6)
        #write to relay
        pin35.write(relay_val)
    except:
        print("Pin write failed")

def set_relay26():  # switch relay on/off
    try:
        relay_val = not var36.get()
        pin36.write(relay_val)
    except:
        print("Pin write failed")

def set_relay27():  # switch relay on/off
    try:
        relay_val = not var37.get()
        pin37.write(relay_val)
    except:
        print("Pin write failed")

def set_relay28():  # switch relay on/off
    try:
        relay_val = not var38.get()
        pin38.write(relay_val)
    except:
        print("Pin write failed")

def set_relay29():  # switch relay on/off
    try:
        relay_val = not var39.get()
        pin39.write(relay_val)
        set_relay19()
    except:
        print("Pin write failed")

def set_relay30():  # switch relay on/off
    try:
        relay_val = not var40.get()
        pin40.write(relay_val)
    except:
        print("Pin write failed")

def set_relay31():  # switch relay on/off
    try:
        relay_val = not var41.get()
        pin41.write(relay_val)
    except:
        print("Pin write failed")

def set_relay32():  # switch relay on/off
    try:
        relay_val = not var42.get()
        pin42.write(relay_val)
    except:
        print("Pin write failed")

def set_relay33():  # switch relay on/off
    try:
        relay_val = not var43.get()
        pin43.write(relay_val)
        set_relay18()
    except:
        print("Pin write failed")

def set_relay34():  # switch relay on/off
    try:
        relay_val = not var44.get()
        pin44.write(relay_val)
    except:
        print("Pin write failed")

def set_relay35():  # switch relay on/off
    try:
        relay_val = not var45.get()
        pin45.write(relay_val)
    except:
        print("Pin write failed")

def set_relay36():  # switch relay on/off
    try:
        relay_val = not var46.get()
        #print(relay_val)
        if(not relay_val):
            v.deselect()
            n.deselect()
            set_relay14()
            set_relay22()
            time.sleep(0.6)
        #write to relay
        pin46.write(relay_val)
    except:
        print("Pin write failed")

def set_relay37():  # switch relay on/off
    try:
        relay_val = not var47.get()
        pin47.write(relay_val)
    except:
        print("Pin write failed")

def set_relay38():  # switch relay on/off
    try:
        relay_val = not var48.get()
        #print(relay_val)
        if(not relay_val):
            q.deselect()
            set_relay17()
            time.sleep(0.6)
        #write to relay
        pin48.write(relay_val)
    except:
        print("Pin write failed")

def set_relay39():  # switch relay on/off
    try:
        relay_val = not var49.get()
        pin49.write(relay_val)
    except:
        print("Pin write failed")

def set_relay40():  # switch relay on/off
    try:
        relay_val = not var50.get()
        pin50.write(relay_val)
    except:
        print("Pin write failed")

def set_relay41():  # switch relay on/off
    try:
        relay_val = not var51.get()
        pin51.write(relay_val)
    except:
        print("Pin write failed")

def set_relay42():  # switch relay on/off
    try:
        relay_val = not var52.get()
        pin52.write(relay_val)
    except:
        print("Pin write failed")

def set_relay43():  # switch relay on/off
    try:
        relay_val = not var53.get()
        #print(relay_val)
        if(not relay_val):
            d.deselect()
            g.deselect()
            set_relay4()
            set_relay7()
            time.sleep(0.6)
        #write to relay
        pin2.write(relay_val)
    except:
        print("Pin write failed")


#place relay checkboxes
a = Checkbutton(root, text = "Residential 2: backup 1", command = set_relay1, variable = var3, state=DISABLED)
var3.set(0) #initially unchecked
a.grid(column = 2, row = 13)

b = Checkbutton(root, text = "Residential 8: backup 1", command = set_relay2, variable = var4, state=DISABLED)
var4.set(0) #initially unchecked
b.grid(column = 2, row = 21)

c = Checkbutton(root, text = "Residential 2", command = set_relay3, variable = var5)
var5.set(0) #initially unchecked
c.grid(column = 0, row = 12)

d = Checkbutton(root, text = "Power Consumption Graph", command = plotGraph)
var6.set(0) #initially unchecked
d.grid(column = 2, row = 11)

e = Checkbutton(root, text = "Residential 8: backup 2", command = set_relay5, variable = var7, state=DISABLED)
var7.set(0) #initially unchecked
e.grid(column = 3, row = 11)

f = Checkbutton(root, text = "Residential 3", command = set_relay6, variable = var8)
var8.set(0) #initially unchecked
f.grid(column = 0, row = 13)

g = Checkbutton(root, text = "Residential 1: backup 2", command = set_relay7, variable = var9, state=DISABLED)
var9.set(0) #initially unchecked
g.grid(column = 2, row = 12)

h = Checkbutton(root, text = "Residential 9: backup 1", command = set_relay8, variable = var10, state=DISABLED)
var10.set(0) #initially unchecked
h.grid(column = 3, row = 12)

i = Checkbutton(root, text = "Residential 4", command = set_relay9, variable = var11)
var11.set(0) #initially  unchecked
i.grid(column = 0, row = 14)

j = Checkbutton(root, text = "Residential 2: backup 2", command = set_relay10, variable = var12, state=DISABLED)
var12.set(0) #initially  unchecked
j.grid(column = 2, row = 14)

k = Checkbutton(root, text = "Residential 9: backup 2", command = set_relay11, variable = var13, state=DISABLED)
var13.set(0) #initially  unchecked
k.grid(column = 3, row = 13)

L = Checkbutton(root, text = "Residential 5", command = set_relay12, variable = var22)
var22.set(0) #initially  unchecked
L.grid(column = 0, row = 15)

m = Checkbutton(root, text = "Residential 3: backup 1", command = set_relay13, variable = var23, state=DISABLED)
var23.set(0) #initially  unchecked
m.grid(column = 2, row = 15)

n = Checkbutton(root, text = "Residential 10: backup 1", command = set_relay14, variable = var24, state=DISABLED)
var24.set(0) #initially  unchecked
n.grid(column = 3, row = 14)

o = Checkbutton(root, text = "Residential 6", command = set_relay15, variable = var25)
var25.set(0) #initially  unchecked
o.grid(column = 0, row = 16)

p = Checkbutton(root, text = "Residential 3: backup 2", command = set_relay16, variable = var26, state=DISABLED)
var26.set(0) #initially  unchecked
p.grid(column = 2, row = 16)

q = Checkbutton(root, text = "Residential 11: backup", command = set_relay17, variable = var27, state=DISABLED)
var27.set(0) #initially  unchecked
q.grid(column = 3, row = 16)

#r = Checkbutton(root, text = "Industrial 1", command = set_relay18, variable = var28)
#var28.set(0) #initially  unchecked
#r.grid(column = 1, row = 17)

#s = Checkbutton(root, text = "Industrial 2", command = set_relay19, variable = var29)
#var29.set(0) #initially  unchecked
#s.grid(column = 1, row = 18)

t = Checkbutton(root, text = "Residential 7", command = set_relay20, variable = var30)
var30.set(0) #initially  unchecked
t.grid(column = 0, row = 17)

u = Checkbutton(root, text = "Residential 4: backup 1", command = set_relay21, variable = var31, state=DISABLED)
var31.set(0) #initially  unchecked
u.grid(column = 2, row = 17)

v = Checkbutton(root, text = "Residential 10: backup 2", command = set_relay22, variable = var32, state=DISABLED)
var32.set(0) #initially  unchecked
v.grid(column = 3, row = 15)

w = Checkbutton(root, text = "Residential 8", command = set_relay23, variable = var33)
var33.set(0) #initially  unchecked
w.grid(column = 0, row = 18)

x = Checkbutton(root, text = "Residential 4: backup 2", command = set_relay24, variable = var34, state=DISABLED)
var34.set(0) #initially  unchecked
x.grid(column = 2, row = 18)

y = Checkbutton(root, text = "Residential 9", command = set_relay25, variable = var35)
var35.set(0) #initially  unchecked
y.grid(column = 0, row = 19)

z = Checkbutton(root, text = "Residential 5: backup 1", command = set_relay26, variable = var36, state=DISABLED)
var36.set(0) #initially  unchecked
z.grid(column = 2, row = 18)

aa = Checkbutton(root, text ="Residential 7: backup", command = set_relay27, variable = var37, state=DISABLED)
var37.set(0) #initially  unchecked
aa.grid(column = 2, row = 20)

bb = Checkbutton(root, text ="Commercial 1", command = set_relay28, variable = var38)
var38.set(0) #initially  unchecked
bb.grid(column = 1, row = 11)

cc = Checkbutton(root, text ="Commercial 2", command = set_relay29, variable = var39)
var39.set(0) #initially  unchecked
cc.grid(column = 1, row = 12)

dd = Checkbutton(root, text ="Commercial 3", command = set_relay30, variable = var40)
var40.set(0) #initially  unchecked
dd.grid(column = 1, row = 13)

ee = Checkbutton(root, text ="Commercial 4", command = set_relay31, variable = var41)
var41.set(0) #initially  unchecked
ee.grid(column = 1, row = 14)

ff = Checkbutton(root, text ="Commercial 5", command = set_relay32, variable = var42)
var42.set(0) #initially  unchecked
ff.grid(column = 1, row = 15)

gg = Checkbutton(root, text ="Commercial 6", command = set_relay33, variable = var43)
var43.set(0) #initially  unchecked
gg.grid(column = 1, row = 16)

#hh = Checkbutton(root, text ="Industrial", command = set_relay34, variable = var44)
#var44.set(0) #initially  unchecked
#hh.grid(column = 1, row = 17)

ii = Checkbutton(root, text = "Industrial", command = set_relay35, variable = var45)
var45.set(0) #initially  unchecked
ii.grid(column = 1, row = 17)

jj = Checkbutton(root, text = "Residential 10", command = set_relay36, variable = var46)
var46.set(0) #initially  unchecked
jj.grid(column = 0, row = 20)

kk = Checkbutton(root, text = "Residential 5: backup 2", command = set_relay37, variable = var47, state=DISABLED)
var47.set(0) #initially  unchecked
kk.grid(column = 3, row = 13)

ll = Checkbutton(root, text = "Residential 11", command = set_relay38, variable = var48)
var48.set(0) #initially  unchecked
ll.grid(column = 0, row = 21)

mm = Checkbutton(root, text = "Residential 6: backup", command = set_relay39, variable = var49, state=DISABLED)
var49.set(0) #initially  unchecked
mm.grid(column = 2, row = 19)


qq = Checkbutton(root, text = "Residential 1", command = set_relay43, variable = var53)
var53.set(0) #initially  unchecked
qq.grid(column = 0, row = 11)

def exitButton():
    #set all relays open
    #close program
    print("Exiting")
    try:
        pin53.write(0)
        pin3.write(1)
        pin4.write(1)
        pin5.write(1)
        pin6.write(1)
        pin7.write(1)
        pin8.write(1)
        pin9.write(1)
        pin10.write(1)
        pin11.write(1)
        pin12.write(1)
        pin13.write(1)
        pin22.write(1)
        pin23.write(1)
        pin24.write(1)
        pin25.write(1)
        pin26.write(1)
        pin27.write(1)
        pin28.write(1)
        pin29.write(1)
        pin30.write(1)
        pin31.write(1)
        pin32.write(1)
        pin33.write(1)
        pin34.write(1)
        pin35.write(1)
        pin36.write(1)
        pin37.write(1)
        pin38.write(1)
        pin39.write(1)
        pin40.write(1)
        pin41.write(1)
        pin42.write(1)
        pin43.write(1)
        pin44.write(1)
        pin45.write(1)
        pin46.write(1)
        pin47.write(1)
        pin48.write(1)
        pin49.write(1)
        pin50.write(1)
        pin51.write(1)
        pin52.write(1)
        pin2.write(1)
    except:
        print("pin write failed, run pin set program or shut down grid system")
        
    root.destroy()
    board.exit() #disengage Arduino Board)

#set exit button
exitButton = Button(root, text = "Exit", command = exitButton)
exitButton.grid(column = 6, row = 18)

#temp label
tempLabel = Label(root, text = "Temp")
tempLabel.grid(column = 6, row = 0)


#functions to enable/disable manual relay control
def disable_check():
    if varman.get():
        a.config(state=NORMAL)
        b.config(state=NORMAL)
        c.config(state=NORMAL)
        d.config(state=NORMAL)
        e.config(state=NORMAL)
        f.config(state=NORMAL)
        g.config(state=NORMAL)
        h.config(state=NORMAL)
        i.config(state=NORMAL)
        j.config(state=NORMAL)
        k.config(state=NORMAL)
        L.config(state=NORMAL)
        m.config(state=NORMAL)
        n.config(state=NORMAL)
        o.config(state=NORMAL)
        p.config(state=NORMAL)
        q.config(state=NORMAL)
       # r.config(state=NORMAL)
        #s.config(state=NORMAL)
        t.config(state=NORMAL)
        u.config(state=NORMAL)
        v.config(state=NORMAL)
        w.config(state=NORMAL)
        x.config(state=NORMAL)
        y.config(state=NORMAL)
        z.config(state=NORMAL)
        aa.config(state=NORMAL)
        bb.config(state=NORMAL)
        cc.config(state=NORMAL)
        dd.config(state=NORMAL)
        ee.config(state=NORMAL)
        ff.config(state=NORMAL)
        gg.config(state=NORMAL)
        #hh.config(state=NORMAL)
       # ii.config(state=NORMAL)
        jj.config(state=NORMAL)
        kk.config(state=NORMAL)
        ll.config(state=NORMAL)
        mm.config(state=NORMAL)
       # nn.config(state=NORMAL)
       # oo.config(state=NORMAL)
       # pp.config(state=NORMAL)
        qq.config(state=NORMAL)
    else:
        a.config(state=DISABLED)
        b.config(state=DISABLED)
        c.config(state=NORMAL)
        d.config(state=DISABLED)
        e.config(state=DISABLED)
        f.config(state=NORMAL)
        g.config(state=DISABLED)
        h.config(state=DISABLED)
        i.config(state=NORMAL)
        j.config(state=DISABLED)
        k.config(state=DISABLED)
        L.config(state=NORMAL)
        m.config(state=DISABLED)
        n.config(state=DISABLED)
        o.config(state=NORMAL)
        p.config(state=DISABLED)
        q.config(state=DISABLED)
       # r.config(state=NORMAL)
        #s.config(state=NORMAL)
        t.config(state=NORMAL)
        u.config(state=DISABLED)
        v.config(state=DISABLED)
        w.config(state=NORMAL)
        x.config(state=DISABLED)
        y.config(state=NORMAL)
        z.config(state=DISABLED)
        aa.config(state=DISABLED)
        bb.config(state=NORMAL)
        cc.config(state=NORMAL)
        dd.config(state=NORMAL)
        ee.config(state=NORMAL)
        ff.config(state=NORMAL)
        gg.config(state=NORMAL)
        #hh.config(state=DISABLED)
        #ii.config(state=DISABLED)
        jj.config(state=NORMAL)
        kk.config(state=DISABLED)
        ll.config(state=NORMAL)
        mm.config(state=DISABLED)
       # nn.config(state=DISABLED)
       # oo.config(state=DISABLED)
       # pp.config(state=DISABLED)
        qq.config(state=NORMAL)

import random
random.seed()
#manual = Checkbutton(root, text = "manual relays", variable = varman, command = disable_check)
#varman.set(0) #initially unchecked
#manual.grid(column = 6, row =1 )

nminus1 = Checkbutton(root, text = "N-1 Correction", variable = nminus1_state)
nminus1.grid(column = 6, row = 2)

def full_start():
    try:
        #turn off all checkboxes
        #manual.deselect
        nminus1.deselect()
        a.deselect()
        b.deselect()
        c.deselect()
        d.deselect()
        e.deselect()
        f.deselect()
        g.deselect()
        h.deselect()
        i.deselect()
        j.deselect()
        k.deselect()
        L.deselect()
        m.deselect()
        n.deselect()
        o.deselect()
        p.deselect()
        q.deselect()
        t.deselect()
        u.deselect()
        v.deselect()
        w.deselect()
        x.deselect()
        y.deselect()
        z.deselect()
        aa.deselect()
        bb.deselect()
        cc.deselect()
        dd.deselect()
        ee.deselect()
        ff.deselect()
        gg.deselect()
        ii.deselect()
        jj.deselect()
        kk.deselect()
        ll.deselect()
        mm.deselect()
        qq.deselect()
        #turn off all relays
        pin53.write(0)
        pin3.write(1)
        pin4.write(1)
        pin5.write(1)
        pin6.write(1)
        pin7.write(1)
        pin8.write(1)
        pin9.write(1)
        pin10.write(1)
        pin11.write(1)
        pin12.write(1)
        pin13.write(1)
        pin22.write(1)
        pin23.write(1)
        pin24.write(1)
        pin25.write(1)
        pin26.write(1)
        pin27.write(1)
        pin28.write(1)
        pin29.write(1)
        pin30.write(1)
        pin31.write(1)
        pin32.write(1)
        pin33.write(1)
        pin34.write(1)
        pin35.write(1)
        pin36.write(1)
        pin37.write(1)
        pin38.write(1)
        pin39.write(1)
        pin40.write(1)
        pin41.write(1)
        pin42.write(1)
        pin43.write(1)
        pin44.write(1)
        pin45.write(1)
        pin46.write(1)
        pin47.write(1)
        pin48.write(1)
        pin49.write(1)
        pin50.write(1)
        pin51.write(1)
        pin52.write(1)
        pin2.write(1)
        #begin sequenced startup
        #residential
        qq.select()
        c.select()
        f.select()
        i.select()
        L.select()
        o.select()
        t.select()
        w.select()
        y.select()
        jj.select()
        ll.select()
        set_relay43()
        set_relay3()
        set_relay6()
        set_relay9()
        set_relay12()
        set_relay15()
        set_relay20()
        set_relay23()
        set_relay25()
        set_relay36()
        set_relay38()
        #commercial
        bb.select()
        cc.select()
        dd.select()
        ee.select()
        ff.select()
        gg.select()
        set_relay28()
        time.sleep(0.2)
        set_relay29()
        time.sleep(0.2)
        set_relay30()
        time.sleep(0.2)
        set_relay31()
        time.sleep(0.2)
        set_relay32()
        time.sleep(0.2)
        set_relay33()
        time.sleep(0.2)
        #industrial
        ii.select()
        set_relay35()
        
        
    except:
        print("Normal operating condition set failed")

#set NOC button
NOCButton = Button(root, text = "Full Start", command = full_start)
NOCButton.grid(column = 6, row = 16)

#function to redraw canvas on view mode selection
def setViewMode():
    if viewMode.get() == 1:
        #standard city view
        canvas.create_image(0, 0, image = tkimage, anchor = NW)
        #w1.place(x=30, y=30)
        #w2.place(x=90, y=30)
    else:
        #inverted city viewmode
        canvas.create_image(0, 0, image = tkimage2, anchor = NW)
        #w1.place(x=30, y=30)
        #w2.place(x=90, y=30)

def nMinus1():
    global CORRECTION_THRESHOLD
    global I_res1
    global I_res2
    global I_res3
    global I_res4
    global I_res5
    global I_res6
    global I_res7
    global I_res8
    global I_res9
    global I_res10
    global I_res11
    #print("I_res1: "+"{0:.4f}".format(I_res1))
    if (I_res1 < CORRECTION_THRESHOLD):
        #if (var6.get()):
        #    d.deselect()
        #    set_relay4()
        #    time.sleep(0.5)
        #    g.select()
        #    set_relay7();
        #else:
        qq.deselect()
        set_relay40()
        #    g.deselect()
        #    set_relay7()
        time.sleep(0.5)
        d.select()
        set_relay4()
    #print("I_res2: "+"{0:.4f}".format(I_res2))
    if (I_res2 < CORRECTION_THRESHOLD):
        #if (var3.get()):
        #    a.deselect()
        #    set_relay1()
        #    time.sleep(0.5)
        #    j.select()
        #    set_relay10()
        #else:
        c.deselect()
        set_relay3()
        #    j.deselect()
        #    set_relay10()
        time.sleep(0.5)
        a.select()
        set_relay1()        
    #print("I_res3: "+"{0:.4f}".format(I_res3))
    if (I_res3 < CORRECTION_THRESHOLD):
        #if (var23.get()):
        #    m.deselect()
        #    set_relay13()
        #    time.sleep(0.5)
        #    p.select()
        #    set_relay16()
        #else:
        f.deselect()
        set_relay6()
        #    p.deselect()
        #    set_relay16()
        time.sleep(0.5)
        m.select()
        set_relay13()
    #print("I_res4: "+"{0:.4f}".format(I_res4))
    if (I_res4 < CORRECTION_THRESHOLD):
        #if (var31.get()):
        #    u.deselect()
        #    set_relay21()
        #    time.sleep(0.5)
        #    x.select()
        #    set_relay24()
        #else:
        i.deselect()
        set_relay9()
        #    x.deselect()
        #    set_relay24()
        time.sleep(0.5)
        u.select()
        set_relay21()
    #print("I_res5: "+"{0:.4f}".format(I_res5))
    if (I_res5 < CORRECTION_THRESHOLD):
        #if (var36.get()):
        #    z.deselect()
        #    set_relay26()
        #    time.sleep(0.5)
        #    kk.select()
        #    set_relay37()
        #else:
        L.deselect()
        set_relay12()
        #    kk.deselect()
        #    set_relay37()
        time.sleep(0.5)
        z.select()
        set_relay26()
    #print("I_res6: "+"{0:.4f}".format(I_res6))
    if (I_res6 < CORRECTION_THRESHOLD):
        o.deselect()
        set_relay15()
        time.sleep(0.5)
        mm.select()
        set_relay39()
    #print("I_res7: "+"{0:.4f}".format(I_res7))
    if (I_res7 < CORRECTION_THRESHOLD):
        t.deselect()
        set_relay20()
        print "res 7 before delay"
        time.sleep(0.5)
        aa.select()
        set_relay27()
    #print("I_res8: "+"{0:.4f}".format(I_res8))
    if (I_res8 < CORRECTION_THRESHOLD):
        #if (var4.get()):
        #    b.deselect()
        #    set_relay2()
        #    time.sleep(0.5)
        #    e.select()
        #    set_relay5()
        #else:
        w.deselect()
        set_relay23()
        #    e.deselect()
        #    set_relay5()
        time.sleep(0.5)
        b.select()
        set_relay2()
    #print("I_res9: "+"{0:.4f}".format(I_res9))
    if (I_res9 < CORRECTION_THRESHOLD):
        #if (var10.get()):
        #    h.deselect()
        #    set_relay8()
        #    time.sleep(0.5)
        #    k.select()
        #    set_relay11()
        #else:
        y.deselect()
        set_relay25()
        #    k.deselect()
        #    set_relay11()
        time.sleep(0.5)
        h.select()
        set_relay8()
    #print("I_res10: "+"{0:.4f}".format(I_res10))
    if (I_res10 < CORRECTION_THRESHOLD):
        #if (var24.get()):
        #    n.deselect()
        #    set_relay14()
        #    time.sleep(0.5)
        #    v.select()
        #    set_relay22()
        #else:
        jj.deselect()
        set_relay36()
        #    v.deselect()
        #    set_relay22()
        time.sleep(0.5)
        n.select()
        set_relay14()
    #print("I_res11: "+"{0:.4f}".format(I_res11))
    if (I_res11 < CORRECTION_THRESHOLD):
        ll.deselect()
        set_relay38()
        time.sleep(0.5)
        q.select()
        set_relay17()
    root.after(50, updateMap)

#define temperature update function
def updateTemp():
    try:
        data = bus.read_i2c_block_data(0x48, 0)
        msb = data[0]
        lsb = data[1]
        #print = ((((msb<<8) | lsb)>>4) * 0.0625)
        tempLabel['text']="Temp: "+(str)((((msb<<8) | lsb)>>4) * 0.0625)
    except IOError:
        #print("temp read failed")
        msb = 0
        lsb = 0
        #print = ((((msb<<8) | lsb)>>4) * 0.0625)
        tempLabel['text']="Temp: "+(str)((((msb<<8) | lsb)>>4) * 0.0625)
    #tempLabel.text = "Changed"
    root.after(10, request_reading_1)

def request_reading_1():
        #get block of 8 bytes from microcontroller
        #use global variables
        global r1_0
        global r1_1
        global r1_2
        global r1_3
        global r1_4
        global r1_5
        global r1_6
        global r1_7
        global MGVolt

        global V1_res1
        global V1_res2
        global V1_res3
        global V2_res1
        global V2_res2
        global V2_res3
        global I_res1
        global I_res2
        global I_res3
        global respow1
        global respow2
        global respow3
        global indpow1
        global V1_ind1
        global V2_ind1
        global I_ind1
        #read
        try:
            data = bus.read_i2c_block_data(0x08, 0, 8)
            r1_0=data[0]
            r1_1=data[1]
            r1_2=data[2]
            r1_3=data[3]
            r1_4=data[4]
            r1_5=data[5]
            r1_6=data[6]
            r1_7=data[7]
            #com1['text'] = "{0:.2f}".format(((r0*5.0*(3.7/255))+1.5)*((((r0*5.0*(3.7/255)))-((r1*5.0*(3.7/255))))/20))+"VA"
            #com2['text'] = "{0:.2f}".format(((r2*5.0*(3.7/255))+1.5)*((((r2*5.0*(3.7/255)))-((r3*5.0*(3.7/255))))/20))+"VA"
            #com3['text'] = (str)((r2*5.0*(3.7/255)))+"VA"
            #com4['text'] = (str)((r3*5.0*(3.7/255)))+"VA"
        except:
                #print("Reading failed 1")
                dummy = 1
        #math
        try:
            #measurement ground offset
            
            #MGVolt = r1_6
            r1_0=r1_0-MGVolt
            r1_1=r1_1-MGVolt
            r1_2=r1_2-MGVolt
            r1_3=r1_3-MGVolt
            r1_4=r1_4-MGVolt
            r1_5=r1_5-MGVolt
            r1_6=r1_6-MGVolt
            r1_7=r1_7-MGVolt
            #voltage
            V1_res1=r1_0*5.0*(3.7/255)
            V2_res1=r1_1*5.0*(3.7/255)
            V1_res2=r1_2*5.0*(3.7/255)
            V2_res2=r1_3*5.0*(3.7/255)
            V1_res3=r1_4*5.0*(3.7/255)
            V2_res3=r1_5*5.0*(3.7/255)
            #current
            I_res1 = (V1_res1 - V2_res1)/20
            I_res2 = (V1_res2 - V2_res2)/20
            I_res3 = (V1_res3 - V2_res3)/20
            #power
            respow1 = (V1_res1+1.5)*I_res1
            respow2 = (V1_res2+1.5)*I_res2
            respow3 = (V1_res3+1.5)*I_res3
            V1_ind1=r1_7*5.0*(15/255)
            V2_ind1=r1_6*5.0*(13.9/255)
            #current
            I_ind1 = (V1_ind1 - V2_ind1)/11
            #power
            indpow1 = (V1_ind1)*I_ind1
        except:
            #print("math failed 1")
            dummy = 1
        #queue next function
        root.after(50, request_reading_2)


def request_reading_2():
        #get block of 8 bytes from microcontroller
        #use global variables
        global r2_0
        global r2_1
        global r2_2
        global r2_3
        global r2_4
        global r2_5
        global r2_6
        global r2_7
        global r6_0
        global r6_1
        global MGVolt
        global V1_res4
        global V2_res4
        global I_res4
        global respow4
        global V1_res5
        global V2_res5
        global I_res5
        global respow5
        global V1_res6
        global V2_res6
        global I_res6
        global respow6
        global V1_res7
        global V2_res7
        global I_res7
        global respow7
        try:
            data = bus.read_i2c_block_data(0x09, 0, 8)
            r2_0=data[0]
            r2_1=data[1]
            r2_2=data[2]
            r2_3=data[3]
            r2_4=data[4]
            r2_5=data[5]
            r2_6=data[6]
            r2_7=data[7]
            
        except:
                #print("Reading failed 2")
                dummy = 1
        #math
        try:
            #measurement ground offset
            #r2_0=r2_0-MGVolt
            #r2_1=r2_1-MGVolt
            #r2_2=r2_2-MGVolt
            #r2_3=r2_3-MGVolt
            #r2_4=r2_4-MGVolt
            #r2_5=r2_5-MGVolt
            #r2_6=r2_6-MGVolt
            #r2_7=r2_7-MGVolt
            #voltage
            V1_res4=r2_0*5.0*(3.7/255)
            V2_res4=r2_1*5.0*(3.7/255)
            V1_res5=r2_2*5.0*(3.7/255)
            V2_res5=r2_3*5.0*(3.7/255)
            V1_res6=r2_4*5.0*(3.7/255)
            V2_res6=r2_5*5.0*(3.7/255)
            #V1_res7=r2_6*5.0*(3.7/255)
            #V2_res7=r2_7*5.0*(3.7/255)
            V1_res7=r6_0*5.0*(3.7/255)
            V2_res7=r6_1*5.0*(3.7/255)
            #current
            I_res4 = (V1_res4 - V2_res4)/20
            I_res5 = (V1_res5 - V2_res5)/20
            I_res6 = (V1_res6 - V2_res6)/20
            I_res7 = (V1_res7 - V2_res7)/20
            #power
            respow4 = (V1_res4+1.5)*I_res4
            respow5 = (V1_res5+1.5)*I_res5
            respow6 = (V1_res6+1.5)*I_res6
            respow7 = (V1_res7+1.5)*I_res7
        except:
            #print("math failed 2")
            dummy = 1
        #queue next function
        root.after(50, request_reading_3)

def request_reading_3():
        #get block of 8 bytes from microcontroller
        #use global variables
        global r3_0
        global r3_1
        global r3_2
        global r3_3
        global r3_4
        global r3_5
        global r3_6
        global r3_7
        global r6_2
        global r6_3
        global MGVolt
        global V1_res8
        global V2_res8
        global I_res8
        global respow8
        global V1_res9
        global V2_res9
        global I_res9
        global respow9
        global V1_res10
        global V2_res10
        global I_res10
        global respow10
        global V1_res11
        global V2_res11
        global I_res11
        global respow11
        try:
            data = bus.read_i2c_block_data(0x0c, 0, 8)
            r3_0=data[0]
            r3_1=data[1]
            r3_2=data[2]
            r3_3=data[3]
            r3_4=data[4]
            r3_5=data[5]
            r3_6=data[6]
            r3_7=data[7]
            
        except:
                #print("Reading failed 3")
                dummy = 1
        #math
        try:
            #measurement ground offset
            r3_0=r3_0-MGVolt
            r3_1=r3_1-MGVolt
            r3_2=r3_2-MGVolt
            r3_3=r3_3-MGVolt
            r3_4=r3_4-MGVolt
            r3_5=r3_5-MGVolt
            r3_6=r3_6-MGVolt
            r3_7=r3_7-MGVolt
            #voltage
            V1_res8=r3_0*5.0*(3.7/255)
            V2_res8=r3_1*5.0*(3.7/255)
            V1_res9=r3_2*5.0*(3.7/255)
            V2_res9=r3_3*5.0*(3.7/255)
            V1_res10=r3_4*5.0*(3.7/255)
            V2_res10=r3_5*5.0*(3.7/255)
            #V1_res11=r3_6*5.0*(3.7/255)
            #V2_res11=r3_7*5.0*(3.7/255)
            V1_res11=r6_2*5.0*(3.7/255)
            V2_res11=r6_3*5.0*(3.7/255)
            #current
            I_res8 = (V1_res8 - V2_res8)/20
            I_res9 = (V1_res9 - V2_res9)/20
            I_res10 = (V1_res10 - V2_res10)/20
            I_res11 = (V1_res11 - V2_res11)/20
            #power
            respow8 = (V1_res8+1.5)*I_res8
            respow9 = (V1_res9+1.5)*I_res9
            respow10 = (V1_res10+1.5)*I_res10
            respow11 = (V1_res11+1.5)*I_res11
        except:
            #print("math failed 3")
            dummy = 1
        #queue next function
        root.after(50, request_reading_4)


def request_reading_4():
        #get block of 8 bytes from microcontroller
        #use global variables
        global r4_0
        global r4_1
        global r4_2
        global r4_3
        global r4_4
        global r4_5
        global r4_6
        global r4_7
        global MGVolt
        global V1_com1
        global V2_com1
        global I_com1
        global compow1
        global V1_com2
        global V2_com2
        global I_com2
        global compow2
        global V1_com3
        global V2_com3
        global I_com3
        global compow3
        global V1_com4
        global V2_com4
        global I_com4
        global compow4
        global PF_com1
        global PF_com2
        global PF_com3
        global PF_com4
        global V1list_com1
        global V1list_com2
        global V1list_com3
        global V1list_com4
        global V2list_com1
        global V2list_com2
        global V2list_com3
        global V2list_com4
        try:
            data = bus.read_i2c_block_data(0x0d, 0, 8)
            r4_0=data[0]
            r4_1=data[1]
            r4_2=data[2]
            r4_3=data[3]
            r4_4=data[4]
            r4_5=data[5]
            r4_6=data[6]
            r4_7=data[7]
            
        except:
                #print("Reading failed 4")
                dummy = 1
        #math
        try:
            #measurement ground offset
            if(var38.get()):
                r4_0 = r4_0 + 35
                r4_1 = r4_1 + 2
                PF_com1 = random.uniform(.74,1.03)
            else:
                PF_com1 = random.uniform(0.98, 1.01)
            #    r4_1=r4_1-MGVolt
            if(var39.get()):
                r4_2 = r4_2 + 31
                r4_3 = r4_3 + 1
                PF_com2 = random.uniform(.74,0.91)
            else:
                PF_com2 = random.uniform(0.98, 1.02)
            #    r4_3=r4_3-MGVolt
            if(var40.get()):
                r4_4 = r4_4 + 19
                r4_5 = r4_5 + 1
                PF_com3 = random.uniform(.74,0.92)
            else:
                PF_com3 = random.uniform(0.98, 1.02)
            #    r4_5=r4_5-MGVolt
            if(var41.get()):
                r4_6 = r4_6 + 17
                r4_7 = r4_7 + 1
                PF_com4 = random.uniform(.74,0.88)
            else:
                PF_com4 = random.uniform(0.98, 1.02)
            #    r4_7=r4_7-MGVolt
            #voltage
            #V1_com1=r4_0*5.0*(5.7/255)
            try:
                del V1list_com1[-len(V1list_com1)]
                V1list_com1.append(r4_0*5.0*(5.7/255))
                V1_com1=(float(sum(V1list_com1))/(float(len(V1list_com1))))
            except:
                #print("math failed V1list_com1")
                dummy = 1
            #print(str(V1_com1))
            #V2_com1=r4_1*5.0*(5.7/255)
            del V2list_com1[-len(V2list_com1)]
            V2list_com1.append(r4_1*5.0*(5.7/255))
            V2_com1=(sum(V2list_com1)/float(len(V2list_com1)))
            #print(str(V2_com1))
            #V1_com2=r4_2*5.0*(5.7/255)
            del V1list_com2[-len(V1list_com2)]
            V1list_com2.append(r4_2*5.0*(5.7/255))
            V1_com2=(sum(V1list_com2)/float(len(V1list_com2)))    
            #V2_com2=r4_3*5.0*(5.7/255)
            del V2list_com2[-len(V2list_com2)]
            V2list_com2.append(r4_3*5.0*(5.7/255))
            V2_com2=(sum(V2list_com2)/float(len(V2list_com2)))    
            #V1_com3=r4_4*5.0*(5.7/255)
            del V1list_com3[-len(V1list_com3)]
            V1list_com3.append(r4_4*5.0*(5.7/255))
            V1_com3=(sum(V1list_com3)/float(len(V1list_com3)))    
            #V2_com3=r4_5*5.0*(5.7/255)
            del V2list_com3[-len(V2list_com3)]
            V2list_com3.append(r4_5*5.0*(5.7/255))
            V2_com3=(sum(V2list_com3)/float(len(V2list_com3)))    
            #V1_com4=r4_6*5.0*(5.7/255)
            del V1list_com4[-len(V1list_com4)]
            V1list_com4.append(r4_6*5.0*(5.7/255))
            V1_com4=(sum(V1list_com4)/float(len(V1list_com4)))    
            #V2_com4=r4_7*5.0*(5.7/255)
            del V2list_com4[-len(V2list_com4)]
            V2list_com4.append(r4_7*5.0*(5.7/255))
            V2_com4=(sum(V2list_com4)/float(len(V2list_com4)))
            #current
            I_com1 = (V1_com1 - V2_com1)/15
            #print("I_com1:"+str(I_com1))
            I_com2 = (V1_com2 - V2_com2)/15
            I_com3 = (V1_com3 - V2_com3)/15
            I_com4 = (V1_com4 - V2_com4)/15
            #power
            compow1 = (V1_com1+1.5)*I_com1
            compow2 = (V1_com2+1.5)*I_com2
            compow3 = (V1_com3+1.5)*I_com3
            compow4 = (V1_com4+1.5)*I_com4
            #print("I_com1:"+I_com1)
            #print("compow1:"+compow1)
            #PF
            PF_com1_temp = ((V1_com1**2) - (V2_com1**2) - ((V1_com1-V2_com1)**2))/(2*V2_com1*(V1_com1-V2_com1))
            PF_com2_temp = ((V1_com2**2) - (V2_com2**2) - ((V1_com1-V2_com2)**2))/(2*V2_com2*(V1_com2-V2_com2))
            PF_com3_temp = ((V1_com3**2) - (V2_com3**2) - ((V1_com1-V2_com3)**2))/(2*V2_com3*(V1_com3-V2_com3))
            PF_com4_temp = ((V1_com4**2) - (V2_com4**2) - ((V1_com1-V2_com4)**2))/(2*V2_com4*(V1_com4-V2_com4))
            if ((PF_com1_temp<=1)&(PF_com1_temp>=0)):
                PF_com1=PF_com1_temp
            if ((PF_com2_temp<=1)&(PF_com2_temp>=0)):
                PF_com2=PF_com2_temp
            if ((PF_com3_temp<=1)&(PF_com3_temp>=0)):
                PF_com3=PF_com3_temp
            if ((PF_com4_temp<=1)&(PF_com4_temp>=0)):
                PF_com4=PF_com4_temp
        except:
            #print("math failed 4")
            dummy = 1
        #queue next function
        root.after(50, request_reading_5)

def request_reading_5():
        #get block of 8 bytes from microcontroller
    #use global variables
        global r5_0
        global r5_1
        global r5_2
        global r5_3
        global r5_4
        global r5_5
        global r5_6
        global r5_7
        global MGVolt
        global V1_com5
        global V2_com5
        global I_com5
        global compow5
        global V1_com6
        global V2_com6
        global I_com5
        global compow6
        global PF_com5
        global PF_com6
        global V1list_com5
        global V1list_com6
        global V2list_com5
        global V2list_com6
       
        try:
            data = bus.read_i2c_block_data(0x0e, 0, 8)
            r5_0=data[0]
            r5_1=data[1]
            r5_2=data[2]
            r5_3=data[3]
            r5_4=data[4]
            r5_5=data[5]
            r5_6=data[6]
            r5_7=data[7]
            MGVolt=r5_4
            
        except:
                #print("Reading failed 5")
                dummy = 1
        #math
        try:
            #measurement ground offset
            if(var42.get()):
                r5_0 = data[0]+61
                r5_1 = r5_1 + 1
                PF_com5 = random.uniform(0.78, 0.9)
            else:
                PF_com5 = random.uniform(0.98, 1.02)
            #    r5_0=r5_0-MGVolt
            #    r5_1=r5_1-MGVolt
            if(var43.get()):
                r5_2=data[2]+33
                r5_3 = r5_3 + 1
                PF_com6 = random.uniform(0.78, 0.9)
            else:
                PF_com6 = random.uniform(0.98, 1.02)
            #    r5_3=r5_3-MGVolt
            #r5_4=r5_4-MGVolt
            #r5_5=r5_5-MGVolt
            #r5_6=r5_6-MGVolt
            #r5_7=r5_7-MGVolt
            #voltage
            #V1_com5=r5_0*5.0*(5.7/255)
            del V1list_com5[-len(V1list_com5)]
            V1list_com5.append(r5_0*5.0*(5.7/255))
            V1_com5=(sum(V1list_com5)/float(len(V1list_com5)))
            #V2_com5=r5_1*5.0*(5.7/255)
            del V2list_com5[-len(V2list_com5)]
            V2list_com5.append(r5_1*5.0*(5.7/255))
            V2_com5=(sum(V2list_com5)/float(len(V2list_com5)))
            #V1_com6=r5_2*5.0*(5.7/255)
            del V1list_com6[-len(V1list_com6)]
            V1list_com6.append(r5_2*5.0*(5.7/255))
            V1_com6=(sum(V1list_com6)/float(len(V1list_com6)))
            #V2_com6=r5_3*5.0*(5.7/255)
            del V2list_com6[-len(V2list_com6)]
            V2list_com6.append(r5_3*5.0*(5.7/255))
            V2_com6=(sum(V2list_com6)/float(len(V2list_com6)))
            #current
            I_com5 = (V1_com5 - V2_com5)/15
            I_com6 = (V1_com6 - V2_com6)/15
            #power
            compow5 = abs((V1_com5+1.5)*I_com5)
            compow6 = (V1_com6+1.5)*I_com6
            PF_com5_temp = ((V1_com5**2) - (V2_com5**2) - ((V1_com5-V2_com5)**2))/(2*V2_com5*(V1_com5-V2_com5))
            PF_com6_temp = ((V1_com6**2) - (V2_com6**2) - ((V1_com6-V2_com6)**2))/(2*V2_com6*(V1_com6-V2_com6))
            if ((PF_com6_temp<=1)&(PF_com6_temp>=0)):
                PF_com6=PF_com6_temp
            if ((PF_com5_temp<=1)&(PF_com5_temp>=0)):
                PF_com5=PF_com5_temp
        except:
            #print("math failed 5")
            dummy = 0
        #queue next function
        root.after(50, request_reading_6)


def request_reading_6():
        #get block of 8 bytes from microcontroller
    #use global variables
        global r6_0
        global r6_1
        global r6_2
        global r6_3
        global r6_4
        global r6_5
        global r6_6
        global r6_7
        global V1_ind1
        global V2_ind1
        global V2_ind2
        global V1_ind2
        global I_ind1
        global I_ind2
        global indpow1
        global indpow2
        global MGVolt
        try:
            data = bus.read_i2c_block_data(0x0f, 0, 8)
            r6_0=data[0]
            r6_1=data[1]
            r6_2=data[2]
            r6_3=data[3]
            r6_4=data[4]
            r6_5=data[5]
            r6_6=data[6]
            r6_7=data[7]
            
        except:
                #print("Reading failed 6")
                dummy = 1
        #math
        try:
            #measurement ground offset
            r6_0=r6_0-MGVolt
            r6_1=r6_1-MGVolt
            r6_2=r6_2-MGVolt
            r6_3=r6_3-MGVolt
            r6_4=r6_4-MGVolt
            r6_5=r6_5-MGVolt
            r6_6=r6_6-MGVolt
            r6_7=r6_7-MGVolt
            #voltage
            #V1_ind1=r6_0*5.0*(5.7/255)
            #V2_ind1=r6_1*5.0*(5.7/255)
            #V1_ind2=r6_2*5.0*(5.7/255)
            #V2_ind2=r6_3*5.0*(5.7/255)
            #current
            #I_ind1 = (V1_ind1 - V2_ind1)/11
            #I_ind2 = (V1_ind2 - V2_ind2)/11
            #power
            #indpow1 = (V1_ind1+1.5)*I_ind1
            #indpow2 = (V1_ind2+1.5)*I_ind2
        except:
            #print("math failed 6")
            dummy = 1
        #queue next function
        if(nminus1_state.get()):
            root.after(50, nMinus1)
        else:
            root.after(50, readSerial)
            #ADDITION
            
def readSerial():
    global compow1
    global compow2
    global compow3
    global compow4
    global compow5
    global compow6
    global respow1
    global respow2
    global respow3
    global respow4
    global respow5
    global respow6
    global respow7
    global respow8
    global respow9
    global respow10
    global respow11
    global indpow1
    
    rs1 = "{0:.2f}".format(abs(respow1))
    rs2 = "{0:.2f}".format(abs(respow2))
    rs3 = "{0:.2f}".format(abs(respow3))
    rs4 = "{0:.2f}".format(abs(respow4))
    rs5 = "{0:.2f}".format(abs(respow5))
    rs6 = "{0:.2f}".format(abs(respow6))
    rs7 = "{0:.2f}".format(abs(respow7))
    rs8 = "{0:.2f}".format(abs(respow8))
    rs9 = "{0:.2f}".format(abs(respow9))
    rs10 = "{0:.2f}".format(abs(respow10))
    rs11 = "{0:.2f}".format(abs(respow11))
    cs1 = "{0:.2f}".format(abs(compow1))
    cs2 = "{0:.2f}".format(abs(compow2))
    cs3 = "{0:.2f}".format(abs(compow3))
    cs4 = "{0:.2f}".format(abs(compow4))
    cs5 = "{0:.2f}".format(abs(compow5))
    cs6 = "{0:.2f}".format(abs(compow6))
    is1 = "{0:.2f}".format(abs(indpow1))
    
    while True: 
        c = ser.read()
        
        if len(c) == 0:
            break
            
        global serBuffer
        
        if c =='\r':
            c = ''
        if c == '\n':
            serBuffer+="\n"
            if serBuffer == 'getDATA\n':
                ser.write(("!"+rs1+"+"+rs2+"+"+rs3+"+"+rs4+"+"+rs5+"+"+rs6+"+"+rs7+"+"+rs8+"+"+rs9+"+"+rs10+"+"+rs11+"+"+cs1+"+"+cs2+"+"+cs3+"+"+cs4+"+"+cs5+"+"+cs6+"+"+is1+"\r\n").encode())
            recDataToggle(serBuffer)
            serBuffer=""
        else:
            serBuffer += c 
            
    root.after(50,updateMap)

def updateMap():
    global compow1
    global compow2
    global compow3
    global compow4
    global compow5
    global compow6
    global respow1
    global respow2
    global respow3
    global respow4
    global respow5
    global respow6
    global respow7
    global respow8
    global respow9
    global respow10
    global respow11
    global indpow1
    global indpow2
    global PF_com1
    global PF_com2
    global PF_com3
    global PF_com4
    global PF_com5
    global PF_com6
    global totalP1
    global totalP2
    global totalP3
    global totalS
    
    #commercial
    com1['text'] = "{0:.2f}".format(compow1)+"VA\nPF: "+"{0:.2f}".format(PF_com1)
    com2['text'] = "{0:.2f}".format(compow2)+"VA\nPF: "+"{0:.2f}".format(PF_com2)
    com3['text'] = "{0:.2f}".format(compow3)+"VA\nPF: "+"{0:.2f}".format(PF_com3)
    com4['text'] = "{0:.2f}".format(compow4)+"VA\nPF: "+"{0:.2f}".format(PF_com4)
    com5['text'] = "{0:.2f}".format(compow5)+"VA\nPF: "+"{0:.2f}".format(PF_com5)
    com6['text'] = "{0:.2f}".format(compow6)+"VA\nPF: "+"{0:.2f}".format(PF_com6)
    #residential
    res1['text'] = "{0:.2f}".format(respow1)+"VA"
    res2['text'] = "{0:.2f}".format(respow2)+"VA"
    res3['text'] = "{0:.2f}".format(respow3)+"VA"
    res4['text'] = "{0:.2f}".format(respow4)+"VA"
    res5['text'] = "{0:.2f}".format(respow5)+"VA"
    res6['text'] = "{0:.2f}".format(respow6)+"VA"
    res7['text'] = "{0:.2f}".format(respow7)+"VA"
    res8['text'] = "{0:.2f}".format(respow8)+"VA"
    res9['text'] = "{0:.2f}".format(respow9)+"VA"
    res10['text'] = "{0:.2f}".format(respow10)+"VA"
    res11['text'] = "{0:.2f}".format(respow11)+"VA"
    #industrial
    ind1['text'] = "{0:.2f}".format(indpow1/3)+"VA"
    ind2['text'] = "{0:.2f}".format(indpow1/3)+"VA"
    ind3['text'] = "{0:.2f}".format(indpow1/3)+"VA"
    totalP1 = compow1 + compow2 + compow3 + compow4 + compow5 + compow6 + respow1 + respow2
    totalP2 = totalP1 + respow3 + respow4 + respow5 + respow6 + respow7 + respow8 + respow9
    totalP3 = totalP2 + respow10 + respow11 + indpow1
    totalS += 1
    time.sleep(1)
    pgrid.append(totalP3)
    ptime.append(totalS)
    root.after(10, updateTemp)                       

#view mode selection box
Radiobutton(root, indicatoron = 0, text="City View CAD", variable = viewMode,
            value=1, command = setViewMode).grid(column = 6, row = 3)
Radiobutton(root, indicatoron = 0, text="City View Photo", variable = viewMode,
            value=2, command = setViewMode).grid(column = 6, row = 4)





root.after(5000, updateTemp())

''' Bluetooth initialization 
s = BluetoothSocket( RFCOMM )
s.bind(("",PORT_ANY))
s.listen(1)
port = s.getsockname()[1]
uuid = "a13514fc-02fa-47e9-aa8e-ad33919815d6"
advertise_services( s,"SmartGridServer", 
                    service_id = uuid,
                    service_classes = [uuid, SERIAL_PORT_CLASS],
                    profile = [SERIAL_PORT_PROFILE],
                    )
                    
client_sock, client_info = s.accept() 
'''

def recDataToggle(data):
    if data == 'res1_tog\n':
        if var53.get() == True:
            qq.deselect()
        else:
            qq.select()
        set_relay43()
    elif data == 'res2_tog\n':
        if var5.get() == True:
            c.deselect()
        else:
            c.select()
        set_relay3()
    elif data == 'res3_tog\n':
        if var8.get() == True:
            f.deselect()
        else:
            f.select()
        set_relay6()
    elif data == 'res4_tog\n':
        if var11.get() == True:
            i.deselect()
        else:
            i.select()
        set_relay9()
    elif data == 'res5_tog\n':
        if var22.get() == True:
            L.deselect()
        else:
            L.select()
        set_relay12()
    elif data == 'res6_tog\n':
        if var25.get() == True:
            o.deselect()
        else:
            o.select()
        set_relay15()
    elif data == 'res7_tog\n':
        if var30.get() == True:
            t.deselect()
        else:
            t.select()
        set_relay20()
    elif data == 'res8_tog\n':
        if var33.get() == True:
            w.deselect()
        else:
            w.select()
        set_relay23()
    elif data == 'res9_tog\n':
        if var35.get() == True:
            y.deselect()
        else:
            y.select()
        set_relay25()
    elif data == 'res10_tog\n':
        if var46.get() == True:
            jj.deselect()
        else:
            jj.select()
        set_relay36()
    elif data == 'res11_tog\n':
        if var48.get() == True:
            ll.deselect()
        else:
            ll.select()
        set_relay38()
    elif data == 'com1_tog\n':
        if var38.get() == True:
            bb.deselect()
        else:
            bb.select()
        set_relay28()
    elif data == 'com2_tog\n':
        if var39.get() == True:
            cc.deselect()
        else:
            cc.select()
        set_relay29()
    elif data == 'com3_tog\n':
        if var40.get() == True:
            dd.deselect()
        else:
            dd.select()
        set_relay30()
    elif data == 'com4_tog\n':
        if var41.get() == True:
            ee.deselect()
        else:
            ee.select()
        set_relay31()
    elif data == 'com5_tog\n':
        if var42.get() == True:
            ff.deselect()
        else:
            ff.select()
        set_relay32()
    elif data == 'com6_tog\n':
        if var43.get() == True:
            gg.deselect()
        else:
            gg.select()
        set_relay33()
    elif data == 'ind1_tog\n':
        if var45.get() == True:
            ii.deselect()
        else:
            ii.select()
        set_relay35()
    
        
    else:
        print("error with input")

'''data = 0
data = s.recv(1024)
recDataToggle(data)
'''

root.mainloop() #start GUI
