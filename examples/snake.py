# Snake game
# 8x8 RGB LED Snake Game
# Autor : Tayfun ULU
# For LCS NeoPixel library used.
# https://github.com/jgarff/rpi_ws281x
# Autor of Library : Jeremy Garff

# Adjusted orientation to suit Wordclock layout - @Boeeerb


import time, curses, thread, random
from neopixel import *

# with tread read data from keyboard
def klavyeden ( threadName,bir):

	global ek_x
	global ek_y
	global timing

	try:
		screen = curses.initscr()
		curses.cbreak()
		curses.echo()
		screen.keypad(True)

		while True :
			char = screen.getch()
			if timing :
				if char == ord('q'):
					break
				elif char == curses.KEY_LEFT:
					if not ek_x==1:
						ek_y=0
						ek_x=-1
						timing=False
				elif char == curses.KEY_RIGHT:
					if not ek_x==-1:
						ek_y=0
						ek_x=1
						timing=False
				elif char == curses.KEY_DOWN:
					if not ek_y==-1:
						ek_y=1
						ek_x=0
						timing=False
				elif char == curses.KEY_UP:
					if not ek_y==1:
						ek_y=-1
						ek_x=0
						timing=False

	finally:
		curses.echo()
		curses.cbreak()
		curses.endwin()

# write a list on led panel
def writer_point (strip,list,color):
	for i in list:
		strip.setPixelColor(i,color)

# clear panel with color defined if not black
def clear_lcd (strip,color=Color(0,0,0)):
    for i in range(strip.numPixels()):
		strip.setPixelColor(i,color)

# game over screen and write scor on screen
def game_over(strip,point):
	# clean screan
	clear_lcd(strip)
	strip.show()
	time.sleep(1)

	# red screen
	clear_lcd(strip,Color(0,100,0))
	strip.show()
	time.sleep(1)

	clear_lcd(strip,Color(76,35,9))
	face=[0,1,2,5,6,7,8,9,14,15,16,23,24,31,32,39,40,42,45,47,48,49,54,55,56,57,58,59,60,61,62,63]
	mot=[18,26,27,28,29,21]

	#to draw sad face
	writer_point(strip,face,Color(0,0,0))
	writer_point(strip,mot,Color(0,50,20))

	strip.setPixelColor(42, Color(30,0,0))
	strip.setPixelColor(45, Color(30,0,0))
	strip.show()
	time.sleep(2)

	clear_lcd(strip,Color(0,0,0))

	# characters
	second_one = [12,20,28,36,44]
	second_two =[12,13,14,22,28,29,30,36,44,45,46]
	second_three =[12,13,14,20,28,29,30,36,44,45,46]
	second_four =[13,20,21,22,30,38,46]
	second_five=[12,13,14,20,28,29,30,38,44,45,46]
	second_six=[12,13,14,20,22,28,29,30,38,46]
	second_seven=[12,20,28,36,44,45,46]
	second_eight=[12,13,14,20,22,28,29,30,36,38,44,45,46]
	second_nine=[12,20,28,29,30,36,38,44,45,46]
	second_zero=[12,13,14,20,22,28,30,36,38,44,45,46]

	first_one=[9,17,25,33,41]
	first_two=[8,9,10,18,24,25,26,32,40,41,42]
	first_three=[8,9,10,16,24,25,26,32,40,41,42]
	first_four=[9,16,17,18,26,34,42]
	first_five=[8,9,10,16,24,25,26,34,40,41,42]
	first_six=[8,9,10,16,18,24,25,26,34,42]
	first_seven=[8,16,24,32,40,41,42]
	first_eight=[8,9,10,16,18,24,25,26,32,34,40,41,42]
	first_nine=[8,16,24,25,26,32,34,40,41,42]
	first_zero=[8,9,10,16,18,24,26,32,34,40,41,42]

	# writing score
	if point > 9 :
		first_digit=int(str(point)[1])
		second_digit=int(str(point)[0])
	else :
		first_digit = point
		second_digit = 0

	if second_digit ==1:
		writer_point(strip,second_one,Color(0,50,0))
	elif second_digit == 2 :
		writer_point(strip,second_two,Color(0,50,0))
	elif second_digit == 3:
		writer_point(strip,second_three,Color(0,50,0))
	elif second_digit == 4:
		writer_point(strip,second_four,Color(0,50,0))
	elif second_digit == 5:
		writer_point(strip,second_five,Color(0,50,0))
	elif second_digit == 6:
		writer_point(strip,second_six,Color(0,50,0))
	elif second_digit == 7:
		writer_point(strip,second_seven,Color(0,50,0))
	elif second_digit == 8:
		writer_point(strip,second_eight,Color(0,50,0))
	elif second_digit == 9:
		writer_point(strip,second_nine,Color(0,50,0))

	if first_digit == 1:
		writer_point(strip,first_one,Color(0,50,0))
	elif first_digit == 2:
		writer_point(strip,first_two,Color(0,50,0))
	elif first_digit == 3:
		writer_point(strip,first_three,Color(0,50,0))
	elif first_digit == 4:
		writer_point(strip,first_four,Color(0,50,0))
	elif first_digit == 5:
		writer_point(strip,first_five,Color(0,50,0))
	elif first_digit == 6:
		writer_point(strip,first_six,Color(0,50,0))
	elif first_digit == 7:
		writer_point(strip,first_seven,Color(0,50,0))
	elif first_digit == 8:
		writer_point(strip,first_eight,Color(0,50,0))
	elif first_digit == 9:
		writer_point(strip,first_nine,Color(0,50,0))
	else :
		writer_point(strip,first_zero,Color(0,50,0))

	strip.show()

