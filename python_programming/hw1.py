# -*- coding: cp950 -*-
arr = raw_input("請輸入數字序列:")
arr = arr.split()
arr.sort(key = int,reverse=True) 
n = input("請問你要第幾大的數字:")
n = n-1
while n != -1 :
    print arr[n] 
    n = input("請問你要第幾大的數字:")
    n = n-1
print '程式結束'
for_pause = input("press enter to exit")