#Terniary operators
print("Ternery operator")

a=10
b=20
c=a if a<b else b
print(c)

a,b=10,20
print(a,b)

print((b,a) [a<b])

print({True:a,False:b} [a<b])

print((lambda:b,lambda:a) [a<b]())