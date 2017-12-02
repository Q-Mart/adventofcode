def getInput():
    with open('inputs/1.txt') as f:
        data = f.read().strip()

    return data

def processCaptcha(captcha):
    acc = 0
    for i in range(len(captcha)):
        next = (i+1)%len(captcha)
        if captcha[i] == captcha[next]:
            acc += int(captcha[i])

    return acc

def processSecondCaptcha(captcha):
    acc = 0
    length = len(captcha)
    halfLength = int(length/2)
    for i in range(length):
        next = (i+halfLength)%length
        if captcha[i] == captcha[next]:
            acc += int(captcha[i])

    return acc

assert processCaptcha('1122') == 3
assert processCaptcha('1111') == 4
assert processCaptcha('1234') == 0
assert processCaptcha('91212129') == 9

assert processSecondCaptcha('1212') == 6
assert processSecondCaptcha('1221') == 0
assert processSecondCaptcha('123425') == 4
assert processSecondCaptcha('123123') == 12
assert processSecondCaptcha('12131415') == 4

inp = getInput()
print(processCaptcha(inp))
print(processSecondCaptcha(inp))
