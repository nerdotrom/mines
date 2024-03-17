#Radim Tesner, P1B
'''Klasická hra Minesweeper, v česku známa pod názvem Miny. Po spuštění užvatel klikne do mřížky a odhalí tak základní pole. Čísla v jednotlivých buňkách představují počet min kolem ní. Pokud uživatel klikne na minu,
prohrál, když klikne na všechna políčka kromě těch na kterých jsou miny vyhrává. Na pravém tlačítku myši má uživatel pomůcku kterou může buńku označit pokud si myslí že je pod ní mina.
Buňka nepůjde odhalit dokud uživatel neklikne znovu levým tlčítekm.'''

import tkinter as tk
import random
import copy

#parametry
pocet_radku = 15
pocet_sloupcu = 15
pocet_bomb = 60
prvni_projiti = True
prohra = False
vyhra = False
vyhral_jsi = False

def znovu_p():
  global znovu, prvni_projiti, prohra, mrizka, zmacknuta_tlacitka
  znovu = False
  konec_okno.destroy()
  prvni_projiti = True
  prohra = False
  mrizka = []
  zmacknuta_tlacitka = 0
def znovu_v():
  global znovu, prvni_projiti, prohra, mrizka, zmacknuta_tlacitka
  znovu = False
  vyhra_okno.destroy()
  prvni_projiti = True
  prohra = False
  mrizka = []
  zmacknuta_tlacitka = 0
def znovu_o():
  global znovu, prvni_projiti, prohra, mrizka, zmacknuta_tlacitka
  znovu = False
  obraz.destroy()
  prvni_projiti = True
  prohra = False
  mrizka = []
  zmacknuta_tlacitka = 0
def ukonci_se_p():
  global znovu
  konec_okno.destroy()
  znovu = True
def ukonci_se_v():
  global znovu
  vyhra_okno.destroy()
  znovu = True

def vypis_mrizku(mrizka: list):
  for i in mrizka:
    print(i)  
  
def zmacknuti(radek: int, sloupec: int):
  global mrizka, prvni_projiti, tlac_mriz, prohra, zmacknuta_tlacitka, vyhra, mrizka_pomocna, vyhral_jsi
  if prvni_projiti:
    prvni_projiti = False
    if mrizka[radek][sloupec] == "x":
      mrizka[radek][sloupec] = 0
    if mrizka[radek - 1][sloupec - 1] == "x":
      mrizka[radek - 1][sloupec - 1] = 0
    if mrizka[radek - 1][sloupec] == "x":
      mrizka[radek - 1][sloupec] = 0
    if mrizka[radek - 1][sloupec + 1] == "x": 
      mrizka[radek - 1][sloupec + 1] = 0
    if mrizka[radek][sloupec + 1] == "x":
      mrizka[radek][sloupec + 1] = 0
    if mrizka[radek + 1][sloupec + 1] == "x":
      mrizka[radek + 1][sloupec + 1] = 0
    if mrizka[radek + 1][sloupec] == "x":
      mrizka[radek + 1][sloupec] = 0
    if mrizka[radek + 1][sloupec - 1] == "x":
      mrizka[radek + 1][sloupec - 1] = 0
    if mrizka[radek][sloupec - 1] == "x":
      mrizka[radek][sloupec - 1] = 0

    for i in range(radek - 2, radek + 3):
      for j in range(sloupec - 2, sloupec + 3):
        if i > 0 and j > 0 and i < pocet_radku - 1 and j < pocet_sloupcu -1:
          spocitat_bomby(i, j)          
          
    tlac_mriz[radek + 1][sloupec + 1]["text"] = mrizka[radek + 1][sloupec + 1]
    mrizka_pomocna[radek + 1][sloupec + 1] = "."
    tlac_mriz[radek + 1][sloupec]["text"] = mrizka[radek + 1][sloupec]
    mrizka_pomocna[radek + 1][sloupec] = "."
    tlac_mriz[radek][sloupec + 1]["text"] = mrizka[radek][sloupec + 1]
    mrizka_pomocna[radek][sloupec + 1] = "."
    tlac_mriz[radek - 1][sloupec + 1]["text"] = mrizka[radek - 1][sloupec + 1]
    mrizka_pomocna[radek - 1][sloupec + 1] = "."
    tlac_mriz[radek + 1][sloupec - 1]["text"] = mrizka[radek + 1][sloupec - 1]
    mrizka_pomocna[radek + 1][sloupec - 1] = "."
    tlac_mriz[radek - 1][sloupec]["text"] = mrizka[radek - 1][sloupec]
    mrizka_pomocna[radek - 1][sloupec] = "."
    tlac_mriz[radek][sloupec - 1]["text"] = mrizka[radek][sloupec - 1]
    mrizka_pomocna[radek][sloupec - 1] = "."
    tlac_mriz[radek - 1][sloupec - 1]["text"] = mrizka[radek - 1][sloupec - 1]
    mrizka_pomocna[radek - 1][sloupec - 1] = "."
    tlac_mriz[radek][sloupec]["text"] = mrizka[radek][sloupec]
    mrizka_pomocna[radek][sloupec] = "."
    
  elif tlac_mriz[radek][sloupec]["bg"] == "red":
    pass
    
  else:

    if mrizka[radek][sloupec] == "x":
      prohra = True
      obraz.destroy()
    else:
      tlac_mriz[radek][sloupec]["text"] = mrizka[radek][sloupec]
      mrizka_pomocna[radek][sloupec] = "."
      for i in range(pocet_radku):
        for j in range(pocet_sloupcu):
          if mrizka_pomocna[i][j] != "x" and mrizka_pomocna[i][j] != ".":
            return
      else:
        obraz.destroy()
        vyhra = True

