# ArmuzziLeonardo_progettoReti2021
Progetto 2 per esame di Programmazione di Reti


##Informzioni personali

Nome: Leonardo\
Cognome: Armuzzi\
e-mail: leonardo.armuzzi@studenti.unibo.it\
Matricola: 0000937481

## Traccia 2

Si immagini di dover realizzare un Web Server in Python per
una azienda ospedaliera. I requisiti del Web Server sono i
seguenti:
• Il web server deve consentire l’accesso a più utenti in
contemporanea.\
• La pagina iniziale deve consentire di visualizzare la lista
dei servizi erogati dall’azienda ospedaliera e per ogni
servizio avere un link di riferimento ad una pagina
dedicata.\
• L’interruzione da tastiera (o da console) dell’esecuzione
del web server deve essere opportunamente gestita in
modo da liberare la risorsa socket.\
• Nella pagina principale dovrà anche essere presente un
link per il download di un file pdf da parte del browser
• Come requisito facoltativo si chiede di autenticare gli
utenti nella fase iniziale della connessione.\

## Funzionalità

Il sito esopone i servizi del gruppo ospedaliero:

*Radiografia\
*Pediatria \
*Chirurgia plastica

Con la possibilià di scaricare il pdf con la lista dei pazienti

## Librerie utilizzate 

*sys\
*os\
*soket

## Utilizzo 

Avviare il server da command line
```bash
python webserver_armuzzi.py
```
Il server partiarà dando informzioni sullo stato dell'avvio Serving 
```bash
HTTP traffic from *Path* on *User* using port 8080
```
Per terminare il webserver da console semplicemente utilizzare Crtl+C




