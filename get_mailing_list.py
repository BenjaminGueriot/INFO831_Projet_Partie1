from pymongo import MongoClient
from bson.objectid import ObjectId

# Connection a MongoDB
client = MongoClient('localhost',27017)

# On choisi la bdd mailing et la collection lists
db = client.mailing
lists = db.lists

def recherche_mailing_list(nom):

    list = lists.find_one({'name' : nom})
    print("Pour la liste: " + nom)
    #print(list)

    result = []
    for user in list['users']:
        result.append(db.users.find_one({"_id" : ObjectId(user)}))

    #print(result)
    return({"name" : list, "users" : result})

if __name__ == "__main__":
    print(recherche_mailing_list('mailing-list-1'))