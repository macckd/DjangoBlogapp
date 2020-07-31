from __future__ import unicode_literals

from typing import Dict, List, Any

import row as row
import standalone
import datetime
standalone.run('icoder.settings')
import json
import requests
from django.db import connection
from home.models import BagicApiData
import urllib.parse

'''
cursor = connection.cursor()
cursor.execute("""SELECT * FROM home_bagicapidata where lang_code='MH'""")
out = cursor.fetchall()
variable = {key:val for key,val in out}
print(out)

a = BagicApiData.objects.all()
for all in a:
    kj_as_dict = {'cat_id': all.cat_id, 'category': all.category,
                  'news': {'news_id':all.news_id, 'news_title': all.news_title,
                           'news_datePublished': all.news_datePublished, 'news_summary':all.news_summary,
                           'news_url': all.news_url, 'news_coverImage': all.news_coverImage,
                           'news_contact': all.news_contact, 'lang_code': all.lang_code} }
    json_data = json.dumps(kj_as_dict , ensure_ascii=False)
    print(json_data)


a = "SELECT * FROM home_bagicapidata where lang_code='mh'"
cursor = connection.cursor()
cursor.execute(a)
records = cursor.fetchall()
for row in records:
    kj_as_dict = {'cat_id': row[1], 'category': row[2],
                  'news': {'news_id':row[4], 'news_title': row[5],
                           'news_datePublished': row[3], 'news_summary':row[6],
                           'news_url': row[7], 'news_coverImage': row[9],
                           'news_contact': row[8], 'lang_code': row[12]} }
    json_data = json.dumps(kj_as_dict , ensure_ascii=False)
    print(json_data)
    

a = "SELECT * FROM home_bagicapidata where lang_code='mh'"
cursor = connection.cursor()
cursor.execute(a)
records = cursor.fetchall()

rt = {'MH':'MH', 'sp':'spp'}
p = {}
p["values"] = []
students = p["values"]
for row in records:
    for key in rt:
        p[rt[key]] = {"lang": rt[key]}
        values.append(rt)

        print(p)
        
a = "SELECT * FROM home_bagicapidata where lang_code='mh'"
cursor = connection.cursor()
cursor.execute(a)
records = cursor.fetchall()
jsonstring = {}
for row in records:
    jsonstring["MH"] = {"lang": "MH", "values": [{"key": row[1], "value": row[5]}]}
    jsonstring["AP"] = {"lang": "AP", "values": [{"key": row[1], "value": row[3]}]}
    jsonstring["KA"] = {"lang": "KA", "values": [{"key": row[1], "value": row[4]}]}
    jsonstring["HN"] = {"lang": "HN", "values": [{"key": row[1], "value": row[6]}]}
    print(jsonstring)

    #print
    
a = "SELECT * FROM home_bagicapidata where lang_code='mh'"
cursor = connection.cursor()
cursor.execute(a)
records = cursor.fetchall()
for row in records:
    reste ={}
    list =[]
    test_keys = [row[1]]
    test_values = [row[3]]
    rest = ({test_keys[i]: test_values[i] for i in range(len(test_keys))})
    list.append(rest)
    reste.update(list)
'''


key_list=[1,2]
value_list=['a','b','c','d']


new_dict={}
if len(key_list) != 0 and len(value_list) != 0 and len(key_list) == len(value_list):
        for i in range(min(len(key_list), len(value_list))):
            new_dict[key_list[i]] = value_list[i]
print(new_dict)
# itrate list value in till 3
test_list = [("key", "value")]
K = 3
res = [ele for ele in test_list for i in range(K)]

# printing result
print("The list after adding elements :  " + str(res))

sql = "SELECT * FROM bagic_app_string"
                cursor = connection.cursor()
                cursor.execute(sql)
                records = cursor.fetchall()
                test_keys = [i[1] for i in records]
                test_values_AP = [i[3] for i in records]
                test_values_KA = [i[4] for i in records]
                test_values_MH = [i[5] for i in records]
                test_values_HN = [i[6] for i in records]
                rest_AP = ({test_keys[i]: test_values_AP[i] for i in range(len(test_keys))})
                rest_MH = ({test_keys[i]: test_values_MH[i] for i in range(len(test_keys))})
                rest_HN = ({test_keys[i]: test_values_HN[i] for i in range(len(test_keys))})
                rest_KA = ({test_keys[i]: test_values_KA[i] for i in range(len(test_keys))})
                test_list = [("key", "value")]
                K = 100
                list_1 = [ele for ele in test_list for i in range(K)]
                list_AP = rest_AP.items()
                list_MH = rest_MH.items()
                list_HN = rest_HN.items()
                list_KA = rest_KA.items()
                dic_AP = [dict(zip(*z)) for z in zip(list_1, list_AP)]
                dic_MH = [dict(zip(*z)) for z in zip(list_1, list_MH)]
                dic_HN = [dict(zip(*z)) for z in zip(list_1, list_HN)]
                dic_KA = [dict(zip(*z)) for z in zip(list_1, list_KA)]
                jsonstring["AP"] = {"langid": "AP", "values": dic_AP}
                jsonstring["MH"] = {"langid": "MH", "values": dic_MH}
                jsonstring["HN"] = {"langid": "HN", "values": dic_HN}
                jsonstring["KA"] = {"langid": "KA", "values": dic_KA}

