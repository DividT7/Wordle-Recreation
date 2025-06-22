import turtle as t
import random as rand
from urllib.request import urlopen, Request

greensquare = 'GreenSquare.gif'
graysquare = 'GraySquare.gif'
yellowsquare = 'YellowSquare.gif'
whitesquare = 'WhiteSquare.gif'
borderline = 'BorderLine.gif'


base = 'https://www.merriam-webster.com/dictionary/'

wn = t.Screen()
wn.setup()
wn.screensize(canvwidth=1000, canvheight=1000)
userguess=[]
greenletters=[]
lettercount=0
x2=-150
y2=100
rowcount = 0

box = t.Turtle()
box.ht()
box.pu()
box.color('gray')
box.speed(0)
box.width(1)

wn.addshape(greensquare)
wn.addshape(graysquare) 
wn.addshape(yellowsquare)
wn.addshape(whitesquare)
wn.addshape(borderline)

white = t.Turtle()
white.ht()
white.shape(whitesquare)
white.color('white')
white.pu()
white.speed(0)

green = t.Turtle()
green.ht()
green.shape(greensquare)
green.color('white')
green.pu()
green.speed(0)

yellow = t.Turtle()
yellow.ht()
yellow.shape(yellowsquare)
yellow.color('white')
yellow.pu()
yellow.speed(0)

gray = t.Turtle()
gray.ht()
gray.shape(graysquare)
gray.color('white')
gray.pu()
gray.speed(0)

black = t.Turtle()
black.ht()
black.shape(borderline)
black.color('black')
black.pu()
black.speed(0)


#c9b458


#box.fillcolor('gray')

#box.ht()

rand_word = ['Adult','Agent','Anger','Apple','Award','Basis','Beach','Birth','Block','Blood','Board','Brain','Bread','Brown','Buyer','Cause','Chain','Chair','Chest','Chief','Child','Claim','Class','Clock','Coach','Coast','Court','Cover','Cream','Crime','Cross','Crowd','Crown','Cycle','Dance','Death','Depth','Doubt','Draft','Drama','Dream','Dress','Drink','Drive','Earth','Enemy','Entry','Error','Event','Faith','Fault','Field','Fight','Final','Floor','Focus','Force','Frame','Frank','Front','Fruit','Glass','Grant''Grass','Green','Group','Guide','Heart','Horse','Hotel','House','Image','Index','Input','Issue','Japan','Jones','Judge','Knife','Layer','Level','Light','Limit','Lunch','Major','March','Match','Metal','Model','Money','Month','Motor','Mouth','Music','Night','Noise','North','Novel','Nurse','Offer','Order','Other','Owner','Panel','Paper','Party','Peace','Peter','Phase','Phone','Piece','Pilot','Pitch','Place','Plane','Plant','Plate','Point','Pound','Power','Press','Price','Pride','Prize','Proof','Queen','Radio','Range','Ratio','Reply','Right','River','Round','Route','Rugby','Scale','Scene','Scope','Score','Sense','Shape','Share','Sheep','Sheet','Shift','Shirt','Shock','Sight','Simon','Skill','Sleep','Smile','Smith','Smoke','Sound','South','Space','Speed','Spite','Sport','Squad','Staff','Stage','Start','State','Steam','Steel','Stock','Stone','Store','Study','Stuff','Style','Sugar','Table','Taste','Terry','Theme','Thing','Title','Total','Touch','Tower','Track','Trade','Train','Trend','Trial','Trust','Truth','Uncle','Union','Unity','Value','Video','Visit','Voice','Waste','Watch','Water','While','White','Whole','Woman','World','Youth',]


	




def generate():
	global r
	r = (rand.choice(rand_word)).lower()
generate()

def drawgrid():
	x = -150
	y = 100
	for i in range (6):	
		box.goto(x,y)
		for i in range (5):
			for i in range(4):
				box.pd()
				box.fd(49)
				box.left(90)
			box.pu()
			box.fd(58)
		y-=58
	
