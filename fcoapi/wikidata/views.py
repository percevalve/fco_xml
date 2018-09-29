import json
import requests
import pandas as pd
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import filename2wikidataurl, ambfilter



class WikiDetailsAPI(APIView):

  def get(self, request, entity_id):

    entityID = entity_id
    url = "https://www.wikidata.org/wiki/Special:EntityData/{}.json".format(entityID)

    response = requests.get(url)
    content = json.loads(response.content)
    img_filename = content["entities"][entityID]["claims"]["P18"][0]["mainsnak"]["datavalue"]["value"]
    img_url = filename2wikidataurl(img_filename)
    return Response({"img_url": img_url})


class PersonPickerAPI(APIView):


  def get(self, request, keyword=None):
    # return Response(keyword)
    suggestions = ambfilter(keyword)
    return Response(suggestions)