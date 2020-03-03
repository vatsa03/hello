fp = open("C:/Users/kvatsa/Desktop/git_hub/size.txt",'r+')

sz= fp.read()
sz= list(sz.split("\n"))
sz= sz[-6]
sz= sz.split(" ")
print(sz)
