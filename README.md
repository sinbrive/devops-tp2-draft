# TP DevOps – Niveau 1 : Bases GitHub & CI simple

Bienvenue dans le premier niveau du TP DevOps ! 
Il est fait usage de conteneur.

## Travail à faire
1. Lancer :
	docker-compose up -d
2. Tester le site
	curl localhost:5000

3. Créer une branche, coder, tester (pytest), commit & push puis ouvrir une PR.
   Actions :
      - git checkout -b votre-nom-feature
      - Entrer dans le shel du conteneur : docker exec -it devops-tp bash
      - modifier les fichiers app.py et test_app.py
         - Consigne : ajouter le route `/hello/<name>` avec les variables nécessaires
      - pytest -v
      - flake8 app.py test_app/py
      - si erreur, cooriger et tester
      - sortir du shell: exit
4. stopper le conteneur : docker rm -f deveops-tp

5. relancer : docker-compose up -d --build

6. vérifier : curl localhots:5000

7. si le résultat est conforme aux attentes, pousser la branche : git push origin votrenom-feature

8. aller sur Github et initier un Pull Request

9. suivre l'état du PR

