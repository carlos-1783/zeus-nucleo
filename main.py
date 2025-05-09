from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# CORS para conectar con React/Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Base de datos simulada (puedes conectar PostgreSQL de Railway)
clientes = {}

class Cliente(BaseModel):
    nombre: str
    email: str
    servicios: list[str]

class Accion(BaseModel):
    agente: str
    comando: str

@app.get("/")
def root():
    return {"status": "Zeus IA Núcleo activo"}

@app.post("/api/cliente")
def agregar_cliente(cliente: Cliente):
    clientes[cliente.email] = cliente
    return {"msg": f"Cliente {cliente.nombre} registrado"}

@app.post("/api/activar")
def activar_agente(accion: Accion):
    if accion.agente not in ["PER-SEO", "RAFAEL", "THALOS", "JUSTICIA"]:
        raise HTTPException(status_code=400, detail="Agente inválido")
    return {"msg": f"Agente {accion.agente} ejecutando comando: {accion.comando}"}

@app.get("/api/ejecutar")
def ejecutar_nocturno():
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"msg": f"Ejecución nocturna completada a las {hora}"}
