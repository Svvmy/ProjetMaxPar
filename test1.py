from unicodedata import name


class Task:
    name = ""
    reads = []
    writes = []
    run = None
 

X = None
Y = None
Z = None
dico = {"t1" : "",
        "t2" : "t1",
         "tSomme": ["t1","t2"]}

def runT1():
    global X
    X = 1

def runT2():
    global Y
    Y = 2

def runTsomme():
    global X, Y, Z
    Z = X + Y

t1 = Task()
t1.name = "T1"
t1.writes = ["X"]
t1.run = runT1

t2 = Task()
t2.name = "T2"
t2.writes = ["Y"]
t2.run = runT2

tSomme = Task()
tSomme.name = "somme"
tSomme.reads = ["X", "Y"]
tSomme.writes = ["Z"]
tSomme.run = runTsomme

def interfere(t1,t2):
    t1.writes
    t2.writes
    t1.reads
    t2.reads
    for i in t1.writes:
        for j in t2.writes:
            if(i==j):
                print("interferance")
            else:
                print("pas d'interferance") 
    for i in t1.writes:
            for j in t2.reads:
                if(i==j):
                    print("inteferance")
            else:
                    print("pas d'inteferance")
    for i in t2.writes:
            for j in t1.reads:
                if(i==j):
                    print("inteferance")
            else:
                    print("pas d'inteferance")      
            
            
            
            break


interfere(t1,t2)

