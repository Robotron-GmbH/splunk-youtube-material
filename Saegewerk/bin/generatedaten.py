#!/usr/bin/env python
# coding=utf-8

import sys,platform, os
import time

path = os.path.normpath(os.getcwd())
splunkhome_arr=path.split(os.sep)[:-4]
splunkhome=os.sep.join(splunkhome_arr)
sys.path.append(os.path.join(splunkhome, 'etc', 'apps', 'Saegewerk', 'lib'))

from splunklib.searchcommands import dispatch, GeneratingCommand, Configuration, Option, validators 


@Configuration()
class generatedatenCommand(GeneratingCommand):
    path = os.path.normpath(os.getcwd())
    splunkhome_arr=path.split(os.sep)[:-4]
    splunkhome=os.sep.join(splunkhome_arr)
    
    if platform.system()=="Windows":
        Python=os.path.join(splunkhome,"bin","python.exe") #Pfad zur App Windows
    else:
        Python=os.path.join(splunkhome,"bin","python") #Pfad zur App Mac und Linux

    seconds_running = Option(require=True, validate=validators.Integer())
    
    def generate(self):
        for i in range(1, 2):
            Befehl='"'+self.Python+'"'+' Saegewerk.py '+ str(self.seconds_running)
            os.system(Befehl)

            text = 'Dateien werden hier gespeichert: '+os.getcwd() + "\nSplunkhome: "+self.splunkhome +"\nPython: "+self.Python+"\nBefehl: "+Befehl+"\n Seconds running: "+str(self.seconds_running)
            yield {'_time': time.time(), 'event_no': i, '_raw': text}
 
dispatch(generatedatenCommand, sys.argv, sys.stdin, sys.stdout, __name__)
 