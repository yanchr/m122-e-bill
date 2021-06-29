import json
data = {}
data['object'] = []

def store_mail(mail_address, rechung_nummer):
    data['object'].append({
        'mail': mail_address,
        'rechnung_nummer': rechung_nummer,
    })

    print('store:' + mail_address)

    with open('temp-files/json/data.json', 'w') as outfile:
        json.dump(data, outfile)

def get_mail_from_rechnung_nummer(rechnung_nummer):
    json_file = open('temp-files/json/data.json',)
    data = json.load(json_file)

    for object in data['object']:
        if (object['rechnung_nummer'] == rechnung_nummer):
            return object['mail']

    json_file.close()
    #print(rechnung_nummer)


#store_mail('yanick.christen@gmail.com', '12')    