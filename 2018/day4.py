import utils
import re
import collections

def getTime(string):
    search = re.search(r'\d\d:\d\d', string).group()
    if search[0:2] != '00':
        return 0
    else:
        return int(search[3:])

def newGuard(string):
    search = re.findall(r'(?<=Guard #)\d+', string)
    if search:
        return int(search[0])
    else:
        return None

def regexPresent(regex, string):
    return re.findall(regex, string) != []

def fallsAsleep(string):
    return regexPresent('falls asleep', string)

def wakesUp(string):
    return regexPresent('wakes up', string)

log = utils.getDay(4)
log.sort()
# log = ["[1518-11-01 00:00] Guard #10 begins shift",
#        "[1518-11-01 00:05] falls asleep",
#        "[1518-11-01 00:25] wakes up",
#        "[1518-11-01 00:30] falls asleep",
#        "[1518-11-01 00:55] wakes up",
#        "[1518-11-01 23:58] Guard #99 begins shift",
#        "[1518-11-02 00:40] falls asleep",
#        "[1518-11-02 00:50] wakes up",
#        "[1518-11-03 00:05] Guard #10 begins shift",
#        "[1518-11-03 00:24] falls asleep",
#        "[1518-11-03 00:29] wakes up",
#        "[1518-11-04 00:02] Guard #99 begins shift",
#        "[1518-11-04 00:36] falls asleep",
#        "[1518-11-04 00:46] wakes up",
#        "[1518-11-05 00:03] Guard #99 begins shift",
#        "[1518-11-05 00:45] falls asleep",
#        "[1518-11-05 00:55] wakes up"]


# populate dict of list of guards that fall asleep at each minute
minutesForEachGuard = collections.defaultdict(list)
totalMinutesForEachGuard = collections.defaultdict(int)

currentGuard = None
asleep = None
for l in log:
    if newGuard(l):
        currentGuard = newGuard(l)
        asleep = None
    elif fallsAsleep(l):
        asleep = getTime(l)
    elif wakesUp(l):
        time = getTime(l)
        for t in range(asleep, time):
            totalMinutesForEachGuard[currentGuard] += 1
            minutesForEachGuard[t].append(currentGuard)
    else:
        print('ERROR')

sleepiestGuard = max(totalMinutesForEachGuard, key=totalMinutesForEachGuard.get)

bestMinute = None
bestFrequency = 0
for m, gs in minutesForEachGuard.items():
    frequencySleepingAtThisMinute = len(list(filter(lambda x: x==sleepiestGuard, gs)))
    if frequencySleepingAtThisMinute > bestFrequency:
        bestFrequency = frequencySleepingAtThisMinute
        bestMinute = m

print (bestMinute * sleepiestGuard)

# Part 2
sleepiestGuard = None
bestMinute = None
bestFrequency = 0
for m, gs in minutesForEachGuard.items():
    for guard in set(gs):
        frequency = len(list(filter(lambda x: x==guard, gs)))
        if frequency > bestFrequency:
            bestFrequency = frequency
            sleepiestGuard = guard
            bestMinute = m

print (bestMinute * sleepiestGuard)
