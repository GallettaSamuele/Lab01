# risolvere trivia game
import random
FILE_DOMANDE="domande.txt"
FILE_PUNTEGGIO="punti.txt"

class Domanda:
    def __init__ (self, domanda, livello, risposte, corretta):
        self.domanda = domanda
        self.livello = livello
        self.risposte = risposte
        self.corretta = corretta

    def mescola_risposte(self):
        random.shuffle(self.risposte)

    def valuta_risposta(self, risposta):
        if risposta == self.corretta:
            return True
        else:
            return False

class Giocatore:
    def __init__ (self, nome, punteggio):
        self.nome = nome
        self.punteggio = punteggio

    def aggiorna_punteggio(self):
        self.punteggio += 1


def leggi_domande(nomefile):
    domande = []
    with open(nomefile, "r", encoding="utf-8") as file:
        lista=[]
        for line in file:
            line=line.rstrip("\n")
            lista.append(line)
    for i in range(0, len(lista), 7):
        risposte=lista[i+2:i+6]
        corretta=lista[i+2]
        domanda = Domanda(lista[i], int(lista[i+1]), risposte, corretta)
        domanda.mescola_risposte()
        domande.append(domanda)
    return domande

def leggi_punteggio(nomefile):
    giocatori=[]
    diz={}
    with open(nomefile, "r", encoding="utf-8") as file:
        for line in file:
            line=line.rstrip("\n")
            lista=line.split(" ")
            giocatore= Giocatore(lista[0], int(lista[1]))
            giocatori.append(giocatore)
            diz[lista[0]]=giocatore.punteggio
        return diz

def aggiorna_punteggio(dizionario, nome, punteggio):
    if dizionario.get(nome) != None:
        dizionario[nome] = dizionario[nome] + punteggio
    else:
        dizionario[nome] = punteggio

def aggiorna_file(nomefile, dizionario):
    with open(nomefile, "w", encoding="utf-8") as file:
        for nome in dizionario:
            file.write(f"{nome} {dizionario[nome]}\n")

def Main():
    c=True
    liv = 0
    punteggio = 0
    dizionario = leggi_punteggio(FILE_PUNTEGGIO)
    domande = leggi_domande(FILE_DOMANDE)
    while  c==True :
        lista = []
        for j in range(0, len(domande)):
            if domande[j].livello == liv:
                lista.append(domande[j])
        if len(lista)==0:
            print("Raggiunto il livello massimo")
            nome = input("Inserisci il nome: ")
            aggiorna_punteggio(dizionario, nome, punteggio)
            break
        random.shuffle(lista)
        domanda=lista[random.randint(0, (len(lista)-1))]
        diz={"A":domanda.risposte[0], "B":domanda.risposte[1], "C":domanda.risposte[2], "D":domanda.risposte[3]}
        print(f"Livello {liv}) {domanda.domanda}")
        print(f"A: {diz["A"]}\nB: {diz["B"]}\nC: {diz["C"]}\nD: {diz["D"]}")
        s=input("Inserisci la risposta:  ")
        s=s.upper()
        if diz.get(s)!=None and diz[s] == domanda.corretta:
            print("Risposta corretta!")
            print("")
            liv=liv+1
            punteggio=punteggio+1
            c=True
        else:
            c=False
            print(f"Risposta errata! La risposta corretta era:d {domanda.corretta}")
            print("")
            nome = input("Inserisci il nome: ")
            aggiorna_punteggio(dizionario, nome, punteggio)
    dizionario_ordinato=dict(sorted(dizionario.items(), key=lambda item: item[1], reverse=True))
    print(dizionario_ordinato)
    aggiorna_file(FILE_PUNTEGGIO, dizionario_ordinato)
    print("hello word")
Main()