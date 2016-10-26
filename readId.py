f=open('D:\\answer\cs.txt','r')
ids=f.read()
#print ids
m=ids.split(',') 
m1=m[:10]
m2=m[10:20]
print m1 
print m2
print m[2],m[3],m[4]
print type(m[2])
