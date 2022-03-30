from unicodedata import name
import copy


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
    for i in t1.reads:
        for j in t2.writes:
            if(i==j):
                print("inteferance")
                return False
    for i in t1.writes:
        for j in t2.reads:
            if(i==j):
                print("inteferance")
                return False      
            return True


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
        
            
#exécuter les tâches du système en parallélisant celles qui peuvent être parallélisées 
def run(self):
     id=0
     dictio= copy.deepcopy(dicfinal) #on travail sur une copie du dictionaire
     l1= taches #listes des taches non-éxecutées encore
     l2= list() #listes des taches déja éxecutées
     print("les tâche de niveau",id,end=": ")
     for key, value in dictio.items(): #éxecuter les taches de niveau 0
      if(not value): #pas de precedence 
        for t in taches:
            if (t.name==key):
                l2.append(t)
                l1.remove(t)
                print(t.name,end=":")
                t.run()
                dicfinal.pop(key)
     e=True

     while(l1):#éxecuter les autres tâches
      print()
      id=id+1
      print("les tâche de niveau", id, end=": ")
      dictio = copy.deepcopy(dicfinal)
      for key, value in dictio.items():
       for v in value:
         for t in l2:
          if(t.name==v):
           e=True
           break
          else:
           e=False
       if(e):

             T=getTache(key,l1)
             l2.append(T)
             l1.remove(T)
             print(T.name, end=":")
             T.run()
             dicfinal.pop(key)
     print()
     print("Pour consulter l'ordre et les précédents de chaque tâches, il faut consulter le vrai dictionaire (dicfinal)")

def getTache(nomdetache,taches):
    for t in taches:
        if(nomdetache == t.name):
            return t


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