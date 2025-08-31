# TP DevOps – Niveau 1 : Bases GitHub & CI simple

Bienvenue dans le premier niveau du TP DevOps ! 
Il est fait usage de conteneur.

## Travail à faire
1. Lancer :
	docker-compose up -d
2. Tester le site
	curl localhost:5000

3. Créer votre branche "votrenom-feature"
	git checkout -b votrenom-feature

4. Entrer dans le conteneur :
	docker exec -it devops-tp bash

4. Créer une branche, coder, tester (pytest), commit & push puis ouvrir une PR.
   Actions :
      - modifier les fichiers app.py et test_app.py
      - Consigne : ajouter le route `/hello/id_apge` avec les variables nécessaires
         - retester et executer app.py
      - pytest -v
      - flake8 app.py test_app.py
      - python app.py


---



