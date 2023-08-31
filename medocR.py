import datetime
import requests
import time

# Fonction
def my_code():
    requests.post("https://ntfy.sh/nom_du_salon",
    data="Hello, tu as pris ton traitement ?".encode(encoding='utf-8'))


# Heure format 24 heures
heure_specifique = "13:30"  # Exemple : 13h30

heure_executed = False

# Boucle
while True:
    maintenant = datetime.datetime.now().time().strftime("%H:%M")
    
    if maintenant == heure_specifique:
        if not heure_executed:
            my_code()
            heure_executed = True
    else:
        heure_executed = False  # Réinitialiser pour la prochaine journée
    
    time.sleep(5)  # Attente 5 secondes pour éviter une utilisation excessive du processeur


# Boucle pour exécuter le code toutes les 20 secondes

#while True:
#    my_code()
#    time.sleep(20)  # Attente de 20 secondes avant la prochaine exécution