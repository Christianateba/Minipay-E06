# Résultats du Lab 1

- Serveur arrêté : le client obtient "[votre message d'erreur]" en [durée] ms. Il ne sait pas si un paiement a été effectué.
- Serveur injoignable (10.255.255.1) : le client attend [durée] ms puis affiche "[votre message]". Deux pannes différentes donnent des erreurs et des délais différents : c'est la panne partielle.
- Double débit : le serveur attend 3 s alors que le timeout du client est de 2 s. Le client réessaie et le serveur a exécuté [2] paiements pour un seul ordre.
- Défi : avec un identifiant unique (uuid), le serveur ignore le doublon et le compteur reste à [1].