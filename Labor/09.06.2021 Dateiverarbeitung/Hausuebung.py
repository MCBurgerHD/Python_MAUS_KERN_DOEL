"""
#-----------------------------------------------------------------------------------------------
#Maximilian Ertl
#12.6.2021
#                            schreiben
#Nimmt die Namen unde den Beruf aus der Datei Mitarbeiter und gibt diese in einer anderen
#formatierung in eine neue Datei aus.
#------------------------------------------------------------------------------------------------
"""

#----------------------------------------------------------------------------------------
#                           schreiben
#Nimmt die Namen unde den Beruf aus der Datei Mitarbeiter und gibt diese in einer anderen
#formatierung in eine neue Datei aus.
#-----------------------------------------------------------------------------------------
"""
def schreiben(fobjein, fobjaus):
    fobjein = open(fobjein)
    fobjaus = open(fobjaus, "w")
    neuertext = ""
    for i in fobjein:
        if(i != "\n"):
            neuertext += i.rstrip()
        else:
            neuertext = neuertext.replace(":", " ")
            neuertext = neuertext.split(" ")
            fobjaus.write("{:} {:s} ({:s})\n".format(" ".join(neuertext[2:]), neuertext[1], neuertext[0])
            neuertext = ""
    fobjein.close()
    fobjaus.close()




schreiben("uebungsdateien/mitarbeiter.txt", "uebungsdateien/mitarbeiterneu.txt")
"""