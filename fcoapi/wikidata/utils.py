import requests
import json
import pandas as pd
import hashlib


def filename2wikidataurl(filename):
  filename = filename.replace(" ", "_")

  filename_md5 = hashlib.md5(filename.encode("utf-8")).hexdigest()

  filename_url = "https://upload.wikimedia.org/wikipedia/commons/{first}/{first}{second}/{filename}" \
                      .format(first=filename_md5[0], second=filename_md5[1], filename=filename) 

  return filename_url
                    

def ambfilter(keyword):
  keyword = keyword.lower()
  # response = requests.get('https://query.wikidata.org/sparql?format=json&query=%23%20Wikidata%20entries%20for%20British%20ambassadors%20and%20high%20commissioners%0A%23%20all%20people%20who%20held%20at%20least%20one%20such%20position%0A%23%20one%20line%20per%20position%20held%20%28so%20many%20people%20appear%20repeatedly%29%0A%23%20start%2Fend%20dates%20for%20that%20particular%20position%0A%0Aselect%20distinct%20%3Fperson%20%3FpersonLabel%20%3FpositionLabel%20%3Fstartyear%20%3Fendyear%20%3Fbirthyear%20%3Fdeathyear%20%3Fimage%20%3FotherpositionLabel%20%3Fotherstartyear%20%3Fotherendyear%20where%0A%7B%0A%20%20%7B%20%3Fposition%20wdt%3AP31%20wd%3AQ18115939%20.%20%7D%20union%20%7B%20%3Fposition%20wdt%3AP31%20wd%3AQ56760832%20%7D%20.%20%23%20position%20is%20UK%20ambassador%20or%20high%20commissioner%0A%20%20%20%20%0A%20%20%20%20%3Fperson%20p%3AP39%20%3FpositionStatement%20.%20%3FpositionStatement%20ps%3AP39%20%3Fposition%20.%20%23%20find%20positions%20they%20held%0A%20%20%7B%20%3Fperson%20wdt%3AP18%20%3Fimage%20.%20%7D%20.%20%20%0A%20%20%20%20optional%20%7B%20%3FpositionStatement%20pq%3AP580%20%3Fstart%20.%20bind%28year%28%3Fstart%29%20as%20%3Fstartyear%29%20%7D%20%23%20id%20start%20year%0A%20%20%20%20optional%20%7B%20%3FpositionStatement%20pq%3AP582%20%3Fend%20.%20bind%28year%28%3Fend%29%20as%20%3Fendyear%29%20%7D%20%23%20id%20end%20year%0A%20%20%20%20optional%20%7B%20%3Fperson%20wdt%3AP569%20%3Fborn%20.%20bind%28year%28%3Fborn%29%20as%20%3Fbirthyear%29%20%7D%20%23%20id%20start%20year%0A%20%20%20%20optional%20%7B%20%3Fperson%20wdt%3AP570%20%3Fdied%20.%20bind%28year%28%3Fdied%29%20as%20%3Fdeathyear%29%20%7D%20%23%20id%20end%20year%0A%20%20%20%20optional%20%7B%20%3Fperson%20p%3AP39%20%3FotherpositionStatement%20.%20%3FotherpositionStatement%20ps%3AP39%20%3Fotherposition%20.%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20filter%20not%20exists%20%7B%20%3Fotherposition%20wdt%3AP31%20wd%3AQ18115939%20.%20%7D%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20filter%20not%20exists%20%7B%20%3Fotherposition%20wdt%3AP31%20wd%3AQ56760832%20.%20%7D%20%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20optional%20%7B%20%3FotherpositionStatement%20pq%3AP580%20%3Fotherstart%20.%20bind%28year%28%3Fotherstart%29%20as%20%3Fotherstartyear%29%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20optional%20%7B%20%3FotherpositionStatement%20pq%3AP580%20%3Fotherend%20.%20bind%28year%28%3Fotherend%29%20as%20%3Fotherendyear%29%20%7D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%7D%0A%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%22.%20%7D%0A%7D')
  # content = json.loads(response.content)  
  content = json.loads(open('wikidata/ambassadors.json').read())
  content = content["results"]["bindings"]
  results = []
  # "vars" : [ "person", "personLabel", "positionLabel", "startyear", "endyear" ]
  for row in content:
    print(row)
    # results.append(row)
    if row["personLabel"]["value"].lower().find(keyword) != -1:
      results.append(
        {
          "person": row["person"]["value"],
          "personLabel": row["personLabel"]["value"],
          "positionLabels": row["positionLabels"]
          # "img_url": filename2wikidataurl(row["person"]["value"])
          # "startyear": row["startyear"]["value"],
          # "endyear": row["endyear"]["value"],
        }
      )

      if "positionLabel" in row:
        results[-1].update({"positionLabel": row["positionLabel"]["value"]})

      if "startyear" in row:
        results[-1].update({"startyear": row["startyear"]["value"]})

      if "endyear" in row:
        results[-1].update({"endyear": row["endyear"]["value"]})

      if "otherPositions" in row:
        results[-1].update({"otherPositions": row["otherPositions"]})

      if "image" in row:
        results[-1].update({"img_url": row["image"]["value"]})


  # result_records = pd.DataFrame.from_records(results)
  # result_records.query("'personLabel' ")
  return results

  # pd.DataFrame.from_records(section_b_lines)



