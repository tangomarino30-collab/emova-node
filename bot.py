import requests, os

CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']
TELEGRAM_CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": mensaje})

url = f"https://apitransporte.buenosaires.gob.ar/subtes/serviceAlerts?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&json=1"
data = requests.get(url).json()
alertas = data.get("entity", [])

if not alertas:
    enviar_telegram("✅ Subte sin alertas activas")
else:
    for e in alertas:
        alerta = e.get("alert", {})
        texto = alerta.get("header_text", {}).get("translation", [{}])[0].get("text", "")
        linea = alerta.get("informed_entity", [{}])[0].get("route_id", "?")
        enviar_telegram(f"🚇 Línea {linea}: {texto}")
