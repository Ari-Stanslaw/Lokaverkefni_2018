# Þurfum þennan
import json

# Tengjumst við skránna Heroes.json (verður að vera til)
with open("Heroes.json","r") as skra:
    gogn = json.load(skra)

# with sér um að loka skránni, skra.close()

# Kíkjum i breytuna gogn
print(gogn)

# Þinn kóði hér til að sækja gögn úr dict (json)
