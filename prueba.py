
import re
def limpiarJSON(text):
    #text = 'Entendido, José. Aquí te dejo una opción de desayuno de aproximadamente 658 calorías que puedes consumir para ayudarte a bajar de peso:```json{  "desayuno": [    {      "alimento": "Huevos revueltos con espinacas",      "porcion": "2 huevos",      "calorias": 200    },    {      "alimento": "Pan integral tostado con aguacate",      "porcion": "2 rebanadas de pan",      "calorias": 458    }  ]}```Este desayuno incluye huevos revueltos con espinacas, que son ricos en proteínas y fibra, y pan integral tostado con aguacate, que proporciona gras'
    regex = "\```(.*?)\```"
    result = re.findall(regex, text)
    result = result[0]
    result = result.replace("json", "")
    result = result.replace("['", "").replace("']", "")
    return result
