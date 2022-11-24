import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = [
{
  "hyperlink": "http://www.atmovies.com.tw/movie/fben10168670/",
  "lastUpdete": "2022/11/18 01:19",
  "Picture": "http://app2.atmovies.com.tw/poster/fben10168670/",
  "rate": "限制級(未滿十八歲之人不得觀賞)",
  "showDate": "2022/11/24",
  "showLength": "130",
  "title": "骨肉的總和"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/fden21435436/",
  "lastUpdete": "2022/11/18 01:19",
  "Picture": "http://app2.atmovies.com.tw/poster/fden21435436/",
  "rate": "保護級(未滿六歲之兒童不得觀賞，六歲以上未滿十二歲之兒童須父母、師長或成年親友陪伴輔導觀賞)",
  "showDate": "2022/11/25",
  "showLength": "100",
  "title": "俠探特攻"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/fsen10370886/",
  "lastUpdete": "2022/11/18 01:19",
  "Picture": "http://app2.atmovies.com.tw/poster/fsen10370886/",
  "rate": "輔導級(未滿十五歲之人不得觀賞)",
  "showDate": "2022/11/25",
  "showLength": "92",
  "title": "大製片家"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/fcjp96051607/",
  "lastUpdete": "2022/11/18 01:19",
  "Picture": "http://app2.atmovies.com.tw/poster/fcjp96051607/",
  "rate": "輔導級(未滿十二歲之兒童不得觀賞)",
  "showDate": "2022/11/25",
  "showLength": "97",
  "title": "通往異世界的便利店"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/fdkr17494686/",
  "lastUpdete": "2022/11/18 01:19",
  "Picture": "http://app2.atmovies.com.tw/poster/fdkr17494686/",
  "rate": "保護級(未滿六歲之兒童不得觀賞，六歲以上未滿十二歲之兒童須父母、師長或成年親友陪伴輔導觀賞)",
  "showDate": "2022/11/25",
  "showLength": "100",
  "title": "音爆浩劫"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/fmen29764362/",
  "lastUpdete": "2022/11/18 01:19",
  "Picture": "http://app2.atmovies.com.tw/poster/fmen29764362/",
  "rate": "限制級(未滿十八歲之人不得觀賞)",
  "showDate": "2022/12/2",
  "showLength": "100",
  "title": "五星饗魘"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/fmkr23158500/",
  "lastUpdete": "2022/11/18 01:19",
  "Picture": "http://app2.atmovies.com.tw/poster/fmkr23158500/",
  "rate": "保護級(未滿六歲之兒童不得觀賞，六歲以上未滿十二歲之兒童須父母、師長或成年親友陪伴輔導觀賞)",
  "showDate": "2022/12/2",
  "showLength": "100",
  "title": "整形帝王"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/ftjp17382524/",
  "lastUpdete": "2022/11/18 01:19",
  "Picture": "http://app2.atmovies.com.tw/poster/ftjp17382524/",
  "rate": "保護級(未滿六歲之兒童不得觀賞，六歲以上未滿十二歲之兒童須父母、師長或成年親友陪伴輔導觀賞)",
  "showDate": "2022/12/2",
  "showLength": "120",
  "title": "通往夏天的隧道，再見的出口"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/fljp48367061//",
  "lastUpdete": "2022/11/18 01:19",
  "Picture": "http://app2.atmovies.com.tw/poster/fljp48367061/",
  "rate": "保護級(未滿六歲之兒童不得觀賞，六歲以上未滿十二歲之兒童須父母、師長或成年親友陪伴輔導觀賞)",
  "showDate": "2022/12/2",
  "showLength": "123",
  "title": "還有愛的日子"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/ften47322224/",
  "lastUpdete": "2022/11/18 01:19",
  "Picture": "http://app2.atmovies.com.tw/poster/ften47322224/",
  "rate": "普遍級(一般觀眾皆可觀賞)",
  "showDate": "2022/12/9",
  "showLength": "123",
  "title": "瘋狂富作用"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/fckr44546976/",
  "lastUpdete": "2022/11/18 01:22",
  "Picture": "http://app2.atmovies.com.tw/poster/fckr44546976/",
  "rate": "尚無電影分級資訊",
  "showDate": "2022/12/9",
  "showLength": "123",
  "title": "瘋狂富作用"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/fnkr42372938/",
  "lastUpdete": "2022/11/18 01:22",
  "Picture": "http://app2.atmovies.com.tw/poster/fnkr42372938/",
  "rate": "尚無電影分級資訊",
  "showDate": "2022/12/9",
  "showLength": "123",
  "title": "晝盲神探"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/ffjp18952724/",
  "lastUpdete": "2022/11/18 01:22",
  "Picture": "http://app2.atmovies.com.tw/poster/ffjp18952724/",
  "rate": "尚無電影分級資訊",
  "showDate": "2022/12/9",
  "showLength": "123",
  "title": "魚之子"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/faen01630029/",
  "lastUpdete": "2022/11/18 01:22",
  "Picture": "http://app2.atmovies.com.tw/poster/faen01630029/",
  "rate": "尚無電影分級資訊",
  "showDate": "2022/12/15",
  "showLength": "190",
  "title": "阿凡達：水之道"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/fsen10151854/",
  "lastUpdete": "2022/11/18 00:37",
  "Picture": "http://app2.atmovies.com.tw/poster/fsen10151854/",
  "rate": "尚無電影分級資訊",
  "showDate": "2022/12/21",
  "showLength": "119",
  "title": "沙贊！眾神之怒"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/flhk14032696/",
  "lastUpdete": "2022/11/18 00:37",
  "Picture": "http://app2.atmovies.com.tw/poster/flhk14032696/",
  "rate": "尚無電影分級資訊",
  "showDate": "2022/12/23",
  "showLength": "118",
  "title": "智齒"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/fasg55213138/",
  "lastUpdete": "2022/11/18 00:38",
  "Picture": "http://app2.atmovies.com.tw/poster/fasg55213138/",
  "rate": "普遍級(一般觀眾皆可觀賞)",
  "showDate": "2022/12/23",
  "showLength": "90",
  "title": "花路阿朱媽"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/fljp21816922/",
  "lastUpdete": "2022/11/18 00:38",
  "Picture": "http://app2.atmovies.com.tw/poster/fljp21816922/",
  "rate": "尚無電影分級資訊",
  "showDate": "2022/12/23",
  "showLength": "106",
  "title": "線，畫出的我"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/ffen14208870/",
  "lastUpdete": "2022/11/18 00:38",
  "Picture": "http://app2.atmovies.com.tw/poster/ffen14208870/",
  "rate": "尚無電影分級資訊",
  "showDate": "2022/12/30",
  "showLength": "106",
  "title": "法貝爾曼"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/fwen12193804/",
  "lastUpdete": "2022/11/18 00:38",
  "Picture": "http://app2.atmovies.com.tw/poster/fwen12193804/",
  "rate": "尚無電影分級資訊",
  "showDate": "2022/12/30",
  "showLength": "106",
  "title": "與你共舞"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/fnjp15625968/",
  "lastUpdete": "2022/11/18 00:38",
  "Picture": "http://app2.atmovies.com.tw/poster/fnjp15625968/",
  "rate": "尚無電影分級資訊",
  "showDate": "2023/01/6",
  "showLength": "106",
  "title": "夜鷹的單戀"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/fsen14458442/",
  "lastUpdete": "2022/11/18 00:38",
  "Picture": "http://app2.atmovies.com.tw/poster/fsen14458442/",
  "rate": "尚無電影分級資訊",
  "showDate": "2023/01/13",
  "showLength": "106",
  "title": "愛．子"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/fken58790086/",
  "lastUpdete": "2022/11/18 00:38",
  "Picture": "http://app2.atmovies.com.tw/poster/fken58790086/",
  "rate": "尚無電影分級資訊",
  "showDate": "2023/01/13",
  "showLength": "106",
  "title": "獵人克萊文"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/futw92659124/",
  "lastUpdete": "2022/11/18 00:38",
  "Picture": "http://app2.atmovies.com.tw/poster/futw92659124/",
  "rate": "尚無電影分級資訊",
  "showDate": "2023/01/13",
  "showLength": "106",
  "title": "我的婆婆怎麼把OO搞丟了"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/ftjp15242330/",
  "lastUpdete": "2022/11/18 00:38",
  "Picture": "http://app2.atmovies.com.tw/poster/ftjp15242330/",
  "rate": "尚無電影分級資訊",
  "showDate": "2023/01/13",
  "showLength": "100",
  "title": "灌籃高手"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/flen14668630/",
  "lastUpdete": "2022/11/18 00:38",
  "Picture": "http://app2.atmovies.com.tw/poster/flen14668630/",
  "rate": "尚無電影分級資訊",
  "showDate": "2023/01/20",
  "showLength": "100",
  "title": "鱷魚歌王"
},

{
  "hyperlink": "http://www.atmovies.com.tw/movie/fbjp96652581/",
  "lastUpdete": "2022/11/18 00:38",
  "Picture": "http://app2.atmovies.com.tw/poster/fbjp96652581/",
  "rate": "尚無電影分級資訊",
  "showDate": "2023/01/20",
  "showLength": "100",
  "title": "屁屁偵探 : 天才惡人屁屁亞蒂"
}

]

#doc_ref = db.collection("111").document("3420")
#doc_ref.set(doc)

collection_ref = db.collection("素清电影")
for doc in docs:
  collection_ref.add(doc)

