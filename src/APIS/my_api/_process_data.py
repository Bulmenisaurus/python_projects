import json

with open('emoticons.json') as f:
    data: list = json.load(f)
    new_data = []

    for face in data:
        del face['expression']
        del face['face_id']

        if not face.get('isAscii'):
            face['isAscii'] = face['face'].isascii()

        if not face.get('length'):
            face['length'] = len(face['face'])

        new_data.append(face)

with open('emoticons.json', 'w') as f:
    json.dump(new_data, f, indent=4)