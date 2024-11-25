#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
import os,sys
from splunklib.searchcommands import dispatch, StreamingCommand,Configuration

@Configuration()
class saegeanalyseCommand(StreamingCommand):
    def stream(self, records):
        """
        # Input = Output
        for record in records: # Zeile fuer Zeile ausgeben
            zwi_dic={} # leeres Dictionary
            for feldname in record:# Alle Felder innerhalb des Dictionarys
                zwi_dic.update({feldname:record[feldname]}) # Aktuelle
            yield zwi_dic #volles Dictionary fuer diese Zeile
        """
        
        zwi_dic={} # leeres Dictionary
        for record in records: # Zeile fuer Zeile ausgeben
            zwi_dic.update({"Holz":record["Holz"],"Euro pro Sekunde": float(record["Umsatz"]) / float(record["Dauer"])}) # Aktuelle
            yield zwi_dic #volles Dictionary fuer diese Zeile
        
# Komplettes Ergebnis zurueck in die SPL Pipe geben
dispatch(saegeanalyseCommand, sys.argv, sys.stdin, sys.stdout, __name__)