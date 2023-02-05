from pymongo import MongoClient
import time

# Connection a MongoDB
client = MongoClient('localhost',27017)

# on choisi la bdd France et la collection communes
db = client.France
communes = db.communes

def recherche_commune(nom):

    debut = time.time()
    commune = communes.find_one({'nom_commune' : nom})
    fin = time.time()
    print("Pour la commune: " + nom)
    #print(commune)
    print("Document trouvé en "+ str(fin - debut) +" secondes" )

if __name__ == "__main__":
    recherche_commune('Ambérieu-en-Bugey')