drawgrid()

def lettertyped(letter):
	global x2,y2,lettercount
	box.color('black')
	if rowcount != 6:
		if lettercount<5:
			box.goto(x2,y2)
			#for i in range(4):
				#box.pd()
				#box.fd(50)
				#box.left(90)
			black.pu()
			black.goto(x2+25,y2+24)
			box.goto(x2+25,y2+7)
			black.stamp()
			box.write(letter.upper(),align='center',font=('sans-serif',21))
			box.goto(x2,y2)
			if lettercount<=5:
				x2+=58

def checkword(userguess):
	global x2,y2,lettercount,r,rowcount
	if rowcount != 6:
		if lettercount==5:
			guess=''.join(userguess) 
			url = base + guess
			try:                       #try, except, else: tries code of line, and if results in an error, the code goes to except, otherwise it goes else
				request = Request(url)
				response = urlopen(request)
				response = response.read()
			except:
				print ('Not in word list')
			else:
				for i in range(5):
					if userguess[i]==r[i]:
						x2 = -150 
						y2 = 100 - (rowcount*58)
						green.goto(x2+25.5+(i*58),y2+25)
						green.stamp()
						green.goto(x2+25.5+(i*58),y2+7)
						green.write(r[i].upper(),align='center',font=('sans-serif',21))
						greenletters.append(i)
					check_first = r.find(userguess[i])
					if check_first != (-1):
						if userguess[i] != r[i]: 
							x2 = -150
							y2 = 100 - (rowcount*58)
							yellow.goto(x2+25.5+(i*58),y2+25)
							yellow.stamp()
							yellow.goto(x2+25.5+(i*58),y2+7)
							yellow.write(userguess[i].upper(),align='center',font=('sans-serif',21))
							greenletters.append(i)
					check_none = i in greenletters
					if check_none == False:
						x2 = -150
						y2 = 100 - (rowcount*58)
						gray.goto(x2+25.5+(i*58),y2+25)
						gray.stamp()
						gray.goto(x2+25.5+(i*58),y2+7)
						gray.write(userguess[i].upper(),align='center',font=('sans-serif',21))	
				userguess.clear()
				if len(greenletters) == 5:
					print ('You Won!')
					rowcount = 5
				lettercount = 0
				rowcount+=1
				if rowcount == 6:
					if len(greenletters)!=5:
						print ('You Lose. The word was', r)
				x2 = -150
				y2 = 100 - (rowcount*58)
				greenletters.clear()
		
		#check the word, to draw green, yellow, gray square


def backspace():
	global lettercount,x2
	if lettercount>=1:
		white.goto(x2-33,y2+24)
		white.stamp()
		x2-=58
		lettercount-=1
		userguess.pop(lettercount)
		box.color('gray')
		box.goto(x2,y2)
		#for i in range(4):
		#	box.pd() 
		#	box.fd(50)
		#	box.left(90)
		#	box.pu()
		#box.color('black')
		
def type_Q():
	global lettercount
	if lettercount<5:
		lettertyped('q')
		userguess.append('q')
		lettercount+=1

def type_W():
	global lettercount
	if lettercount<5:
		lettertyped('w')
		userguess.append('w')
		lettercount+=1
def type_E():
	global lettercount
	if lettercount<5:
		lettertyped('e')
		userguess.append('e')
		lettercount+=1
def type_R():
	global lettercount
	if lettercount<5:
		lettertyped('r')
		userguess.append('r')
		lettercount+=1
def type_T():
	global lettercount
	if lettercount<5:
		lettertyped('t')
		userguess.append('t')
		lettercount+=1
def type_Y():
	global lettercount
	if lettercount<5:
		lettertyped('y')
		userguess.append('y')
		lettercount+=1
