
from unicodedata import name
import copy

from testDict import getDependencies



class Task:
    name = ""
    reads = []
    writes = []
    run = None


def bernstein(t1,t2):
    for i in t1.writes:
        for j in t2.writes:
            if(i==j):
                print("interferance domaine d'écriture entre",t1.name,t2.name)
                return False
    for i in t1.reads:
        for j in t2.writes:
            if(i==j):
                print("inteferance entre le domaine de lecture de",t1.name, "et le domaine d'ecriture de",t2.name)
                return False
    for i in t1.writes:
        for j in t2.reads:
            if(i==j):
                print("inteferance entre le domaine d'ecriture de",t1.name, "et le domaine de lecture de",t2.name)
                return False      
            
    return True


#étapes de la parallèlisation maximal:

#Lister les interférences entre les diffèrentes taches
#Déterminer à partir des interférences les relations de précédences à imposer pour évites les interférences
#Supprimer les arcs qui n'entraineront pas d'interférence  --> parallèlisé les taches qui le peuvent
#Ajouter les relations de précédences trouver pour éviter les interférences 
#supprimer les redondances = les plus courts


#voir si la tache 1 a deja en précédence la tache 2 --> arret
""" t1 et t2 
    
    verifie cond bernstein
        si interferance alors
            verifier que t1 n'est pas deja en précédence de t2
        sinon
            je passe t1 en precedence de t2
        sinon je fait rien
    
 """ 


def SupprInter(nomt1,nomt2): 
    if not bernstein(nomt1, nomt2):#vérifie si interferance 
        if(dic[nomt2.name] == []): #si t2 n'a pas de precedences
            print(dic)
            dic[nomt2.name].append(nomt1.name)
            print(dic)
            return False
        for i in dic[nomt2.name]: #parcours les précédences de la tache 2
            if(i == nomt1.name): #Et ce que t1 est deja dans les precedences de t2
                print("relations de précédence entre",nomt1.name,nomt2.name)
                return False
            else:
                print(dic)
                dic[nomt2.name].append(nomt1.name) #ajout de t1 dans les précédence de t2
                print(dic)
                break
    else:
        print("Aucune interferance entre les deux taches")
        ParaTache(nomt1,nomt2)
        


def ParaTache(nomt1,nomt2):#Paralléliser les taches qui n'ont pas d'interférence 
    if bernstein(nomt1, nomt2):#pas d'interférance
        print(dic)
        dic[nomt2.name].remove(nomt1.name) #suppression de t1 dans les précédence de t2
        print(dic)





"""dic
    vérifier pour chaque taches celles qui en possédent 2 

"""




class TaskSystem:  
    #classe TaskSystem
    def __init__(self,taches,dic): 
        self.taches = taches
        self.dic = dic
    
    """def getDependencies(self,nomTache):
        for key in dic.keys():
            #str = " ".join(map(str, self.dic.get(key)))
            if(key == nomTache and dic.get(nomTache) == ""):
                print("La tache", nomTache, "n'a pas de précédence")
                break
            elif(key == nomTache and not dic[nomTache] == ""):
                print("Les précédences de la tache", nomTache,"sont", dic[nomTache])
                break"""
    
    def getDependencies(self,nomTache): # donne la liste des taches qui s'éxécute avant une tache donnée
        if(dic[nomTache.name] == []): #si la tache ne possède pas de précedence
             print("La tache "+nomTache.name+ " n'a pas de précédence")
        else:
            for value in dic[nomTache.name]:
                if(not value == ""):
                    print("Les précédences de la tache " + nomTache.name+ " sont", dic[nomTache.name])
                    return dic[nomTache.name]
                #elif(nomTache not in dic.keys()):
                    #print("la tache n'existe pas")
          
'''
def redondances(nomt1,nomt2):
        for i in range (len(dic)): #pour i dans la sequence des taches du dic de la premiere a la derniere tache
            for j in range(len(dic.get(i))): #pour j dans le sequence des precedences de la tache i
                for k in range(i+1,len(dic)): #pour k la tache suivant i dans le dic
                    for l in range (len(dic.get(k))): #pour l dna les precedences de k
                        if dic.get(i).get(j)==dic.get(k).get(l) and (TaskSystem.taches[k]) in dic.get(i).values():
                            dic.get(i).pop(dic.getKey(dic.get(i),dic.get(k).get(l)))
        return dic
'''

def redondances (nomt):
  
    s1.getDependencies(nomt)
    """
    for i in nomt:
         for j in nomt:
            if(i != j):
                 print (i)
                 print(j)
            break
        """
        
def run(self):
    print("att")
    l1 = taches
    l2 = list()
    lsp =list()# liste taches sans précédences
    for key, value in dic.items():
        if(not value):
            for t in taches:
                if(t.name==key):
                    lsp.append(t)
            
                    print(lsp)
            #while(i!= len(lsp)):
            for t1 in lsp:
                for t2 in lsp:
                    SupprInter(t1,t2)
                
                
            
    
          
#exécuter les tâches du système en parallélisant celles qui peuvent être parallélisées 
"""def run(self):
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
"""
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
t2.writes = ["X"]
t2.run = runT2

t3 = Task()
t3.name = "T3"
t3.writes = ["X"]
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

dic = {"somme":["T1","T2"],"T1":[],"T2":[],"T3":["T1"]}# le dictionnaire donne par l'utilisateur
dicfinal={} #le dictionnaire donne par la parallelisation maximal 


s1 = TaskSystem(taches,dic)

#afficher l'ensemble des precédences des taches de 1
#for i in s1.taches:
    #s1.getDependencies(i)

#print(dic.keys())

#s1.getDependencies(t3)

test = redondances(tSomme)
print(test)

#run(s1)
#SupprInter(t1,t2)
#ParaTache(t1,t2)





