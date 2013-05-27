# -*- coding: utf-8 -*-
import re
class log_analysis:
    def throwerror(ErrNum) :
        if ErrNum == 101 :
            print HulHul
        if ErrNum == 202 :
            print HulHulHulHul

    def findError(stringN) :
        if stringN.find("error") >= 0 :
            value = stringN.split(']')[3]
        
            if(value.find(':') != -1 ) :
                error_point = value.split(':')
            
                #re_point = x.strip() for x in error_point
                #ERROR 발생.
                #원인 알 수 없음

                repoint = map(str.strip, error_point)
            
                error_name = repoint[0]
                error_location = repoint[1]
        
            else :
                error_name = value
                error_location = None
        
            '''
            도움을 받아 생성한 if문.
            해결하지 못했던 디렉토리가 존재하지 않는 경우에도 처리가능.
            신난다.
            '''

            if error_name in logName :
                logName[error_name].append(error_location)

            else :
                logName[error_name] = [error_location]

            '''
            logName이라는 딕셔너리에 이름을 key로 갖고 디렉토리를 value로 갖는 pair 추가
            key 값이 존재하지 않으면 추가하고 존재하면 append.
            '''

        else :
            pass

    def showResult() :
        key_num = logName.keys()

        print '================================COUNT================================'
        count = 0
    
        for i in range(0, len(key_num)) :
            count += len(logName.get(key_num[i]))
        print "Error  : ", count
        for i in range(0, len(key_num)) :
            print key_num[i], len(logName.get(key_num[i]))
    
        print '================================ERROR================================'
        for i in range(0, len(key_num)) :
            print key_num[i]
            print logName.get(key_num[i])
            #for j in range(0, len(logName.get(key_num)[i])) :
            #    print logName.get(key_num[i])[j]
            #왜 오류가 나는지 이해할 수 없음

        print '================================END=================================='
    '''
    def saveFile(nameFile) :
        with open(nameFile, 'w') as reportData :
            import showResult
            print(showResult(), file=reportData)

    def except_Pic() :
        for line in errorFile :
            if(not(re.search(r'(jpg|gif|png)',error_location))) :
                findError(line)
    '''
logName = {}

errorFile = open('/Users/TARDIS/Documents/GIT_EX/error_log.txt')
for line in errorFile:
    findError(line)
showResult()
'''
except_Pic()
saveFile(Report.txt)
'''