def type_U():
	global lettercount
	if lettercount<5:
		lettertyped('u')
		userguess.append('u')
		lettercount+=1
def type_I():
	global lettercount
	if lettercount<5:
		lettertyped('i')
		userguess.append('i')
		lettercount+=1
def type_O():  
	global lettercount
	if lettercount<5:
		lettertyped('o')
		userguess.append('o')
		lettercount+=1
def type_P():
	global lettercount
	if lettercount<5:
		lettertyped('p')
		userguess.append('p')
		lettercount+=1
def type_A():
	global lettercount
	if lettercount<5:
		lettertyped('a')
		userguess.append('a')
		lettercount+=1
def type_S():
	global lettercount
	if lettercount<5:
		lettertyped('s')
		userguess.append('s')
		lettercount+=1
def type_D():
	global lettercount
	if lettercount<5:
		lettertyped('d')
		userguess.append('d')
		lettercount+=1
def type_F():
	global lettercount
	if lettercount<5:
		lettertyped('f')
		userguess.append('f')
		lettercount+=1
def type_G():
	global lettercount
	if lettercount<5:
		lettertyped('g')
		userguess.append('g')
		lettercount+=1
def type_H():
	global lettercount
	if lettercount<5:
		lettertyped('h')
		userguess.append('h')
		lettercount+=1
def type_J():
	global lettercount
	if lettercount<5:
		lettertyped('j')
		userguess.append('j')
		lettercount+=1
def type_K():
	global lettercount
	if lettercount<5:
		lettertyped('k')
		userguess.append('k')
		lettercount+=1
def type_L():
	global lettercount
	if lettercount<5:
		lettertyped('l')
		userguess.append('l')
		lettercount+=1
def type_Z():
	global lettercount
	if lettercount<5:
		lettertyped('z')
		userguess.append('z')
		lettercount+=1
def type_X():
	global lettercount
	if lettercount<5:
		lettertyped('x')
		userguess.append('x')
		lettercount+=1
def type_C():
	global lettercount
	if lettercount<5:
		lettertyped('c')
		userguess.append('c')
		lettercount+=1
def type_V():
	global lettercount
	if lettercount<5:
		lettertyped('v')
		userguess.append('v')
		lettercount+=1
def type_B():
	global lettercount
	if lettercount<5:
		lettertyped('b')
		userguess.append('b')
		lettercount+=1
def type_N():
	global lettercount
	if lettercount<5:
		lettertyped('n')
		userguess.append('n')
		lettercount+=1
def type_M():
	global lettercount
	if lettercount<5:
		lettertyped('m')
		userguess.append('m')
		lettercount+=1




def type_enter():
  checkword(userguess)
wn.onkeypress(type_Q,"q")
wn.onkeypress(type_W,"w")
wn.onkeypress(type_E,"e")
wn.onkeypress(type_R,"r")
wn.onkeypress(type_T,"t")
wn.onkeypress(type_Y,"y")
wn.onkeypress(type_U,"u")
wn.onkeypress(type_I,"i")
wn.onkeypress(type_O,"o")
wn.onkeypress(type_P,"p")
wn.onkeypress(type_A,"a")
wn.onkeypress(type_S,"s")
wn.onkeypress(type_D,"d")
wn.onkeypress(type_F,"f")
wn.onkeypress(type_G,"g")
wn.onkeypress(type_H,"h")
wn.onkeypress(type_J,"j")
wn.onkeypress(type_K,"k")
wn.onkeypress(type_L,"l")
wn.onkeypress(type_Z,"z")
wn.onkeypress(type_X,"x")
wn.onkeypress(type_C,"c")
wn.onkeypress(type_V,"v")
wn.onkeypress(type_B,"b")
wn.onkeypress(type_N,"n")
wn.onkeypress(type_M,"m")
wn.onkeypress(type_enter, 'Return')
wn.onkeypress(backspace, 'BackSpace')

wn.listen()



wn.mainloop()
