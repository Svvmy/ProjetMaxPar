
import time
from unicodedata import name
import copy
import threading


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
        for i in dic[nomt1.name]: #parcours les précédences de la tache 1
            if(i == nomt2.name): #Est ce que t2 est deja dans les precedences de t1 ?
                print(nomt2.name," précéde ",nomt1.name)
                return False
        if(dic[nomt2.name] == []): #si t2 n'a pas de precedences
            dic[nomt2.name].append(nomt1.name)
            return False
        for i in dic[nomt2.name]: #parcours les précédences de la tache 2
            if(i == nomt1.name): #Est ce que t1 est deja dans les precedences de t2 ?
                print(nomt1.name," précéde ",nomt2.name)
                return False
        else:
            dic[nomt2.name].append(nomt1.name) #ajout de t1 dans les précédence de t2
            print("ajout de "+nomt1.name+" dans les précédences "+nomt2.name)
            #break
    else:
        print("Aucune interferance entre les deux taches "+nomt1.name+ " et " +nomt2.name)
        return True
        
        


def ParaTache(nomt1,nomt2):#Paralléliser les taches qui n'ont pas d'interférences 
    if bernstein(nomt1, nomt2):#pas d'interférance
        for i in dic[nomt2.name]:
            if(i == nomt1.name):
                dic[nomt2.name].remove(nomt1.name) #suppression de t1 dans les précédences de t2
                print("Supression de ",nomt1.name," dans les précédences de ",nomt2.name)
            else:
                print(nomt1.name,"n'est pas dans les précédences de", nomt2.name)
                break





"""dic
    vérifier pour chaque taches celles qui en possédent 2 

"""




class TaskSystem:  
    #classe TaskSystem
    def __init__(self,taches,dic): 
        self.taches = taches
        self.dic = dic
    
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
                    
    
    
    def paraMax(self):
        print("test paraMax //////////////////////////")
        print("le dictionnaire de précedence :",dic)
        afficheTaches(s1)
        
        print("vérification d'interference entre les taches et suppression des arcs non essentiel") 
        
        for tache in taches:
            for tache2 in taches:
                if(tache!=tache2):
                    SupprInter(tache,tache2)
                    ParaTache(tache,tache2)
        #for tache in taches:
            #redondances(tache)            

            




            


def redondances(nomt):
  
    CheminVisiter = []
    CheminActuelle = []
        
    s1.getDependencies(nomt)
    if(dic[nomt.name] == []): #si t n'a pas de precedences
        print("pas de redondance à éliminer car la tache n'a pas de  pas de précedence")
    else:
        for i in dic[nomt.name]:
            #tache en question
            #print("pour la tache",i,"voici une precedences")
            for j in dic.get(i):
                CheminActuelle.append(i)
                CheminActuelle.append(j)
                #precedences tache
                #print(j)

                while (dic.get(j) != []): #si t n'a pas de precedences
                    for k in dic.get(j):
                        #print("pour la tache",j,"voici une precedences")
                        #print(k)
                        CheminActuelle.append(k)
                        j = k
                        #print("nouvelle valeur de j:",j)
                        break
                CheminVisiter.append(CheminActuelle)
                #print("voila le chemin actuelle",CheminActuelle) 
                CheminActuelle = []
                #print("liste des chemins visiter",CheminVisiter)

        print("liste des chemins visiter",CheminVisiter)
            
 
        for x in dic[nomt.name]:
            #print(x)
            for y in CheminVisiter:
                if x in y :
                    #print(y)
                    for z in CheminVisiter:
                        if x in z:
                            if (z != y) :
                                if len(z) > len(y) :
                                    CheminVisiter.remove(y)
                                    y = z
                                    #print(z)
                                    print(CheminVisiter)
                                elif len(z) < len(y) :
                                    CheminVisiter.remove(z)
                                    print(CheminVisiter)
                break
    
        CheminPlusLong = CheminVisiter[0]
        print("chemin le plus long",CheminPlusLong)
        e = CheminPlusLong[0]
        print("le premier element",e)

        for s in dic[nomt.name]:
            if s != e:
                print("tache",s)
                if s in CheminPlusLong:
                    print(CheminPlusLong)
                    print(s)
                    dic[nomt.name].remove(s) #suppression de s dans les précédences de t
    
    s1.getDependencies(nomt)


        



        
def run(self):
    print("Début du run")
    
        
    

    l1 = taches #listes des taches du système pas encore éxécuté
    l2 = list() #liste des taches éxécutés
    lsp =list()# liste taches sans précédences
    for key, value in dic.items():
        if(not value):
            for t in taches:
                if(t.name==key):
                    lsp.append(t)#ajout des taches sans précédences dans la liste lsp
                    print("ajout de ",t.name, " dans lsp")
                    #print(lsp)
    #lsp2 = lsp
    
    #for tache in taches:
        #print("thread",tache.name)
        #th = threading.Thread(target = tache.run) 
        for tachesp in lsp:    
                th = threading.Thread(target = tachesp.run) 
                print("exécution de ",tachesp.name)
                l1.remove(tachesp)
                lsp.remove(tachesp)
                #afficheTaches(s1)
                l2.append(tachesp.name)
                #threadsp = threading.Thread(target = t.run)
                #threadsp.start()
                print(tachesp.name)
                th.start()
                print("fin",tachesp.name)

    while(l2 != taches):    
        for t in l1:# parcours de la liste des taches non éxécuté 
            check = all(item in l2 for item in dic[t.name])  #on vérifie si toutes les taches qui précédent la tache t sont éxécutés         
        if(check):  
            thread = threading.Thread(target = t.run)
            thread.start()
            l2.append(t.name)
            print(t.name)
            l1.remove(t)
            if(l1 == []):
                break 
            #afficheTaches(s1)
            #break
        else:
            print("toutes les précédences de ",t.name," ne sont pas encore éxécuté")
            print(dic[t.name])
            
            
            #for i in dic[t.name]: #parcours des précédences de t
            #for j in l2: #parcours des taches deja éxécutés
             
                   
                
                #on parcours toutes les taches pour trouver les taches deja exécutes dans les précédences 
                # on lance la tache seulement si l'ensemble de ses précédences appartient a liste des taches éxécutés L2
""""              
 
 for t in l1:# parcours de la liste des taches non éxécuté 
        #for i in dic[t.name]: #parcours des précédences 
            #for j in l2: #parcours des taches deja éxécutés
                #print(j.name)
 if(i == j.name):
    print("Lancement")
    thread.start()
    l2.append(t)
    print(t.name)
    l1.remove(t)
else:
    thread.join  
    """                
        
        
    
     
        

                
                
            
    
          
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

def afficheTaches(self): #affiche la liste des taches du système
    print("Liste des taches:")
    for t in taches:
        print(t.name)
    
        

    



#utilisation de la classe Task   
X = None
Y = None
Z = None
M = None
N = None
P = None
L = None

def runT1():
    global X
    X = 1
    print("éxécution de T1",X)

def runT2():
    global Y
    Y = 2
    print("éxécution de T2",Y)

def runT3():
    global M
    M = 3
    print("éxécution de T3",M)
    
def runT4():
    global P
    P = 6
    #time.sleep(5)
    print("éxécution de T4",P)

def runT5():
    global L
    L = 3
    print("éxécution de T5",L)

def runT6():
    global P
    P = 3
    print("éxécution de T6",P)
    
def runTsomme():
    global X, Y, Z
    Z = X + Y
    print("éxécution de tSomme",Z)

t1 = Task()
t1.name = "T1"
t1.writes = ["X"]
t1.run = runT1

t2 = Task()
t2.name = "T2"
t2.writes = ["Y"]
t2.run = runT2

t3 = Task()
t3.name = "T3"
t3.writes = ["X"]
t3.run = runT3

t4 = Task()
t4.name = "T4"
t4.writes = ["V"]
t4.run = runT4

t5 = Task()
t5.name = "T5"
t5.writes = ["V"]
t5.run = runT5

t6 = Task()
t6.name = "T6"
t6.writes = ["V"]
t6.run = runT6

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
taches.append(t4)
taches.append(t5)
taches.append(t6)

dic = {"somme":["T1","T2","T3"],"T1":["T5"],"T2":["T3", "T5"],"T3":["T4", "T5"],"T4":[], "T5":["T6"], "T6":[]}# le dictionnaire donne par l'utilisateurdicfinal={} #le dictionnaire donne par la parallelisation maximal 


s1 = TaskSystem(taches,dic)

#afficher l'ensemble des precédences des taches de 1
#for i in s1.taches:
    #s1.getDependencies(i)

#print(dic.keys())

#s1.getDependencies(t5)

#test = redondances(t6)
#print(test)
#runT1()

#print(dic)
#s1.paraMax()
#print(dic)
#redondances(tSomme)
#t4 = threading.Thread(target = runT4)
#t4.start()
#t4.join # attend que t4 se termine pour passer au prochain thread 

#t5 = threading.Thread(target = runT5)
#t5.start()
'''
t1 = threading.Thread(target = runT1)
t1.start()
#t4.join # attend que t4 se termine pour passer au prochain thread 

t2 = threading.Thread(target = runT2)
t2.start()

tSomme = threading.Thread(target = runTsomme)
tSomme.start()
'''
print(dic)
#run(s1)
s1.paraMax()
redondances(tSomme)
redondances(t1)
redondances(t2)
redondances(t3)
redondances(t4)
redondances(t5)
redondances(t6)
#run(s1)
print(dic)







#def bonus1()