def vlajka(radek, sloupec):
  global tlac_mriz
  if tlac_mriz[radek][sloupec]["text"] == "	":
    if tlac_mriz[radek][sloupec]["bg"] == "light green":
      tlac_mriz[radek][sloupec]["bg"] = "red"
    elif tlac_mriz[radek][sloupec]["bg"] == "red":
      tlac_mriz[radek][sloupec]["bg"] = "light green"
  elif tlac_mriz[radek][sloupec]["bg"] == "red":
    tlac_mriz[radek][sloupec]["bg"] = "light green"
    
def spocitat_bomby(radek, sloupec):
  global mrizka
  bomby_kolem = 0
  if mrizka[radek][sloupec] == "x": #střed
    return
  
  elif radek == 0 and sloupec == 0: #levý horní roh
    if mrizka[radek][sloupec+1] == "x":
      bomby_kolem += 1
    if mrizka[radek+1][sloupec+1] == "x":
      bomby_kolem += 1
    if mrizka[radek+1][sloupec] == "x":
      bomby_kolem += 1
    if mrizka[radek+1][sloupec] == "x":
      bomby_kolem += 1

  elif radek == 0 and sloupec != 0 and sloupec != pocet_sloupcu - 1: #horní řádek
    if mrizka[radek][sloupec-1] == "x":
      bomby_kolem += 1
    if mrizka[radek][sloupec+1] == "x":
      bomby_kolem += 1          
    if mrizka[radek+1][sloupec+1] == "x":
      bomby_kolem += 1  
    if mrizka[radek+1][sloupec-1] == "x":
      bomby_kolem += 1   
    if mrizka[radek+1][sloupec] == "x":
      bomby_kolem += 1
      
  elif radek == 0 and sloupec == pocet_sloupcu - 1: #pravý horní roh
    if mrizka[radek][sloupec-1] == "x":
      bomby_kolem += 1
    if mrizka[radek+1][sloupec-1] == "x":
      bomby_kolem += 1
    if mrizka[radek+1][sloupec] == "x":
      bomby_kolem += 1
      
  elif radek != 0 and sloupec == pocet_sloupcu - 1 and radek != pocet_radku - 1: #pravý sloupec
    if mrizka[radek-1][sloupec] == "x":
      bomby_kolem += 1
    if mrizka[radek-1][sloupec-1] == "x":
      bomby_kolem += 1
    if mrizka[radek][sloupec-1] == "x":
      bomby_kolem += 1
    if mrizka[radek+1][sloupec-1] == "x":
      bomby_kolem += 1
    if mrizka[radek+1][sloupec] == "x":
      bomby_kolem += 1

  elif radek == pocet_radku - 1 and sloupec == pocet_sloupcu - 1: #pravý dolní roh
    if mrizka[radek-1][sloupec] == "x":
      bomby_kolem += 1
    if mrizka[radek-1][sloupec-1] == "x":
      bomby_kolem += 1
    if mrizka[radek][sloupec-1] == "x":
      bomby_kolem += 1

  elif sloupec != 0 and sloupec != pocet_sloupcu - 1 and radek == pocet_radku - 1: #spodní řádek
    if mrizka[radek][sloupec-1] == "x":
      bomby_kolem += 1
    if mrizka[radek-1][sloupec-1] == "x":
      bomby_kolem += 1
    if mrizka[radek-1][sloupec] == "x":
      bomby_kolem += 1
    if mrizka[radek-1][sloupec+1] == "x":
      bomby_kolem += 1
    if mrizka[radek][sloupec+1] == "x":
      bomby_kolem += 1
      
  elif radek == pocet_radku - 1 and sloupec == 0: #levý dolní roh
    if mrizka[radek-1][sloupec] == "x":
      bomby_kolem += 1  
    if mrizka[radek-1][sloupec+1] == "x":
      bomby_kolem += 1
    if mrizka[radek][sloupec+1] == "x":
      bomby_kolem += 1

  elif radek != 0 and sloupec == 0 and radek != pocet_radku - 1: #levý sloupec    
    if mrizka[radek-1][sloupec] == "x":
      bomby_kolem += 1
    if mrizka[radek-1][sloupec+1] == "x":
      bomby_kolem += 1  
    if mrizka[radek][sloupec+1] == "x":
      bomby_kolem += 1
    if mrizka[radek+1][sloupec+1] == "x":
      bomby_kolem += 1  
    if mrizka[radek+1][sloupec] == "x":
      bomby_kolem += 1
  else:    
    if mrizka[radek-1][sloupec-1] == "x":
      bomby_kolem += 1
    if mrizka[radek-1][sloupec] == "x":
      bomby_kolem += 1
    if mrizka[radek-1][sloupec+1] == "x":
      bomby_kolem += 1
    if mrizka[radek][sloupec+1] == "x":
      bomby_kolem += 1
    if mrizka[radek+1][sloupec+1] == "x":
      bomby_kolem += 1
    if mrizka[radek+1][sloupec] == "x":
      bomby_kolem += 1
    if mrizka[radek+1][sloupec-1] == "x":
      bomby_kolem += 1
    if mrizka[radek][sloupec-1] == "x":
      bomby_kolem += 1
      
  mrizka[radek][sloupec] = bomby_kolem 

while True:
  znovu = True
  mrizka = []
  sloupce = []
  for j in range(0, pocet_sloupcu): #generace mrizky 
      sloupce.append(0)
  for i in range (0, pocet_radku):
      mrizka.append(sloupce.copy())  
  for i in range(pocet_bomb): #generace bomb
      radek = random.randint(0,pocet_radku - 1)
      sloupec = random.randint(0,pocet_sloupcu - 1)

      mrizka[radek][sloupec] = "x"
  for radek in range(pocet_radku):#pocitani bomb
    for sloupec in range(pocet_sloupcu):
      spocitat_bomby(radek, sloupec)

  mrizka_pomocna = copy.deepcopy(mrizka)

  obraz = tk.Tk()
  obraz.geometry("1920x1080")
  obraz.title("Minesweeper")
  mrizkatalcitek = tk.Frame(obraz)
  obraz.config(background = "black")

  nadpis = tk.Label(obraz, text="Minesweeper", bg = "Black",fg="white", font=("Times New Roman", 50, "bold"))
  nadpis.pack(padx=10, pady=30)

  for sloupec in range(0, pocet_sloupcu):
    mrizkatalcitek.columnconfigure(sloupec,weight=1)

  tlac_mriz = []
  for radek in range(pocet_radku):
    tlac_radek = []
    for sloupec in range(pocet_sloupcu):
      tlac = tk.Button(mrizkatalcitek, bg="light green", text="	" , font=("Times New Roman", 18, "bold"), command=lambda r=radek, s=sloupec: zmacknuti(r,s))
      tlac.bind("<Button-3>",lambda udalost, r=radek, s=sloupec: vlajka(r,s))
      tlac_radek.append(tlac)
      tlac.grid(row=radek, column=sloupec, sticky=tk.W + tk.E)
    tlac_mriz.append(tlac_radek)
  
  mrizkatalcitek.pack(fill="x", pady=10)
  znovu_tlac = tk.Button (obraz, bg="light green", text="Hrát znovu" , font=("Times New Roman", 18, "bold"), command=znovu_o)
  znovu_tlac.pack()
  obraz.mainloop()

  if prohra:
    konec_okno = tk.Tk()
    konec_okno.geometry("500x250")
    konec_okno.title("Konec hry")
    konec_okno.config(background = "black")
    
    hlaska = tk.Label(konec_okno, text="Klikl jsi na bombu a prohrál", bg = "Black",fg="white", font=("Times New Roman", 20, "bold"))
    hlaska.pack(padx=10, pady=20)
    odchod_tlac = tk.Button (master = konec_okno, bg="light green", text="Odejít" , font=("Times New Roman", 18, "bold"), command=ukonci_se_p)
    znovu_tlac = tk.Button (master = konec_okno, bg="light green", text="Hrát znovu" , font=("Times New Roman", 18, "bold"), command=znovu_p)
    odchod_tlac.pack(pady=10)
    znovu_tlac.pack()

    konec_okno.mainloop()
  if vyhra:
    vyhra_okno = tk.Tk()
    vyhra_okno.geometry("800x400")
    vyhra_okno.title("Vyhral jsi")
    vyhra_okno.config(background = "black")
    
    hlaska = tk.Label(vyhra_okno, text="Neklikl jsi na jedinou minu a vyhrál. Gratuluji", bg = "Black",fg="white", font=("Times New Roman", 20, "bold"))
    hlaska.pack(padx=10, pady=20)
    odchod_tlac = tk.Button (master = vyhra_okno, bg="light green", text="Odejít" , font=("Times New Roman", 18, "bold"), command=ukonci_se_v)
    znovu_tlac = tk.Button (master = vyhra_okno, bg="light green", text="Hrát znovu" , font=("Times New Roman", 18, "bold"), command=znovu_v)
    odchod_tlac.pack(pady=10)
    znovu_tlac.pack()
  
    vyhra_okno.mainloop()
  if znovu:
    break