# Membres du groupe
- Bastien TAKIS
- Alexandre MONIER
- Myke CHASTANG

# Gitflow
- Les features sont réalisées sur une branche nommée `feat/nom_feature`, puis une PR est créée sur `master`.
- `master` est protégée, il faut obligatoirement passé par une PR, et qu'elle soit approuvée par une personne au moins.

# Environnement
L'environnement comporte une application python permettant de récupérer des données d'une table en base mysql et d'un ajouter des données. Il y a aussi un nginx configuré en reverse proxy. En effet le container de l'application python n'est pas exposé, il faut passer par le container nginx : http://localhost:80.

La deuxième étape de ce projet consiste à implémenter Ansible pour gérer les configuration de l'environnement et faciliter le déploiement par la suite.

Nous avons décidé d'utiliser docker compose pour la première étape. Ainsi, Ansible aura pour but de générer les fichiers `compose.yml` permettant de containeriser les services.