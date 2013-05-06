def throwerror(ErrNum) :
    if ErrNum == 101 :
        print HulHul
    if ErrNum == 202 :
        print HulHulHulHul

def findWhat(stringN) :
    name = stringN.split()[5]
    
    if name == "[error]" :
        value = stringN.split(']')[3]
        str = value.split(':')

        search1 = ['File','does','not','exist']
        search2 = ['Invalid','URI','in','request','GET','invalid']
        search3 = ['script','not','found','or','unable','to','stat']
        search4 = ['client','denied','by','server','configuration']
        search5 = ['attempt','to','invoke','directory','as','script']

        result1 = all(x in str[0] for x in search1)
        result2 = all(x in str[0] for x in search2)
        result3 = all(x in str[0] for x in search3)
        result4 = all(x in str[0] for x in search4)
        result5 = all(x in str[0] for x in search5)
        
        if result1 == True :
            errorFDNE.append(str)
            error.append(stringN)
        elif result2 == True :
            errorIUIRGI.append(str)
            error.append(stringN)
        elif result3 == True :
            errorSNFOUTS.append(str)
            error.append(stringN)
        elif result4 == True :
            errorCDBSC.append(str)
            error.append(stringN)
        elif result5 == True :
            errorATIDAS.append(str)
            error.append(stringN)
        else :
            errUNKNOWN.append(str)
            error.append(stringN)

    elif name == "[notice]" :
        notice.append(stringN)

    elif name == "[warn]" :
        warn.append(stringN)

    else :
        FXXK.append(stringN)

def showresult() :
    print '================================COUNT================================'
    print "Error  : ", len(error)
    print "Warn   : ", len(warn)
    print "Notice : ", len(notice)
    print "Else   : ", len(FXXK)
    print '================================ERROR================================'
    print "1. File does not exist : \n"
    for x in range(0,len(errorFDNE)) :
        print errorFDNE[x][1]
    print "\n"
    print "2. Invalid URI in request GET invalid : \n"
    for x in range(0,len(errorIUIRGI)) :
        print errorIUIRGI[x][0]
    print "\n"
    print "3. script not found or unable to stat : \n"
    for x in range(0,len(errorSNFOUTS)) :
        print errorSNFOUTS[x][1]
    print "\n"
    print "4. client denied by server configuration : \n"
    for x in range(0,len(errorCDBSC)) :
        print errorCDBSC[x][1]
    print "\n"
    print "5. attempt to invoke directory as script : \n"
    for x in range(0,len(errorATIDAS)) :
        print errorATIDAS[x][1]
    print "\n"
    print "6. Unknown : \n"
    for x in range(0,len(errUNKNOWN)) :
        print errUNKNOWN[x]
    print "\n"
    print '================================WARN================================='
    for x in range(0,len(warn)) :
        print warn[x]
    print '================================NOTICE==============================='
    for x in range(0,len(notice)) :
        print notice[x]
    print '================================ELSE================================='
    for x in range(0,len(FXXK)) :
        print FXXK[x]
    print '================================END=================================='

error=[]
errorFDNE=[]
errorIUIRGI=[]
errorSNFOUTS=[]
errorCDBSC=[]
errorATIDAS=[]
errUNKNOWN=[]
warn=[]
notice=[]
FXXK=[]

try :
    errorFile = open('/Users/TARDIS/Documents/GIT_EX/error_log.txt')
    for line in errorFile:
        findWhat(line)
    showresult()

except hulhul:
    throwerror(101)

except HulHulHulHul:
    throwerror(202)