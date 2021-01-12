import base64
import random
import json
import itertools

# in order for each face: value, expression, length. isAsci and length are added automatically

f = open("/src/APIS/my_api/my_api_data.json", "r")
emoticon_python = json.load(f)
f.close()

print(emoticon_python)

api_url = input("Api url:\n https://lmao.myapi.omnom/")

all_faces = list(itertools.chain(*[[i['face'] for i in x['faces']] for x in emoticon_python]))
if api_url == 'random':
    print(random.choice(all_faces))

