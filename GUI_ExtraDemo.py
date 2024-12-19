from tkinter import * 
from gpiozero import LED
from gpiozero import Servo
from gpiozero.tools import sin_values from signal import pause
from time import sleep import time
from gpiozero import MotionSensor
#For Butons check https://gpiozero.readthedocs.io/en/stable/api_input.html

led1 = LED(19) 
led2 = LED(26)
buzzer = LED(20) 
servo = Servo(18)
pir = MotionSensor(23) 
# CREATE THE WINDOW
root = Tk()
root.title("FINAL PROJECT") 
root.geometry("600x400")
e = Entry(root, width =50, borderwidth = 25)
e.grid(row=0, column=0,columnspan=3,padx=10,pady=10) 
#e.insert(0, "Enter Your Name: ")
activelabel = Label(root, text = "INACTIVE", bg = "gray", fg = "black") 
activelabel.grid(row = 7, column = 2)
def button_click(number):
	# e.delete(0, END) #delete what is in box 
	current = e.get()
	e.delete(0,END)
	e.insert(0, str(current) + str(number)) 

def button_clear():
	e.delete(0,END) 
	f_num = 0
	s_num = 0
	r_num = 0 

def button_call():
	first_number = e.get() 
	global f_num
	f_num = 0
	f_num = int(first_number) 
	e.delete(0,END)
	if f_num == 12345:
		led2.on() 
		servo.max() 
#		sleep(100000)

	else:
		led1.on() 
		buzzer.on() 
#		sleep(1) 
		buzzer.off()

def motiondetect():
	activelabel = Label(root, text = "PLEASE SET YOUR PASSWORD", bg = "gray", fg = "black") 
	activelabel.grid(row = 7, column = 2)

def  motion_function():
	print("Motion Detected") 
	motiondetect()

def no_motion_function(): 
	print("Motion Stopped")
 

#pir.when_motion = motion_function 
#pir.when_no_motion = no_motion_function

button_1 = Button(root, text="1",padx =40,pady = 20, command=lambda:button_click(1)) 
button_2 = Button(root, text="2",padx =40,pady = 20, command=lambda:button_click(2)) 
button_3 = Button(root, text="3",padx =40,pady = 20, command=lambda:button_click(3)) 
button_4 = Button(root, text="4",padx =40,pady = 20, command=lambda: button_click(4)) 
button_5 = Button(root, text="5",padx =40,pady = 20, command=lambda: button_click(5)) 
button_6 = Button(root, text="6",padx =40,pady = 20, command=lambda: button_click(6)) 
button_7 = Button(root, text="7",padx =40,pady = 20, command=lambda: button_click(7)) 
button_8 = Button(root, text="8",padx =40,pady = 20, command=lambda:button_click(8)) 
button_9 = Button(root, text="9",padx =40,pady = 20, command=lambda:button_click(9)) 
button_0 = Button(root, text="0",padx =40,pady = 20, command=lambda:button_click(0)) 
button_Clear = Button(root, text="Clear",padx =30,pady = 20, command=button_clear)
button_Call = Button(root, text="ENTER",padx =40,fg = "white",bg = "blue",pady = 20, command=button_call)
#Put the buttons on the screen 
button_1.grid(row=3, column=0) 
button_2.grid(row=3, column=1) 
button_3.grid(row=3, column=2) 
button_4.grid(row=2, column=0) 
button_5.grid(row=2, column=1) 
button_6.grid(row=2, column=2) 
button_7.grid(row=1, column=0) 
button_8.grid(row=1, column=1) 
button_9.grid(row=1, column=2) 
button_0.grid(row=4, column=1) 
button_Clear.grid(row=4, column=0)
button_Call.grid(row=4, column=2) 
root.rowconfigure(7, weight = 1) 
root.mainloop()
