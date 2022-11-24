from flask import Flask, render_template, request

import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>黄素清Firestore資料庫存取</h1>"
    homepage += "<a href=/search>電影查詢</a><br>"

    return homepage

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        cond = request.form["keyword"]
        result = "請輸入您要片名關鍵字：" 

        db = firestore.client()
        collection_ref = db.collection("素清电影")
        docs = collection_ref.get()
        result = ""
        for doc in docs:
            dict = doc.to_dict()
            if cond in dict["title"]:
                #print("{}老師開的{}課程,每週{}於{}上課".format(dict["Leacture"], dict["Course"],  dict["Time"],dict["Room"]))
                result += dict["title"] + "   (      " 
                result += dict["rate"] + "  )\n"

        if result =="":
            result = " 抱歉，查無相關條件的電影資訊 "
            
        return result
    else: 
        return render_template("search.html")      
            
#if __name__ == "__main__":
#    app.run()S