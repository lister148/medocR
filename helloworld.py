import requests
import time

# Fonction
def my_code():
    requests.post("https://ntfy.sh/helloworld",
                  data="Hello World !".encode(encoding='utf-8'))

# Boucle infinie pour exécuter la fonction toutes les 20 secondes
while True:
    my_code()
    time.sleep(20)  # Attente de 20 secondes avant la prochaine exécution