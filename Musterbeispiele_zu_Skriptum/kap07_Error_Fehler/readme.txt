An jeden try – Block muss zumindest ein except oder finally – Block folgen. 
Passiert ein Fehler, so wird jener except – Block betreten, welcher als erster zutrifft. 
Danach gilt der Fehler als behandelt und es wird nach dem try – Konstrukt weitergemacht. 
Tritt kein Fehler auf, so werden die Anweisungen des else – Blocks durchgeführt. 
Der Code im finally – Block wird immer ausgeführt. 
Egal ob ein Fehler auftritt, er behandelt wird oder nicht (eignet sich für Aufräumarbeiten).
