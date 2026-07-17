import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import glob
import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Configura o serviço de arquivos estáticos montando a pasta de imagens na rota
app.mount("/imgs", StaticFiles (directory=PASTA_IMAGENS), name="imgs")

# Lista de figurinhas de exemplo da API
figurinhas = [
    {"id": 1, "nome": "Monkey D. Luffy", "categoria": "EAST BLUE", "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2, "nome": "Roronoa Zoro", "categoria": "EAST BLUE", "imagem_url": "/figurinhas/2/imagem"},
    {"id": 3, "nome": "Nami", "categoria": "EAST BLUE", "imagem_url": "/figurinhas/3/imagem"},
    {"id": 4, "nome": "Usopp", "categoria": "EAST BLUE", "imagem_url": "/figurinhas/4/imagem"},
    {"id": 5, "nome": "Sanji", "categoria": "EAST BLUE", "imagem_url": "/figurinhas/5/imagem"},
    {"id": 6, "nome": "Franky", "categoria": "TRIPULAÇÃO", "imagem_url": "/figurinhas/6/imagem"},
    {"id": 7, "nome": "Nico Robin", "categoria": "TRIPULAÇÃO", "imagem_url": "/figurinhas/7/imagem"},
    {"id": 8, "nome": "Tony Chopper", "categoria": "TRIPULAÇÃO", "imagem_url": "/figurinhas/8/imagem"},
    {"id": 9, "nome": "Brook", "categoria": "TRIPULAÇÃO", "imagem_url": "/figurinhas/9/imagem"},
    {"id": 10, "nome": "Jinbe", "categoria": "TRIPULAÇÃO", "imagem_url": "/figurinhas/10/imagem"},
    {"id": 11, "nome": "Shanks", "categoria": "ALIADOS", "imagem_url": "/figurinhas/11/imagem"},
    {"id": 12, "nome": "Sabo", "categoria": "ALIADOS", "imagem_url": "/figurinhas/12/imagem"},
    {"id": 13, "nome": "Portgas D. Ace", "categoria": "ALIADOS", "imagem_url": "/figurinhas/13/imagem"},
    {"id": 14, "nome": "Trafalgar D. Water Law", "categoria": "ALIADOS", "imagem_url": "/figurinhas/14/imagem"},
    {"id": 15, "nome": "Boa Hancock", "categoria": "ALIADOS", "imagem_url": "/figurinhas/15/imagem"},
    {"id": 16, "nome": "Marshall D. Teach", "categoria": "IMPERADORES", "imagem_url": "/figurinhas/16/imagem"},
    {"id": 17, "nome": "Kaido", "categoria": "IMPERADORES", "imagem_url": "/figurinhas/17/imagem"},
    {"id": 18, "nome": "Charlotte Linlin", "categoria": "IMPERADORES", "imagem_url": "/figurinhas/18/imagem"},
    {"id": 19, "nome": "Donquixote Doflamingo", "categoria": "IMPERADORES", "imagem_url": "/figurinhas/19/imagem"},
    {"id": 20, "nome": "Crocodile", "categoria": "IMPERADORES", "imagem_url": "/figurinhas/20/imagem"},
    {"id": 21, "nome": "Monkey D. Garp", "categoria": "MARINHA", "imagem_url": "/figurinhas/21/imagem"},
    {"id": 22, "nome": "Sengoku", "categoria": "MARINHA", "imagem_url": "/figurinhas/22/imagem"},
    {"id": 23, "nome": "Dracule Mihawk", "categoria": "MARINHA", "imagem_url": "/figurinhas/23/imagem"},
    {"id": 24, "nome": "Smoker", "categoria": "MARINHA", "imagem_url": "/figurinhas/24/imagem"},
    {"id": 25, "nome": "Koby", "categoria": "MARINHA", "imagem_url": "/figurinhas/25/imagem"},
    {"id": 26, "nome": "Gol D. Roger", "categoria": "LENDAS", "imagem_url": "/figurinhas/26/imagem"},
    {"id": 27, "nome": "Silvers Rayleigh", "categoria": "LENDAS", "imagem_url": "/figurinhas/27/imagem"},
    {"id": 28, "nome": "Edward Newgate", "categoria": "LENDAS", "imagem_url": "/figurinhas/28/imagem"},
    {"id": 29, "nome": "Kozuki Oden", "categoria": "LENDAS", "imagem_url": "/figurinhas/29/imagem"},
    {"id": 30, "nome": "Eustass Kid", "categoria": "LENDAS", "imagem_url": "/figurinhas/30/imagem"},
]


@app.get("/figurinhas")
def listar_figurinhas():
    # Retorna a lista de figurinhas
    return figurinhas


@app.get("/figurinhas/{id}/imagem")
def obter_imagem(id: int):
    arquivos = glob.glob(os.path.join(PASTA_IMAGENS, f"{id:02d}-*"))

    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")

    return FileResponse(arquivos[0])
