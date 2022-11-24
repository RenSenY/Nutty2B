import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

cond  = input("請輸入您要片名關鍵字:")

db = firestore.client()
collection_ref = db.collection("素清电影")
docs = collection_ref.get()
result = ""
for doc in docs:
	dict = doc.to_dict()
	if cond in dict["title"]:
		#print("{}老師開的{}課程,每週{}於{}上課".format(dict["Leacture"], dict["Course"],  dict["Time"],dict["Room"]))
		result += dict["title"] + "" 
		result += dict["rate"] + "\n"
print(result)

