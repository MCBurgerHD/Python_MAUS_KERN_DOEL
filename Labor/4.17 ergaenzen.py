import matplotlib . pyplot as plt
from random import randrange

lst = [0, 100]
def get_noten(lst):
    """ Bekommt eine Liste von Prozentwerten ([0, 100]) übergeben
    und berechnet daraus Noten. Die retournierte Liste gibt die
    Anzahl der jeweiligen Note an ;
    z.B. return_liste[0] == Anzahl der 'Sehr gut ' """
     


def get_prozent():
    """Retourniert eine Liste von 36 zufälligen Prozentwerten ([0, 100])."""
    i = 0
    while i < 36:
    a = randrange(0, 100)
    i += 1
    return a

def plot(prozent, noten):
    plt.rcParams.update({"font.size": 24})
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (6, 4))
    fig.dpi = 75
    ax1.hist(prozent, bins=10)
    ax1 . set_title ("Punkteverteilung")
    ax1 . set_ylabel ("Anzahl an Schülern")
    ax1 . set_xlabel ("Erreichte Punkte")
    ax2 . bar ( range (1 , 6) , height = noten )
    ax2 . set_title ("Notenverteilung")
    ax2 . set_ylabel ("Anzahl an Schülern")
    ax2 . set_xlabel ("Note")
    plt . show ()

prozent = get_prozent()
noten = get_noten(prozent)
plot(prozent, noten )