def findWhat(stringN) :
    countError = 0
    countWarn = 0
    countNotice = 0
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
        FXXK.append(stringN)

    print '================COUNT================'
    print "Error  : ", countError
    print "Warn   : ", countWarn
    print "Notice : ", countNotice
    print '================ERROR================'
    print error
    print '\n'
    print '================WARN================='
    print warn
    print '\n'
    print '================NOTICE==============='
    print notice
    print '\n'
    print '================ELSE================='
    print FXXK
    print '\n'
    print '=================END================='


error=[]
warn=[]
notice=[]
FXXK=[]

input = "[Fri Oct 05 08:35:39 2012] [error] [client ::1] File does not exist: /Library/WebServer/Documents/favicon.ico"

findWhat(input)

