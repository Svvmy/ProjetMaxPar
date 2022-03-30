from unicodedata import name


class Task:
    name = ""
    reads = []
    writes = []
    run = None

def bernstein(t1,t2):
    for i in t1.writes:
        for j in t2.writes:
            if(i==j):
                print("interferance")
                return False
    for i in t1.writes:
        for j in t2.reads:
            if(i==j):
                print("inteferance")
                return False
    for i in t2.writes:
        for j in t1.reads:
            if(i==j):
                print("inteferance")
                return False      
            return True


#utilisation de la classe Task   
X = None
Y = None
Z = None
M = None

def runT1():
    global X
    X = 1

def runT2():
    global Y
    Y = 2

def runT3():
    global M
    M = 3

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

t3 = Task()
t3.name = "T2"
t3.writes = ["M"]
t3.run = runT3

tSomme = Task()
tSomme.name = "somme"
tSomme.reads = ["X", "Y"]
tSomme.writes = ["Z"]
tSomme.run = runTsomme

class TaskSystem:  
    #classe TaskSystem
    def __init__(self,taches,dic): 
        self.taches = taches
        self.dic = dic
    
    
    def getDependencies(self,nomTache):# donne pour une tache la liste des taches à exécuter avant cette tache
        dicfinal[nomTache.name] = list()
        for i in dic[nomTache.name]:
            for j in taches:
                if(j.name == i):
                    if not bernstein(nomTache,j):
                        dicfinal[nomTache.name].append(i)
        
            




# liste des taches
taches = list()

#ajouter les tâches à la liste
taches.append(tSomme)
taches.append(t1)
taches.append(t2)
taches.append(t3)

dic = {"somme":["T1","T2"],"T1":[],"T2":["T3","T1"],"T3":[]}# le dictionnaire donne par l'utilisateur
dicfinal={} #le dictionnaire donne par la parallelisation maximal 


s1 = TaskSystem([t1, t2, tSomme], {"T1": [], "T2": ["T1"], "somme": ["T1", "T2"]})