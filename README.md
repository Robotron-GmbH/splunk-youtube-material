# splunk-youtube-material

Auf dieser Seite findet ihr alle wichtigen Unterlagen zum Splunk-YouTube Kanal von Robotron.

Hier findet ihr unter anderem:   

- Die Datengenatorapp mit dem ihr Daten eines Sägewerkes simulieren könnt. Eine ausführliche Video-Anleitung für die Installation findet ihr hier: LINK. 
- Weiteres Infomaterial zu den Videos.


## Anleitung für die Installation des Datengenerators
1. Den kompletten Ordner Daten_Generator herrunterladen und gegebnenfalls entpacken.
2. Den Ordner anschließend in den SPLUNK/etc/apps Ordner verschieben. Unter Windows findet man Splunk meistens unter C:\Program Files\.
3. Splunk neustarten. Hierbei unter Einstellungen -> Serversteuerungen -> Splunk neustarten gehen.
4. Anschließend kann man mit dem Befehl     | generatedaten seconds_running=X wobei X die Laufzeit des Skriptes in Sekunden angibt.
5. Die Daten können dann mit index=auftrag abgerufen werden. Ebenfalls gibt es metrische Daten unter dem Index Maschinen welche im Analytics Store zu finden sind.  

### Daten
Das Skript befüllt zwei Indizes, den Eventindex "auftrag" und den Metrikindex "maschinen". In ersterem sehen die Daten wie folgt aus:
| Kunde | Produkt | Holz | AuftragsID | Maschine | Dauer | _time | Umsatz | Gewicht|
| -- | -- | -- | -- | -- | -- | -- | -- | --|
|Fuchsbau | Regal | Tanne | 5074-19kiomb-3300 | Alpha | 10.5 | 2021-07-05 12:48:18 | 52.66 | 2.958 | 
|Immanuel Kantholz | Stuhl | Fichte | 49209-4ymgzt-7674 | Alpha | 17.25 | 2021-07-05 12:48:18 | 108.08 | 6.216 | 
|Weser Baumschule | Hocker | Fichte | 10444-56kvcar-9546 | Alpha | 8.05 | 2021-07-05 12:48:19 | 42.96 | 2.274 | 
|Porathholz | Tisch | Kiefer | 15860-0mauhi-4057 | Alpha | 21.4 | 2021-07-05 12:48:19 | 170.09 | 21.147 | 

Die AuftragsID ist dabei ein zufällig erzeugter String. Die Dauer gibt an wie lange der Auftrag in Sekunden gedauert hat.

Die Metrikdaten werden hingegen im folgenden Format gespeichert. 

metric_timestamp | Halle | metric_name | _value
| -- | -- | -- | --
|1625482098.1778402 | Bieberbau | Bieberbau.alpha.Temperatur | 39.68 | 
|1625482098.1778402 | Bieberbau | Bieberbau.alpha.Strom | 10.724 | 
|1625482098.1778402 | Spechtnest | Spechtnest.beta.Temperatur | 40.83 | 
|1625482098.1778402 | Aussenbereich | Aussenbereich.Aussentemperatur | 17.8 | 

metric_timestamp beschreibt dabei die Zeit UNIX-Zeit. Metric_Name ist der Pfad wo sich das Messgerät befindet, und _value beschreibt den Wert, z.B. Temperatur in Grad oder den Luftdruck.

## Splunk Kurse
Du bist Anfänger oder Fortgeschrittener und interessierst dich für eine Splunk Schulung? Hier findest du eine Auswahl an passenden Kursen der Firma Robotron: https://www.robotron.de/schulungszentrum/splunk 


## Beispieldashboard
Im folgenden Bild sieht man ein Dashboard das mit den simulierten Sägewerk Daten befüllt wurde.
![dashboardsägewerk](https://user-images.githubusercontent.com/87022602/124736650-82679380-df17-11eb-9b2c-2f9d00095baa.PNG)
