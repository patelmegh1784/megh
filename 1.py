import pickle
'''print("WORKING WITH BINARY FILES")
with open("empfile.dat","wb")as bf:
    edata=["eno,","ename","ebasic","totsal"]
    pickle.dump(edata,bf)
'''


try:
    with open("empfile.dat","rb") as bfile:
        while True:
            edata=pickle.load(bfile)
        #print("Record Number ;",readrec)
            print(edata)
        #readrec=readrec+1
except EOFError:
    pass
