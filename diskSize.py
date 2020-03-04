<<<<<<< HEAD
import socket
=======
>>>>>>> c3dbe81b424a1e747838523db78f44a171502008
fp = open("C:/Users/kvatsa/Desktop/git_hub/size.txt",'r+')
sz= fp.read()
sz= list(sz.split("\n"))
sz= sz[-6]
sz= sz.split("KB available on disk.")
sz=sz[0]
sz=sz.strip(" ")
sz= int(sz)
sz= sz/(1e+6)
print(socket.gethostname(), sz, sep=" ", end= " ")
