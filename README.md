# Voted Perceptron e Perceptron a confronto
## Composizione
Il progetto è strutturato in modo tale che ogni test possa essere riprodotto in una singola classe chiamata AllTest.py.
per poter usare correttamente il programma illustro prima di tutto le sue classi e come lavorano, in seguito iin ognuna di esse spiego come poterle usare.

Perceptron.py:

```è un file contente i metodi di training(self, X, Y) e guess(Xi) dove X è un array di elementi da cui vengono prelevati i valori del  dataset e inseriti nel Perceptron.```

Voted Perceptron.py: 

```è un file che similmente al Perceptron ha come metodi training e guess con le stesse dimensioni di X e Y.```

Datasets:

```questo file contiene i file presi da Uci Machine learning repositories```

PokerHandTest.py:

```questo file contiene una funzione, chiamata test,  che studia il file pokerhandTest.csv stampa a schermo i risultati del training e del guess e le matrici di confusione, normalizzate e non, e la percentuale di accuratezza del nostro algoritmo```

AirQuality.py:

```studiamo i valori del file AirQuality.csv e ne stampa a schermo i risulati del training e del guess oltre alle matrici di confusione e la percentuale di accuratezza```

DotaTest.py:

```studia i risultati degli algoritmi sul dataset Dota2Train.csv e Dota2Test.csv e notiamo che non si sfrutta la la funzionalità della repository di scikit-learn poiché si ha già una divisione tra Train e Test. ```

Grafic.py:

```sono compresi tre metodi che permettono di sviluppare graficamente i risultati della percentuale di accuratezza e ne vediamo i risutlati in base al tempo con il quale vengono cambiati```

AllTest.py:

```una classe che semplifica l'utilizzo delle funzioni delle varie classi permettendo di sfruttarle in un unica classe.```

## Come funziona

Nella classe AllTest vengono specificati le classi che sono presenti nel progetto. A questo punto nei singoli file.py vengono passati i set di Train e Test ed inoltre vengono creati i file Y(che permette una classificazione binaria del problema). A questo punto, grazie all'utilizzo della funzione di Scikit-learn, train_test_split, possiamo dividere il nostro set in  Train e Test. Inoltre psosiamo decidere di quanto scegliere il nostro set di training e di test grazie al particolare attributo test_size=n del quale è composto la funzione citata prima.
Da qui in poi viene creato prima l'oggetto perceptron e im seguito l'oggetto Voted Perceptron ed entrambi allenati un numero prestabilito di epochs, numero espresso nei costruttori dei nostri oggetti. Nello stesso programma possiamo vedere stampati a schermo i risultati del test di accuratezza, della matrice di confusione e del report di classificazione.

## Maneggiare il dataset

Per modificare il dataset dobbiamo semplicemente andare a scaricarlo da UCI machine learning repository e aggiungerlo inizialmente alla cartella dei datasets. 
Dopodichè bisogna modificare la funzione di lettura in modo tale che il nome del file corrisponda con quello scritto nella funzione, affinché avvenga la sua corretta lettura. Detto ciò bisogna anche cambiare i singoli nomi delle colonne e far corrispondereal numero di colonne del file, il nuovo numero di colonne con cui andremo a modificare il file.

## Output

L'output è diviso tra Perceptron e Voted Perceptron. Ogni valore ha le sue caratteristiche:

* Single Layer Accuracy:

``` specifica l'accuratezza con la quale l'algoritmo si sia avvicinato alla realtà```

* Grafici:

```specifica, attraverso un grafico, le accuratezze durante le diverse iterazioni del programma e del training```

* Normalized confusion Matrix

```indica la matrice di confusione normalizzata che specifica il numero di test positivi o negativi corretti.```

# Riferimenti
Tutti i datasets forniti in questo progetto sono stati presi da [UCI Machine Learning](http://archive.ics.uci.edu/ml/index.php), Grazie al quale è stato semplice poter reperire dei dataset con tanto di spiegazione. 

Si ringrazia inoltre le seguenti pagine per aver reso più chiaro il concetto e lo sviluppo in python degli algoritmui studiati:

* [Freund & Schapire 1999](https://link.springer.com/content/pdf/10.1023/A:1007662407062.pdf)
* [The Coding Train](https://www.youtube.com/user/shiffman)
* [Artificial Intelligence: a modern approach](http://aima.cs.berkeley.edu/)
* [StackOverflow](https://stackoverflow.com/)
