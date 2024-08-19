# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:09:31 2020

@author: stephan.fuchs

"""
from platform import machine
import sys
import os
sys.path.insert(0, "..")
import datetime
import time
import random
from random import randrange
import math



Erstelle_Lookup=False


try: 
    kunden=int(sys.argv[1])     #Anzahl der Sekunden wie lange das Skript laufen soll 
except:
    kunden=10

def zufalls_ip():
    #return str(np.random.randint(255, size=1)[0])+"."+str(np.random.randint(255, size=1)[0])+"."+str(np.random.randint(255, size=1)[0])+"."+str(np.random.randint(255, size=1)[0])
    return str(randrange(1,255,1))+"."+str(randrange(1,255,1))+"."+str(randrange(1,255,1))+"."+str(randrange(1,255,1))


def write_logs(file,line): # Input ist hier dictonary
        #write out the event, open and close the file each time for proper tailing
        #Time= datetime.datetime.fromtimestamp(int(Zeitpunkt)).strftime('%Y-%m-%d %H:%M:%S')
        output_file = open(file, 'a')
        for column in line.values():
            output_file.write(str(column)+",")
        output_file.write(str("\n"))
        output_file.close()
  

def write_logs_array(file,array): # Input ist hier Array
        #write out the event, open and close the file each time for proper tailing
        #Time= datetime.datetime.fromtimestamp(int(Zeitpunkt)).strftime('%Y-%m-%d %H:%M:%S')
        output_file = open(file, 'a')
        for value in array:
            output_file.write(str(value)+",")
        output_file.write(str("\n"))
        output_file.close()  
        
def aufaddieren(arr):
    zwi=[]
    a=0
    for i in arr:
        a=i+a
        zwi.append(a)
    ##print("zwi",zwi)
    return zwi

def erstelle_lookup(erste_spalte,dictionary,dateiname): # erstellt lookups aus dictionarys
    output_file = open(dateiname, 'w')
    a=next(iter(dictionary.values())) #beispiel Values
    header=erste_spalte+","
    for spalte in a.keys():
        header=header+spalte+","
    #print(header)
    output_file.write(header+"\n")

    for keys in dictionary.keys():
        output_file.write(str(keys)+",")
        for werte in dictionary[keys].values():
            output_file.write(str(werte)+",")
        output_file.write("\n")
    
    output_file.close()
    
    
def statistik_funktion(wahrscheinlichkeiten,auswahl):
    zufalls_zahl=random.random()
    wahr_arr=wahrscheinlichkeiten[:]  
    wahr_arr.insert(0,0)
    wahr_arr_zwi=aufaddieren(wahr_arr)
    wahr_arr_zwi[-1]=1.0
    ausgabe_i=0
    ##print("Wahr_arr",wahr_arr,"Wahr_arr_zwi",wahr_arr_zwi,"Auswahl",auswahl)
    for i in range(len(wahr_arr)-1):
        ##print(i,zufalls_zahl,wahr_arr_zwi[i])
        if (zufalls_zahl>wahr_arr_zwi[i]) and (zufalls_zahl<wahr_arr_zwi[i+1]):
            ##print("Bin drin",auswahl[i])
            ausgabe_i=auswahl[i]
    return ausgabe_i

def wichtigkeit(arr):
    Prio=[i["Prio"] for i in arr]
    #print("Prio",Prio)
    laenge=sum(Prio)
    ausgabe=[i/laenge for i in Prio]
    #print("Ausgabe",ausgabe)
    return ausgabe


def auftrag(kunden_arr,verhaltnis_auftrage):
    Eintrag=statistik_funktion(verhaltnis_auftrage,kunden_arr)
    ##print("Eintrag",Eintrag)
    kunde=Eintrag["Kunde"]
    Produkt=statistik_funktion(Eintrag["P_Produkt"],Eintrag["Produkte"])
    Holz=   statistik_funktion(Eintrag["P_Holzart"],Eintrag["Holzart"])
    return [kunde,Produkt,Holz]


def prozess_ablauf(auftragsnummer,zeitstempel,maschine,Lager):
    
    file="Prozesskette.csv" #Zeit, Auftragsnummer, Prozesschritt, Maschine
    bohrer=    random.choice(["Bohrer_1","Bohrer_2","Bohrer_3","Bohrer_4"])
    politur=   random.choice(["Politur_1","Politur_2","Politur_3"])
    verpackung=random.choice(["Verpackung_1","Verpackung_2","Verpackung_3","Verpackung_4","Verpackung_5"])
    Lager_Wahl=random.choice([0,1,2,3])
    Lager_Namen=["Lagerhalle_1","Lagerhalle_2","Lagerhalle_3","Lagerhalle_4"]
    
    # Wenn Lager voll ist
    if Lager[Lager_Wahl]>10:
        Lager[Lager_Wahl]=1

    write_logs_array(file,[zeitstempel                            ,auftragsnummer,maschine,])
    write_logs_array(file,[zeitstempel+round(random.gauss(10,3),2),auftragsnummer,bohrer,])
    write_logs_array(file,[zeitstempel+round(random.gauss(20,3),2),auftragsnummer,politur,])
    write_logs_array(file,[zeitstempel+round(random.gauss(40,5),2),auftragsnummer,verpackung,])
    write_logs_array(file,[zeitstempel+round(random.gauss(60,5),2),auftragsnummer,Lager_Namen[Lager_Wahl],Lager[Lager_Wahl]])


    Lager[Lager_Wahl]=Lager[Lager_Wahl]+1
    
    return Lager

def Zufallszahlen(start,abweichung):
    #ausgabe=start+num_ra.normal(0,abweichung)    
    ausgabe=start+random.gauss(0,abweichung)
    return round(ausgabe,2)

# Um den Wasserdruck der Hauptpumpe zu simulieren, inklusive Störungen
def temperatur_ausreisser(x): 
    #x=x/30. # hoehere Zeitauflösung
    periode=random.randrange(20,50,1)
    #print(x,x%periode,periode)
    laenge_ausbrauch=3
    if (x%periode<laenge_ausbrauch):
        Temp=random.gauss(30,10)  
        #print("Wasserausreißer")
    else:
        Temp=random.gauss(30,1)
    return Temp


def maschinen_daten_schreiben(Zeitstempel,Mitarbeiter,Halle,Maschine,i):
    
    if Maschine=="alpha":
        Temp= round(10*math.sin(0.4*i)+random.gauss(42,1),2)
        Strom=  round(10*math.sin(0.2*i)+random.gauss(10,1),3)
        if Zeitstempel%60<2:
            Temp=Temp+random.gauss(60,10)
    if Maschine=="beta":
        Temp= round(11*math.sin(0.45*i)+random.gauss(40,1),2)
        Strom=    round(20*math.sin(0.15*i)+random.gauss(10,1),3)  
        if Zeitstempel%50<2:
            Temp=Temp+random.gauss(50,10)  
    if Maschine=="gamma":
        Temp= round(9*math.sin(0.35*i)+random.gauss(38,1),2)
        Strom=    round(40*math.sin(0.25*i)+random.gauss(10,1),3)
        if Zeitstempel%70<2:
            Temp=Temp+random.gauss(70,10)

    #maschinendaten={"Zeitstempel":Zeitstempel,"Halle":Halle,"Messwert":Halle+"."+Maschine+".Temperatur","Temperatur":str(Temp)}
    write_logs_array(file_metrics,[Zeitstempel,Mitarbeiter,Halle+"."+Maschine+".Temperatur",str(Temp)])

    #maschinendaten={"Zeitstempel":Zeitstempel,"Halle":Halle,"Messwert":Halle+"."+Maschine+".Strom","Strom":str(Strom)}
    write_logs_array(file_metrics,[Zeitstempel,Mitarbeiter,Halle+"."+Maschine+".Strom",str(Strom)])

    #print("Temperatur",Temp,"Strom",Strom,"Halle",Halle,"Maschine",Maschine)
    return Temp,Strom


def maschinen_daten_schreiben_aussen(Zeitstempel,i,Wasserdruck,Sensehat_Vorhanden):
    Luftdruck=     round(random.gauss(1012,0.8),2)
    Aussentemp=    round(math.sin(0.02*i)+random.gauss(17.4,0.3),1)
    Feuchtigkeit=  round(random.gauss(51,0.6),1)
    Wasserdruck=   round(temperatur_ausreisser(i),3)    

        
   # maschinendaten={"Zeitstempel":Zeitstempel,"Halle":"Aussenbereich","Messwert":"Aussenbereich.Aussentemperatur","Temperatur":str(Aussentemp)}
    #write_logs(file_metrics,maschinendaten)
    write_logs_array(file_metrics,[Zeitstempel,"Emilia","Aussenbereich.Aussentemperatur",str(Aussentemp)])
    
   # maschinendaten={"Zeitstempel":Zeitstempel,"Halle":"Aussenbereich","Messwert":"Aussenbereich.Luftfeuchtigkeit","Luftfeuchtigkeit":str(Feuchtigkeit)}
    write_logs_array(file_metrics,[Zeitstempel,"Emilia","Aussenbereich.Luftfeuchtigkeit",str(Feuchtigkeit)])
    
    #maschinendaten={"Zeitstempel":Zeitstempel,"Halle":"Aussenbereich","Messwert":"Aussenbereich.Luftdruck","Luftdruck":str(Luftdruck)}
    write_logs_array(file_metrics,[Zeitstempel,"Emilia","Aussenbereich.Luftdruck",str(Luftdruck)])
    
    #maschinendaten={"Zeitstempel":Zeitstempel,"Halle":"Aussenbereich","Messwert":"Aussenbereich.Wasserdruck","Wasserdruck":str(Wasserdruck)}
    write_logs_array(file_metrics,[Zeitstempel,"Emilia","Aussenbereich.Wasserdruck",str(Wasserdruck)])
    
    #print("Aussentemp,Feuchtigkeit,Luftdruck,Wasserdruck",Aussentemp,Feuchtigkeit,Luftdruck,Wasserdruck)
    return Aussentemp,Feuchtigkeit,Luftdruck,Wasserdruck

def zufalls_ID():
    ABC=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    Buchstaben=random.sample(ABC, 5)
    Buchstaben="".join(Buchstaben)
    Zahl= random.choice([1,10,100,1000])
    
    ID=str(int(random.random()*100000))+"-"+str(int(random.random()*Zahl))+Buchstaben+"-"+str(int(random.random()*10000))

    return ID

################# Header schreiben falls datei nicht exisitiert#######################
    


file_index="Holzfabrik.csv"
##print("Datei wird hier gespeichert: ",file_index)
if os.path.isfile(file_index):
    #print("Datei Holzfabrik vorhanden")
    pass
else:
    output_file = open(file_index, 'w')
    output_file.write("Kunde,Produkt,Holz,AuftragsID,Maschine,Dauer,_time,Umsatz,Gewicht\n")
    output_file.close()


file_prozesskette="Prozesskette.csv"
##print("Datei wird hier gespeichert: ",file_index)
if os.path.isfile(file_prozesskette):
    #print("Datei Holzfabrik vorhanden")
    pass
else:
    output_file = open(file_prozesskette, 'w')
    output_file.write("_time, Auftragsnummer, Prozessschritt,Lager\n")
    output_file.close()


file_metrics="Holzfabrik_Maschinen.csv"
if os.path.isfile(file_metrics):
    #print("Datei File Metrics vorhanden")
    pass
else:
    output_file = open(file_metrics, 'w')
    output_file.write("metric_timestamp,Verantwortlicher,metric_name,_value\n")
    output_file.close()

################## Datengrundlage #############################
kunden_arr=[]
kunden_arr.append({"Kunde":"IDEA"   ,"Prio":6,"Produkte":["Schrank","Stuhl","Tisch","Regal","Tablethalter"],"P_Produkt":[0.4,0.2,0.15,0.2,0.05],"Holzart":["Fichte","Kiefer","Buche","Birke"],"P_Holzart":[0.1,0.3,0.2,0.4]})
kunden_arr.append({"Kunde":"Fuchsbau","Prio":5,"Produkte":["Tisch","Stuhl","Regal"],"P_Produkt":[0.7,0.1,0.2],"Holzart":["Fichte","Tanne"],"P_Holzart":[0.4,0.6]})
kunden_arr.append({"Kunde":"Porathholz" ,"Prio":4,"Produkte":["Tisch","Stuhl"],"P_Produkt":[0.9,0.1],"Holzart":["Buche","Kiefer"],"P_Holzart":[0.5,0.5]})
kunden_arr.append({"Kunde":"Schmidt Bretter","Prio":3,"Produkte":["Tisch","Regal","Stuhl"],"P_Produkt":[0.8,0.1,0.1],"Holzart":["Fichte","Tanne"],"P_Holzart":[0.3,0.7]})
kunden_arr.append({"Kunde":"Weser Baumschule"  ,"Prio":2,"Produkte":["Schrank","Hocker"],"P_Produkt":[0.5,0.5],"Holzart":["Fichte","Buche"],"P_Holzart":[0.4,0.6]})
kunden_arr.append({"Kunde":"Walter Baumhaus" ,"Prio":0.5,"Produkte":["Regal"],"P_Produkt":[1],"Holzart":["Fichte","Birke"],"P_Holzart":[0.7,0.3]})
kunden_arr.append({"Kunde":"Pinoccio" ,"Prio":1 ,"Produkte":["Tisch","Hocker"],"P_Produkt":[0.3,0.7],"Holzart":["Kiefer","Buche"],"P_Holzart":[0.5,0.5]})
kunden_arr.append({"Kunde":"Herrmann Bretter","Prio":1,"Produkte":["Bank"],"P_Produkt":[1],"Holzart":["Birke","Buche"],"P_Holzart":[0.1,0.9]})
kunden_arr.append({"Kunde":"Ecke"    ,"Prio":1,"Produkte":["Schrank","Stuhl"],"P_Produkt":[0.3,0.7],"Holzart":["Fichte","Kiefer"],"P_Holzart":[0.2,0.8]})
kunden_arr.append({"Kunde":"Immanuel Kantholz"   ,"Prio":1,"Produkte":["Stuhl","Bank"],"P_Produkt":[0.5,0.5],"Holzart":["Fichte","Kiefer"],"P_Holzart":[0.4,0.6]})
kunden_arr.append({"Kunde":"BlumenExpress"   ,"Prio":1.5,"Produkte":["Tablethalter","Truhe"],"P_Produkt":[0.8,0.2],"Holzart":["Fichte","Kiefer"],"P_Holzart":[0.4,0.6]})
kunden_arr.append({"Kunde":"Blocksberg Besen" ,"Prio":0.3,"Produkte":["Truhe","Tablethalter"],"P_Produkt":[0.8,0.2],"Holzart":["Buche","Eiche"],"P_Holzart":[0.4,0.6]})
kunden_arr.append({"Kunde":"Fynn" ,"Prio":0.05,"Produkte":["Zaunlatten"],"P_Produkt":[1],"Holzart":["Birke"],"P_Holzart":[1.]})



kunden_info={}
kunden_info.update({"IDEA":{"Adresse":"Orangenstrasse 30","IP":zufalls_ip()}})
kunden_info.update({"Fuchsbau":{"Adresse":"Himbeerstrasse 18","IP":zufalls_ip()}})
kunden_info.update({"Porathholz":{"Adresse":"Baumweg 3","IP":zufalls_ip()}})
kunden_info.update({"Schmidt Bretter":{"Adresse":"Zitronengasse 32","IP":zufalls_ip()}})
kunden_info.update({"Weser Baumschule":{"Adresse":"Erdbeer Rue 32","IP":zufalls_ip()}})
kunden_info.update({"Walter Baumhaus":{"Adresse":"Marmeladenplatz 642","IP":zufalls_ip()}})
kunden_info.update({"Pinoccio":{"Adresse":"Keksstrasse 22","IP":zufalls_ip()}})
kunden_info.update({"Herrmann Bretter":{"Adresse":"Hariboweg 98","IP":zufalls_ip()}})
kunden_info.update({"Ecke":{"Adresse":"An der Ecke 54","IP":zufalls_ip()}})
kunden_info.update({"Immanuel Kantholz":{"Adresse":"Fotogasse 766","IP":zufalls_ip()}})
kunden_info.update({"Blocksberg Besen":{"Adresse":"Hexenweg 666","IP":zufalls_ip()}})
kunden_info.update({"Blümchen":{"Adresse":"Sonnenblumnenallee 10","IP":zufalls_ip()}})


verhaltnis_auftrage=wichtigkeit(kunden_arr) # erstellt array aus den Prioritäten und normiert die Summe auf 1.

produkt_info={}
produkt_info.update({"Stuhl":{"Kosten":100,"Dauer":15,"Gewicht":5}})
produkt_info.update({"Schrank":{"Kosten":200,"Dauer":30,"Gewicht":50}})
produkt_info.update({"Tisch":{"Kosten":150,"Dauer":20,"Gewicht":20}})
produkt_info.update({"Regal":{"Kosten":50,"Dauer":10,"Gewicht":2}})
produkt_info.update({"Hocker":{"Kosten":40,"Dauer":7,"Gewicht":1}})
produkt_info.update({"Bank":{"Kosten":60,"Dauer":12,"Gewicht":15}})
produkt_info.update({"Tablethalter":{"Kosten":5,"Dauer":1,"Gewicht":0.3}})
produkt_info.update({"Truhe":{"Kosten":30,"Dauer":25,"Gewicht":40}})
produkt_info.update({"Zaunlatten":{"Kosten":15,"Dauer":8,"Gewicht":10}})


holz_info={}
holz_info.update({"Eiche":{"Kosten":1.1,"Dauer":1.0,"Farbe":"Sehr Dunkel"}})
holz_info.update({"Buche":{"Kosten":1.2,"Dauer":1.02,"Farbe":"Leicht Dunkel"}})
holz_info.update({"Fichte":{"Kosten":1.3,"Dauer":1.15,"Farbe":"Mittel Dunkel"}})
holz_info.update({"Tanne":{"Kosten":0.9,"Dauer":1.05,"Farbe":"Sehr Hell"}})
holz_info.update({"Kiefer":{"Kosten":0.95,"Dauer":1.07,"Farbe":"Mittel Hell"}})
holz_info.update({"Birke":{"Kosten":1.0,"Dauer":1.04,"Farbe":"Dunkel"}})

Mitarbeiter=["Albert","Richard","Thomas"]

# Lookups generiert aus simulierten Daten. Für den Fall das sich was ändert, ausklammern und in  Lookup Ordner verschieben.
if Erstelle_Lookup:
    erstelle_lookup("Holz",holz_info,"holzinfo_lookup.csv")
    erstelle_lookup("Produkt",produkt_info,"produktinfo_lookup.csv")
    erstelle_lookup("Kunde",kunden_info,"kundeninfo_lookup.csv")


########################
hallen={"Halle":{"Bieberbau":{"alpha":{"Messwerte":["Temperatur","Strom"]}},"Spechtnest":{"beta":{"Messwerte":["Temperatur","Strom"]},"gamma":{"Messwerte":["Temperatur","Strom"]}}}}
aussenwerte={"Aussenwerte":{"Messwerte":["Wasserdruck","Aussentemp","Feuchtigkeit","Luftdruck"]}}
auftrags_wert={"Letzter_Auftrag":["Maschine","Kunde","Produkt","Holz","ID","Dauer","Umsatz","Gewicht","Zeit"]}


#Startparameter
Wasserdruck=20
Temp_a,Strom_a=10,30
Temp_b,Strom_b=10,30
Temp_c,Strom_c=10,40
letzter_Kunde="IDEA"
ID=zufalls_ID()
neuer_auftrag=True
alpha,beta,gamma=0,0,0
Maschine="Alpha"
Lager=[0,1,2,3]

for i in range(kunden):
    

    time.sleep(1)
    Zeitstempel=round(time.time(),1)
    Time= datetime.datetime.fromtimestamp(int(Zeitstempel)).strftime('%Y-%m-%d %H:%M:%S')

    
    if (neuer_auftrag):
        kunde_aus=auftrag(kunden_arr,verhaltnis_auftrage)
        #print("kundeaus",kunde_aus)
    
        if letzter_Kunde==kunde_aus[0]:
            #print("Sammelauftrag:", ID, "aktueller Kunde:",kunde_aus[0]," Letzter Kunde:",letzter_Kunde)
            pass
        else:
            ID=zufalls_ID()
        letzter_Kunde=kunde_aus[0]

        gewicht      =produkt_info[kunde_aus[1]]["Gewicht"]+round(random.gauss(1,0.2),3)
        auftragsdauer=round(produkt_info[kunde_aus[1]]["Dauer"] *holz_info[kunde_aus[2]]["Dauer"],2)
        umsatz       =round(produkt_info[kunde_aus[1]]["Kosten"]+holz_info[kunde_aus[2]]["Kosten"]*gewicht,2) #Arbeitskosten + Materialkosten

        #Auftrag der als Event an Splunk geht
        aktueller_auftrag={"Kunde":kunde_aus[0],"Produkt":kunde_aus[1],"Holz":kunde_aus[2],"AuftragsID":ID,"Maschine":Maschine,"Dauer":auftragsdauer,"_time":Time,"Umsatz":umsatz,"Gewicht":gewicht}
    
        #print("Alpha:",alpha,"Beta:",beta,"Gamma:",gamma)
        #print(aktueller_auftrag)
        #write_logs(file_index,aktueller_auftrag)
        write_logs_array(file_index,[kunde_aus[0],kunde_aus[1],kunde_aus[2],ID, Maschine,auftragsdauer,Time,umsatz,gewicht])

        Lager=prozess_ablauf(ID,Zeitstempel,Maschine,Lager)


    #Welche Maschine als nächstes Ausgewählt wird
    neuer_auftrag=False
    if alpha<=0:
        alpha=auftragsdauer+alpha*0
        Maschine="Alpha"
        neuer_auftrag=True
        
    elif beta <=0:
        beta=auftragsdauer+beta*0
        Maschine="Beta"
        neuer_auftrag=True

    elif gamma <=0:
        gamma=auftragsdauer+gamma*0
        Maschine="Gamma"
        neuer_auftrag=True

    if i%120==0: #Schichtwechsel
        Benutzer=["Michael","Karl","Emilia","Tim","Sarah","Wilhelm","Emmy"]
        
        Benutzer_a=random.choice(Benutzer)
        Benutzer.remove(Benutzer_a)
        Benutzer_b=random.choice(Benutzer)
        Benutzer.remove(Benutzer_b)
        Benutzer_c=random.choice(Benutzer)
        Benutzer.remove(Benutzer_c)
        
    Temp_a,Strom_a=maschinen_daten_schreiben(Zeitstempel,Benutzer_a,"Bieberbau","alpha",i)
    Temp_b,Strom_b=maschinen_daten_schreiben(Zeitstempel,Benutzer_b,"Spechtnest","beta", i)
    Temp_c,Strom_c=maschinen_daten_schreiben(Zeitstempel,Benutzer_c,"Spechtnest","gamma",i)
    Aussentemp,Feuchtigkeit,Luftdruck,Wasserdruck=maschinen_daten_schreiben_aussen(Zeitstempel,i,Wasserdruck,False)


    # Abarbeiten der Maschine
    alpha=alpha-1
    beta=beta-1
    gamma=gamma-1
    









