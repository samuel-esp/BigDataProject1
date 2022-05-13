# BigDataProject1
a cura di Simone Chilosi e Samuel Esposito.

Specifiche dei job:
**Job 1**: Un job che sia in grado di generare, per ciascun anno, le dieci parole che sono state più usate nelle
recensioni (campo text) in ordine di frequenza, indicando, per ogni parola, il numero di occorrenze
della parola nell’anno.

**Job 2**: Un job che sia in grado di generare, per ciascun utente, i prodotti preferiti (ovvero quelli che ha
recensito con il punteggio più alto) fino a un massimo di 5, indicando ProductId e Score. Il risultato
deve essere ordinato in base allo UserId.

**Job 3**: Un job in grado di generare coppie di utenti con gusti affini, dove due utenti hanno gusti affini se hanno
recensito con score superiore o uguale a 4 almeno tre prodotti in comune, indicando le coppie di utenti
e i prodotti recensiti che condividono. Il risultato deve essere ordinato in base allo UserId del primo
elemento della coppia e non deve presentare duplicati

**Dataset**: https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews