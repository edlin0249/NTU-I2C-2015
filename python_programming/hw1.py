# -*- coding: cp950 -*-
arr = raw_input("�п�J�Ʀr�ǦC:")
arr = arr.split()
arr.sort(key = int,reverse=True) 
n = input("�аݧA�n�ĴX�j���Ʀr:")
n = n-1
while n != -1 :
    print arr[n] 
    n = input("�аݧA�n�ĴX�j���Ʀr:")
    n = n-1
print '�{������'
for_pause = input("press enter to exit")