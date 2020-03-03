fp = open("C:/Users/kvatsa/Desktop/git_hub/size.txt",'r+')

sz= fp.read()
sz= list(r.split("\n"))
sz= r[-6]
sz= r.split()
sz= int(r[1])
sz= sz/(1e+6)
print(sz)