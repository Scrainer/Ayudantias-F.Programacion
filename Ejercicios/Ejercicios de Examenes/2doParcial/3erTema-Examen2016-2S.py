A={1,2,3,4,5}
B={4,5,6,7,8,9}
C={5,4,7,0,1}
Y={len(A),len(B),len(C)}

X=A|B
Z=X^C
E=X-C
print(A.issubset(E))

Y=A&Y
Z=Y-C
print(Z)