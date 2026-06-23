from fastapi import FastAPI
import requests
import random

url_bestemmie = "https://raw.githubusercontent.com/BaoloLabs/BaoloLabs.github.io/refs/heads/main/lista.json" # Per gentil concessione di BaoloLabs
lista_bestemmie = requests.get(url_bestemmie).json()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Benvenuto nella root di porconi-as-a-service! Se vuoi fare una richiesta, usa l'endpoint /bestemmia."}

@app.get("/bestemmia")
async def risposta_bestemmia():
    return {"message": lista_bestemmie[random.randint(0, len(lista_bestemmie) - 1)]}
