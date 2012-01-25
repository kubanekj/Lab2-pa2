y = input('Enter number of iterations: ')
trueVal = 0.0
roundedVal = 0.0
trueMultVal = 0.0
roundedMultVal = 0.0
increment = 0.09961
incrementError = 0.0
multError = 0.0

def round_four(x):
	magnitude = 0
	while x >= 1.0:
		x /= 10
		magnitude = magnitude + 1
	while x < .1:
		x *= 10
		magnitude = magnitude - 1
	x = round(x,4)
	x = x * (10 ** magnitude)
	return x
	
for i in range(0,y):
	trueVal = trueVal + increment
	roundedVal = round_four(roundedVal + increment)
incrementError = abs(trueVal - roundedVal)

print 'Actual: ' , trueVal
print 'Computed: ' , roundedVal
print 'The absolute error for \"t[i] = t[i-1] + dt\" is ', incrementError

trueMultVal = y * increment
roundedMultVal = round_four(y*increment)
multError = abs(trueMultVal - roundedMultVal)

print 'Actual: ' , trueMultVal
print 'Computed: ' , roundedMultVal
print 'The absolute error for \"t = i * dt\" is ', multError 