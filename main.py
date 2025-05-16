@app.get("/")
def root():
    sistema_config["estado"]["núcleo"] = "activado"
    return {
        "status": "Zeus IA Núcleo activo",
        "mensaje": "Estás en casa",
        "núcleo": "activado",
        "agentes": sistema_config["agentes"]
    }

