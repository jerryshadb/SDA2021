__author__ = "Jeremias Shadbolt"
__copyright__ = "Antaa palaa ja käyttäkää"
__credits__ = __author__
__version__ = "1.0.1"


# Solita Dev Academy 2021:n kooditehtävän ratkaisu. README sisältää tehtävänannon kokonaisuudessaan. 
import json
from tkinter import *


# Tehtävä 1
# Funktio palauttaa listan hajautustauluja 
# names.json -tiedostosta. Hajautustaulut ovat järjestetty nimien määrän ('amount' -arvo) mukaan. 
def nimetMaaranMukaan():
    with open("solitadevtehtava/dev-academy-2021/names.json", 'r') as f:
        data = json.load(f)
        return sorted(data['names'],key=lambda k: k['amount'],reverse=True)
# Tehtävä 2
# Funktio palauttaa listan hajautustauluja järjestettynä aakkosjärjestykseen hajautustaulujen arvon 'name' -mukaan. 
# Sama kuin t1, mutta numerot vaihtuivat aakkosiksi. 
def nimetAakkostenMukaan():
    with open("solitadevtehtava/dev-academy-2021/names.json", 'r') as f:
        data = json.load(f)
        return sorted(data['names'],key=lambda k: k['name'])

# Tehtävä 3
# Palauttaa names.json -tiedoston hajautustaulujen 'amount' -arvojen summan.   
def nimienMäärä():
    with open("solitadevtehtava/dev-academy-2021/names.json", 'r') as f:
        data = json.load(f)    
        return (sum(x['amount']for x in data['names']))

# Tehtävä 4
# Etsii names.json -tiedoston hajautustaululistasta String-parametrina saamansa arvoa vastaavan nimen määrän.
# names -tiedoston arvot talletetaan listaan, luoden listan hajautustauluja (nimet). 
# nimet -lista iteroidaan läpi, etsien parametria vastaavaa arvoa. Jos sitä ei löydy, palauttaa funktio "virheviestin". 
# Luodaan toinen lista ans. Iteroidaan data jälleen läpi, verraten parametria sen (datan) arvoihin. 
# Mikäli osuma tulee, lisätään sen nimen arvo 'amount' listaan "ans" ja palautetaan ans:n 0:s arvo, eli haettu 'amount'-arvo. 
# Ratkaisu on ehkä vähän turhan bruteforce ja isompiin datamääriin siirryttäessä täysin käyttökelvoton, mutta tähän tehtävään varsin passeli. 
def nimiListasta(s):
    with open("solitadevtehtava/dev-academy-2021/names.json", 'r') as f:
        data = json.load(f)
        nimet = [x['name'] for x in data['names']]
        if s not in nimet:
            return "nolla. Viallinen syöte?"
        ans = [x['amount']for x in data['names']if s == x['name']]
        
    return ans[0]

#Tkinter graafinen käyttöliittymä
root = Tk()
root.geometry('700x500')
root.title("Solita DevAcademy2021:n kooditehtävä")

#Tehtävä 1
maara = Label(root, text = '')
maaraIntro = Label(root,text = "Työntekijöiden nimet määrän mukaan järjestettynä ")
maara['text'] = '\n'.join(f"{työntekijä['name']}, määrä: {työntekijä['amount']}" for työntekijä in nimetMaaranMukaan())

#Tehtävä 2
aakkosIntro = Label(root, text = "Työntekijöiden nimet aakkosjärjestyksessä ")
aakkos = Label(root, text = '')
aakkos['text'] = '\n'.join(f"{työntekijä['name']}" for työntekijä in nimetAakkostenMukaan())

#Tehtävä 3
summa = Label(root,text = f"Jengiä yhteensä: {nimienMäärä()}")

#Tehtävä 4
e = Entry(root)
nimenMukaan = Label(root, text = "Tulosta työntekijöiden määrä nimen mukaan: ")
henkilö = Label(root, text = '')    
#e.get() metodin palauttama String on pienennetty tulosteessa max 7 kirjaimeen, ettei ikkuna sekoa liian pitkästä syötteestä.
#Todellisuudessahan tällaisia ei voisi tehdä, mutta sopii tehtävänantoon varsin mainiosti, sillä etsimme vain etunimillä.
#Pisin etunimi listassa on "Tuomas" joka on 6 merkkiä eli käyttäjä, mikäli etsii ei-pelleillen, ei edes huomaa mitään. 
#
b = Button(root, text = "Tulosta", command = lambda: henkilö.config(text = f"Henkilöitä {e.get()[:7]} on {nimiListasta(e.get())}"))



#Sälän asettelu ikkunaan
maaraIntro.grid(row = 1, column = 0)
maara.grid(row = 2, column = 0)

aakkosIntro.grid(row = 1, column = 1)
aakkos.grid(row = 2, column = 1)

summa.grid(row = 23, column = 0)

nimenMukaan.grid(row = 22, column = 0)
e.grid(row = 22, column = 1)
henkilö.grid(row = 23, column = 1, columnspan = 1)
b.grid(row = 22, column = 2)

#Ikkunan luonti ja ohjelman ajo
root.mainloop()