# LED strip configuration:
LED_COUNT      = 64      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 155     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

if __name__ == '__main__':
	# create object for Adafruit_NeoPixel
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	strip.begin()

	print ('Press Ctrl-C to quit.')

	global ek_x
	global ek_y
	global timing

	ek_x = 0
	ek_y = 1

	ex_x_2=ex_x=x=3
	ex_y_2=ex_y=y=3

	x_rand=random.randint(-1,1)
	y_rand=random.randint(-1,1)

	# to crate random point for forage
	yem_x = random.randint(0,7)
	yem_y = random.randint(0,7)

	# control
	if ( x==yem_x and y==yem_y):
		yem_x = random.randint(0,7)
		yem_y = random.randint(0,7)

	liste_x = []
	liste_y = []

	# thead for keyboard interupts
	thread.start_new_thread( klavyeden, ("Thread-1",'' ))

	try :
		while True:
			liste_x.append(x)
			liste_y.append(y)

			sil_x=liste_x.pop(0)
			sil_y=liste_y.pop(0)

			if ( x==yem_x and y==yem_y):
				liste_x.append(x)
				liste_y.append(y)

				yem_x = random.randint(0,7)
				yem_y = random.randint(0,7)

				yeni = True
				while yeni:
					yeni = False
					for i in range(0,len(liste_x)):
						if ( yem_x==liste_x[i] and yem_y==liste_y[i]):
							yem_x = random.randint(0,7)
							yem_y = random.randint(0,7)
							yeni = True
							pass
			x = x + ek_x
			y = y + ek_y

			if x==-1 :
				x = 7
			if x==8 :
				x = 0
			if y==-1 :
				y = 7
			if y==8 :
				y = 0

			strip.setPixelColor(yem_y*8+yem_x, Color(0,100,0))
			strip.setPixelColor(y*8+x, Color(80,0,0))
			strip.setPixelColor(sil_y*8+sil_x, Color(0,0,0))

			for i in range(0,len(liste_x)):
				strip.setPixelColor(liste_y[i]*8+liste_x[i], Color(30,0,0))
			strip.show()
			time.sleep(400/1000.0)
			timing = True

			for i in range(0,len(liste_x)):
				if ( x==liste_x[i] and y==liste_y[i]):
					game_over(strip,(len(liste_x)+1))
					quit ()

	except (KeyboardInterrupt, SystemExit):
		curses.echo()
		curses.nocbreak()
		curses.endwin()

