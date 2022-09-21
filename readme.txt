Le dossier contenant le fichier notebook de travail(model_saving.ipynb) doit etre executer afin de generer le fichier (foodRecommender.pkl) qui sera utiliser par les executables python

La dataset(food.csv ) est disponible ici:

https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions?resource=download&select=RAW_interactions.csv

	app.py contient le script de lancement d'un formulaire pour obtenir le rating d'un (user_id,item_id) donne avec les dossiers static et templates contenants respectivement les fichiers css et html(index.html) du formulaire.

	et 
	
	topNRecommendation_app.py contient le script de lancement d'un formulaire pour obtenir le rating d'un (user_id,list des item_id,nombre d'articles a recommander) donne avec les dossiers static et templates contenants respectivement les fichiers css et html(indexTopN.html) du formulaire.


Pour les faire fonctionner,il faut avoir la librairie flask installer et depuis la console, executer le script grace a la commande "python app.py" ou "python topNRecommendation_app.py" et apres un temps d'execution,un lien http sera fourni afin de pouvoir accceder a l'application depuis le navigateur.

Pour ce systeme de recommandation, les caracteristiques de la machine d'execution sont les suivantes:

hp Elitebook 840 G3
ram:16gb 
disque dur:ssd 500gb
processur: intel(R) Core(TM) i5-6300U CPU @ 2,40GHz 2.50 GHz
Systeme d'exploitation:windows 10 64bits professionel


