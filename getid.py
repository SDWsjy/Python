import re
pa=r'\"(\d+)\"\,'
f2=open('D:\question\\14.csv','r')
s=f2.read()
ms=re.findall(pa, s)
f2.close()
print ms[0]
f3=open('D:\\answer\\14.txt','a')
i=0
lid=len(ms)
print lid
while i<lid:
	m=ms[i]
	i+=1
	f3.write(m)
	f3.write(',')
f3.close()