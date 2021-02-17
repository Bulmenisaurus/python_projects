import json


with open('my_api_data.json') as f:
    data = json.load(f)

    new_data = []

    for expression_type in data:
        expression = expression_type['expression']
        for face in expression_type['faces']:
            face['expression'] = expression
            new_data.append(face)

    print(new_data)

with open('emoticons.json', 'w') as f:
    f.write(json.dumps(new_data, indent=4))
