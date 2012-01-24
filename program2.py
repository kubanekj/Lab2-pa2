import random
x = input('Input the x-coordinate of the drunk\'s home: ')
y = input('Input the y-coordinate of the drunk\'s home: ')
k = input('Input the number of steps the drunk will take: ')
 

def walk(k, homeX, homeY):
	xLocation = 0
	yLocation = 0
	randomDir = 0
	hits = False
	random.seed()
	while k > 0:
		randomDir = random.randint(0,3)
		print randomDir
		# 0 means go backwards(-y)
		if randomDir == 0:
			yLocation -= 1
		# 1 means go left(-x)
		elif randomDir == 1:
			xLocation -= 1
		# 2 means go forward(+y)
		elif randomDir == 2:
			yLocation += 1
		# 3 means go right(+x)
		else:
			xLocation += 1
		print '( %d , %d )' % (xLocation, yLocation)
		if homeX == xLocation:
			if homeY == yLocation:
				hits = True
				print 'Home'
				break
		k -= 1
	print 'Done'
	return hits
runs = 0.0
home = 0.0
while runs < 10.0:
	if walk(k,x,y):
		home += 1.0
	runs +=  1.0
print 'Made it home %d percent of the time' % (home/runs)