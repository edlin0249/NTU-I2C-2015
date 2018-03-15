# -*- coding: cp950 -*-

def palindrome(str):
    str1 = str[::-1]
    length = len(str)
    for i in range(1,length):
        a=cmp(str[:i],str1[-i:])
        b=cmp(str[i:],str1[:-i])
        if(a == 0  and b == 0):
            first = str[:i]
            second = str[i:]
            return first , second , True 
    return 0 , 0 , False
        


str = raw_input("請輸入字串:")
first , second , result = palindrome(str)
if result == True :
    print str,'是雙回文字串 , ',str,' = ',first,' + ',second
else:
    print str,'不是雙回文字串'
for_pause = input("press enter to exit")