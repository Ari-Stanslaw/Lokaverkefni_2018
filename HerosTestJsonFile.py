import json

# Skilgreinum breytuna Heroes sem geymir dict (json hlut)
Heroes = {'hero':[{'name':'Moira','Role':'Support'},{'name':'Hanzo','Role':'Defense'}]}

# Skoðum innihald Heroes breytunnar - debug
# print(Heroes)


# dict key value 'hero' inniheldur lista
for i in Heroes['hero']:
    print("Name :", i['name'])# hver i er i raun gildi í listanum 'hero', getum hér notað key value 'name'


# auð lína
print()


# Bætum við hero..
Heroes['hero'].append({'name':'Roadhog','Role':'Tank'})

# Prentum lista með nýjum hero
for i in Heroes['hero']:
    print("Name :", i['name'])


# Skrifum i skránna Heroes.json, er ekkert að pæla í íslenskum stöfum en það er hægt.
with open("Heroes.json","w") as skra:
    # dump er fyrir skrár, dumps fyrir strengi
    json.dump(Heroes,skra)
# skra.close() þarf ekki




#Lesa_Heroes

# Þurfum þennan
import json

# Tengjumst við skránna Heroes.json (verður að vera til)
with open("Heroes.json","r") as skra:
    gogn = json.load(skra)

# with sér um að loka skránni, skra.close()

# Kíkjum i breytuna gogn
print(gogn)

# Þinn kóði hér til að sækja gögn úr dict (json)



#Heroes.json
{"Heroes": [
  {"Role": "Support", "name": "Moira"},
  {"Role": "Defense", "name": "Hanzo"},
  {"Role": "Tank", "name": "Roadhog"}
]}