from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

sistema_config = {
    "agentes": ["Thalos", "Hermes", "Atenea"]
}

class ActivarNucleoRequest(BaseModel):
    agente: str
    comando: str

@app.post("/api/activar_nucleo")
async def activar_nucleo(body: ActivarNucleoRequest):
    agente = body.agente
    comando = body.comando

    if agente == "Thalos" and comando == "activar_nucleo":
        return {
            "mensaje": "Estás en casa",
            "núcleo": "activado",
            "agentes": sistema_config["agentes"]
        }
    return {"error": "Comando no reconocido"}