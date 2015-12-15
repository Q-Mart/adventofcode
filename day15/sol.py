import itertools

#result, a, b, c, d
maxResult = [0,0,0,0,0]

#contraint functions, calculated from looking at input
def totalCapacity(a,b,c,d):
    calculation = (5*a) - b - d
    if calculation < 0: return 0
    else: return calculation

def totalDurability(a,b,c,d):
    calculation = -a + (3*b) - c
    if calculation < 0: return 0
    else: return calculation

def totalFlavor(a,b,c,d):
    calculation = 4*c
    if calculation < 0: return 0
    else: return calculation

def totalTexture(a,b,c,d):
    calculation = 2*d
    if calculation < 0: return 0
    else: return calculation

def totalCalories(a,b,c,d):
    calculation = 5*a + b + 6*c + 8*d
    if calculation < 0: return 0
    else: return calculation

for a,b,c,d in itertools.product(xrange(1,100), xrange(1,100), xrange(1,100), xrange(1,100)):
    if (a + b + c + d == 100) and (totalCalories(a,b,c,d) == 500):
        result = totalCapacity(a,b,c,d) * totalDurability(a,b,c,d) * totalFlavor(a,b,c,d) * totalTexture(a,b,c,d)

        if result > maxResult[0]: maxResult = [result,a,b,c,d]

print maxResult
