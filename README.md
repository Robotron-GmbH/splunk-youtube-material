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

