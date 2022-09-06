Explications de comment ouvrir un rttm avec les packages. 

J'ai rajouté dans le main "scorelib" qui contient des fichiers pour
ouvrir les fichiers rttm. 

Dans un script lorsque l'on veut ouvrir un rttm pour en faire un Turn (objet définit dans .turn dans 
scorelib), Il faut mettre : 

from scorelib import rttm 

Puis on peut utiliser la fonction load_rttm qui prend un fichier rttm (ex load_rttm(file.rttm)) et qui 
renvoie un tableau de Turn. 

Un Turn correspond à la participation inintérompue d'un locuteur. La première donnée (le onset) est 
l'instant au quel le locuteur a commencé son discour, la deuxième (duration) le temps de son intervention, 
la troisième le genre du locuteur, et le quatrième le nom du fichier rttm. 

Il y a un exemple dans essais.py
 