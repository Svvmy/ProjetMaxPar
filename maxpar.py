import time
from unicodedata import name
import threading

# le package graphviz permet de représenter des diagrammes et graphes à partie d'informations
import graphviz

class Task: #classe pour la déclaration d'une tache 
    name = ""
    reads = []
    writes = []
    run = None


def bernstein(t1,t2):# fonction qui prend deux taches qui renvoie false si il y a une intérférence entre les taches
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


def SupprInter(nomt1,nomt2): #Fonction de suppression d'interférence qui prend deux taches en parametres 
    if not bernstein(nomt1, nomt2):#vérifie s'il y a une interferance 
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
            
    else:
        print("Aucune interferance entre les deux taches "+nomt1.name+ " et " +nomt2.name)
        return True
        
        

def ParaTache(nomt1,nomt2):#Paralléliser les taches qui n'ont pas d'interférences 
    if bernstein(nomt1, nomt2):# s'il n'y a pas d'interférance
        for i in dic[nomt2.name]:
            if(i == nomt1.name):
                dic[nomt2.name].remove(nomt1.name) #suppression de t1 dans les précédences de t2
                print("Supression de ",nomt1.name," dans les précédences de ",nomt2.name)
            else:
                print(nomt1.name,"n'est pas dans les précédences de", nomt2.name)
                break



class TaskSystem:  
    
    
    def __init__(self,taches,dic): 
        self.taches = taches
        self.dic = dic
    
    
    def getDependencies(self,nomTache): #donne la liste des taches qui s'éxécute avant une tache donné
        if(dic[nomTache.name] == []): #si la tache ne possède pas de précedence
             print("La tache "+nomTache.name+ " n'a pas de précédence")
        else:
            for value in dic[nomTache.name]:
                if(not value == ""):
                    print("Les précédences de la tache " + nomTache.name+ " sont", dic[nomTache.name])
                    return dic[nomTache.name]
                
    
    
    def paraMax(self):
        print("------------------------------------- Parallèlisation maximal -------------------------------------")
        print("le dictionnaire de précedence :",dic)
        print("")
        afficheTaches(s1)
        print("")
        print("vérification d'interference entre les taches et suppression des arcs non essentiel") 
        print("")
        for tache in taches:
            for tache2 in taches:
                if(tache!=tache2):
                    SupprInter(tache,tache2)
                    ParaTache(tache,tache2)
        #redondances(tache)  ici la fonction de redondances ne fonctionne pas dans le for
        #Mais fonctionne pour une tache passé en parametre
        # nous n'avons pas eu le temps de corriger ce problème        


def redondances(nomt):
  
    CheminVisiter = []
    CheminActuelle = []
        
    s1.getDependencies(nomt)
    if(dic[nomt.name] == []): #si t n'a pas de precedences
        print("pas de redondance à éliminer car la tache n'a pas de  pas de précedence")
    else:
        for i in dic[nomt.name]:
            #tache en question

            for j in dic.get(i):
                CheminActuelle.append(i)
                CheminActuelle.append(j)
                #precedences de tache
               

                while (dic.get(j) != []): #si t n'a pas de precedences
                    for k in dic.get(j):
                        
                        CheminActuelle.append(k)
                        j = k
                        
                        break
                CheminVisiter.append(CheminActuelle)
             
                CheminActuelle = []
         

        print("liste des chemins visiter",CheminVisiter)
            
 #permet de reduire la liste des chemins visiter a seulement le chemin le plus long
        for x in dic[nomt.name]:
            for y in CheminVisiter:
                if x in y :
                    for z in CheminVisiter:
                        if x in z:
                            if (z != y) :
                                if len(z) > len(y) :
                                    CheminVisiter.remove(y)
                                    y = z
                                    print(CheminVisiter)
                                elif len(z) < len(y) :
                                    CheminVisiter.remove(z)
                                    print(CheminVisiter)
                break
    
        CheminPlusLong = CheminVisiter[0]
        print("chemin le plus long",CheminPlusLong)
        e = CheminPlusLong[0]
        print("le premier element",e)

