countError = 0
countWarn = 0
countNotice = 0
countFxxk = 0

def throwerror(number) :
    if number == 

def findWhat(stringN) :
    global countError
    global countWarn
    global countNotice
    global countFxxk
    
    name = stringN.split()[5]
    
    if name == "[error]" :
        countError += 1
        error.append(stringN)

    elif name == "[notice]" :
        countNotice += 1
        notice.append(stringN)

    elif name == "[warn]" :
        countWarn += 1
        warn.append(stringN)

    else :
        countFxxk += 1
        FXXK.append(stringN)

def showresult() :
    print '================================COUNT================================'
    print "Error  : ", countError
    print "Warn   : ", countWarn
    print "Notice : ", countNotice
    print "Else   : ", countFxxk
    print '================================ERROR================================'
    for x in range(0,countError) :
        print error[x]
    print '================================WARN================================='
    for x in range(0,countWarn) :
        print warn[x]
    print '================================NOTICE==============================='
    for x in range(0,countNotice) :
        print notice[x]
    print '================================ELSE================================='
    for x in range(0,countFxxk) :
        print FXXK[x]
    print '================END=================='


error=[]
warn=[]
notice=[]
FXXK=[]

countError = 0
countWarn = 0
countNotice = 0

errorFile = open('/Users/TARDIS/Documents/GIT_EX/error_log.txt')
for line in errorFile:
    findWhat(line)
showresult()


