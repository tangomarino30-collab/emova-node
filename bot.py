import requests, os




if not alertas:
    enviar_telegram("✅ Subte sin alertas activas")
else:
    for e in alertas:
        alerta = e.get("alert", {})
        texto = alerta.get("header_text", {}).get("translation", [{}])[0].get("text", "")
        linea = alerta.get("informed_entity", [{}])[0].get("route_id", "?")
        enviar_telegram(f"🚇 Línea {linea}: {texto}")
