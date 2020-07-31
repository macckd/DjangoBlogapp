from __future__ import unicode_literals
import standalone
import datetime
standalone.run('icoder.settings')
import json
import requests
from django.db import connection
from home.models import BagicApiData
import urllib.parse

class KJData():
        url = {'mh':'https://marathi.krishijagran.com/api/categories/rss',
               'hi':'https://hindi.krishijagran.com/api/categories/rss',
               'ka':'https://kannada.krishijagran.com/api/categories/rss'}

        querystring = {"key": "5e89ea26-ef57-4ab0-bd48-58b03a1466cb", "related": "1"}
        headers = {
            'cache-control': "no-cache",
            'postman-token': "ab935326-96c9-baa8-ddc8-3d94d0c68fcf"
        }
        id_data=datetime.datetime.now()
        print(id_data)
        checkStatus = 0


        for z,y in url.items():
                response = requests.request("GET", y, headers=headers, params=querystring)
                data = json.loads(response.text)
                print(data)
                for item in data:
                        category = item.get("category")
                        cat_id = item.get("id")
                        for x in item.get("news"):
                                news_contact = x.get("contact")
                                news_coverImage = urllib.parse.unquote(x.get("coverImage"))
                                news_datePublished = x.get("datePublished")
                                news_id = x.get("id")
                                news_summary = x.get("summary")
                                news_title = x.get("title")
                                news_url = x.get("url")
                                identifier = id_data
                                lang_code = z
                                checkStatus = +1
                                created = BagicApiData(cat_id=cat_id, category=category, news_id=news_id, news_title=news_title,news_coverImage=news_coverImage,
                                                news_datePublished=news_datePublished, news_summary=news_summary, news_url=news_url, news_contact=news_contact,
                                                identifier=identifier, lang_code=lang_code)
                                created.save()


        if checkStatus > 0:
            deletesql = "delete from home_bagicapidata where identifier !='%s'" % id_data
            print(deletesql)
            cursor = connection.cursor()
            cursor.execute(deletesql)
        print("Finish")