#élimination de redondance
        for s in dic[nomt.name]:
            if s != e:
                print("tache",s)
                if s in CheminPlusLong:
                    print(CheminPlusLong)
                    print(s)
                    dic[nomt.name].remove(s) #suppression de s dans les précédences de t
    #nouvelle precedence
    s1.getDependencies(nomt)


#graphviz doit etre importer dans python et doit se trouver dans les liens du path
"""bonus2"""             
def draw(dic):
    g = graphviz.Digraph( name='maxparGraph')
    for i in dic:
        for j in dic.get(i):
            #la fleche ira de j a i
            g.edge(j,i)
    g.view()    

        
def run(self):
    print("------------------------------------ Début du run -------------------------------------")
    l1 = taches #listes des taches du système pas encore exécuté
    l2 = list() #liste des taches exécutés
    lsp =list()# liste des taches sans précédences
    for key, value in dic.items():
        if(not value):
            for t in taches:
                if(t.name==key):
                    lsp.append(t)#ajout des taches sans précédences dans la liste lsp
                    
                
        for tachesp in lsp:    
                th = threading.Thread(target = tachesp.run) 
                l1.remove(tachesp)
                lsp.remove(tachesp)
                l2.append(tachesp.name)
                th.start()
                print("fin",tachesp.name)

    while(l2 != taches):    
        for t in l1:# parcours de la liste des taches non éxécuté 
            check = all(item in l2 for item in dic[t.name])  #on vérifie si toutes les taches qui précédent la tache t sont exécutés         
        if(check):  
            thread = threading.Thread(target = t.run)
            thread.start()
            l2.append(t.name)
            l1.remove(t)
            if(l1 == []):
                break 
            
        else:
            print("toutes les précédences de ",t.name," ne sont pas encore éxécuté")
            print(dic[t.name])
            
                   
                
                #on parcours toutes les taches pour trouver les taches deja exécutés dans les précédences 
                #on lance la tache seulement si l'ensemble de ses précédences appartient à la liste des taches exécutés L2
             

def bonus1(taches,dic): #validation
    res = True
    if(len(taches) == len(set(taches))):
        res =True
    else:
        print("La liste des taches contient des taches dupliqées")
        return False
    
    if(len(taches)==0): #verifie si la liste des taches est vide
        print("la liste des taches est vide")
        return False
    else:
        res = True
        
    for t in taches:
        if(t.run==None): #vérifier si les tâches dans la liste ne contiennt pas de méthode run
            print("une ou plusieurs tâches dans la liste ne contiennt pas de méthode run pour l'exécuter ")
            return False

    for i in range(len(taches)): #vérifier si la liste des tâches contient des nom de tâches dupliqués
        for j in range(i+1,len(taches)):
            if(taches[i].name==taches[j].name):
             print("la liste des tâches contient des nom de tâches dupliqués" )
             return False
        
    
        


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
    global N
    N = 3
    print("éxécution de T6",N)
    
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

#liste des taches
taches = list()

#ajouter les tâches à la liste de taches
taches.append(tSomme)
taches.append(t1)
taches.append(t2)
taches.append(t3)
taches.append(t4)
#taches.append(t5)
taches.append(t6)

dic = {"somme":["T1","T2","T3","T4"],"T1":["T4"],"T2":["T3", "T4"],"T3":["T4"],"T4":[],"T6":[]} # le dictionnaire donné par l'utilisateur


s1 = TaskSystem(taches,dic)

#afficher l'ensemble des precédences des taches de 1
#for i in s1.taches:
    #s1.getDependencies(i)
   
#fonction qui permet la parallèlisation maximal automatique du système s1
s1.paraMax()

#la fonction de redondance marche mais seulement pour les taches en precedence de tsomme en plus de t somme nous n 'arrivons pas a la lancer dans run
#cependant elle fonctionne tres bien pour les taches qu'elles run
redondances(tSomme)
redondances(t1)
redondances(t2)
redondances(t4)

#affichage du dictionnaire après la parallèlisation maximal
print("")
print("Dictionnaire final: ",dic)

# fonction qui permet de lancer les taches qui peuvent etre parallélisé 
run(s1)


#appelle la fonction pour dessiner le graph
draw(dic)