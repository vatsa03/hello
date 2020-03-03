fp = open("C:/Users/kvatsa/Desktop/git_hub/size.txt",'r+')

sz= fp.read()
sz= list(sz.split("\n"))
sz= sz[-6]
sz= sz.split()
sz= int(sz[1])
sz= sz/(1e+6)
print(sz)
