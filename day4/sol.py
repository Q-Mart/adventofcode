import hashlib

key = 'iwrupvqb'
answer = 0

m = hashlib.md5(key + str(answer))
md5String = m.hexdigest()

while md5String[0:5] != '00000':
    answer += 1
    m = hashlib.md5(key + str(answer))
    md5String = m.hexdigest()

print answer 
print md5String
