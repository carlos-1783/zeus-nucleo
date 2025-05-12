from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://zeuspanel02.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuración del sistema basada en el archivo JSON
sistema_config = {
    "agentes": ["Thalos", "Justicia", "Per-Seo", "Rafael"],
    "estado": {
        "núcleo": "abierto",
        "modo": "activo",
        "ssl": "activo",
        "interfaz_web": "activa",
        "interfaz_móvil": "preparada",
        "gpt4": "habilitado",
    },
}

# Modelos de entrada
class Cliente(BaseModel):
    nombre: str
    email: str

class Accion(BaseModel):
    agente: str
    comando: str

# Base de datos simulada
clientes = {}

@app.get("/")
def root():
    return {"status": "Zeus IA Núcleo activo"}

@app.post("/api/cliente")
def agregar_cliente(cliente: Cliente):
    clientes[cliente.email] = cliente.nombre
    return {"msg": f"Cliente {cliente.nombre} registrado"}

@app.post("/api/activar")
def activar_agente(accion: Accion):
    if accion.agente not in sistema_config["agentes"]:
        raise HTTPException(status_code=400, detail="Agente inválido")
    return {"msg": f"Agente {accion.agente} ejecutando comando: {accion.comando}"}

@app.get("/api/estado")
def obtener_estado():
    return {"estado_sistema": sistema_config["estado"]}

@app.get("/api/ejecutar")
def ejecutar_nocturno():
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"msg": f"Ejecución nocturna completada a las {hora}"}
