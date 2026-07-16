import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Define os caminhos absolutos para encontrar a pasta de imagens de forma robusta
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Configura o serviço de arquivos estáticos montando a pasta de imagens na rota
app.mount("/imgs", StaticFiles (directory=PASTA_IMAGENS), name="imgs")

# Lista de figurinhas de exemplo da API
figurinhas = [
    {"id": 1,
        "nome": "Monkey D. Luffy", 
        "categoria": "EAST BLUE",
        "imagem_url": "/imgs/01-monkey-d-luffy.jpg"
    },

    {"id": 2,
        "nome": "Roronoa Zoro", 
        "categoria": "EAST BLUE",
        "imagem_url": "/imgs/02-roronoa-zoro.jpg"
    },
    {"id": 3,
        "nome": "Nami", 
        "categoria": "EAST BLUE",
        "imagem_url": "/imgs/03-nami.jpg"
    },
    {"id": 4,
    "nome": "Usopp", 
    "categoria": "EAST BLUE",
    "imagem_url": "/imgs/04-usopp.jpg"
    },
    {"id": 5,
        "nome": "Sanji", 
        "categoria": "EAST BLUE",
        "imagem_url": "/imgs/05-sanji.jpg"    
    },
    {"id": 6,
        "nome": "Franky", 
        "categoria": "TRIPULAÇÃO",
        "imagem_url": "/imgs/06-franky.jpg"  
    },
    {"id": 7,
        "nome": "Nico Robin", 
        "categoria": "TRIPULAÇÃO",
        "imagem_url": "/imgs/07-nico-robin.jpg"
    },
    {"id": 8,
        "nome": "Tony Chopper", 
        "categoria": "TRIPULAÇÃO",
        "imagem_url": "/imgs/08-tony-chopper.jpg"
    },
    {"id": 9,
        "nome": "Brook", 
        "categoria": "TRIPULAÇÃO",
        "imagem_url": "/imgs/09-brook.jpg"
    },
    {"id": 10,
        "nome": "Jinbe", 
        "categoria": "TRIPULAÇÃO",
        "imagem_url": "/imgs/10-jinbe.jpg"
    },
    {"id": 11,
        "nome": "Shanks", 
        "categoria": "ALIADOS",
        "imagem_url": "/imgs/11-shanks.jpg"
    },
    {"id": 12,
        "nome": "Sabo", 
        "categoria": "ALIADOS",
        "imagem_url": "/imgs/12-sabo.jpg"
    },
    {"id": 13,
        "nome": "Portgas D. Ace", 
        "categoria": "ALIADOS",
        "imagem_url": "/imgs/13-portgas-d-ace.jpg"
    },
    {"id": 14,
        "nome": "Trafalgar D. Water Law", 
        "categoria": "ALIADOS",
        "imagem_url": "/imgs/14-trafalgar-d-water-law.jpg"
    },
    {"id": 15,
        "nome": "Boa Hancock", 
        "categoria": "ALIADOS",
        "imagem_url": "/imgs/15-boa-hancock.jpg"
    },
    {"id": 16,
        "nome": "Marshal D. Teach", 
        "categoria": "IMPERADORES",
        "imagem_url": "/imgs/16-marshal-d-teach.jpg"
    },
    {"id": 17,
        "nome": "Kaido", 
        "categoria": "IMPERADORES",
        "imagem_url": "/imgs/17-kaido.jpg"
    },
    {"id": 18,
        "nome": "Charlotte Katakuri", 
        "categoria": "IMPERADORES",
        "imagem_url": "/imgs/18-charlotte-katakuri.jpg"
    },
    {"id": 19,
        "nome": "Donquixote Doflamingo", 
        "categoria": "IMPERADORES",
        "imagem_url": "/imgs/19-donquixote-doflamingo.jpg"
    },
    {"id": 20,
        "nome": "Crocodile", 
        "categoria": "IMPERADORES",
        "imagem_url": "/imgs/20-crocodile.jpg"
    },
    {"id": 21,
        "nome": "Monkey D. Garp", 
        "categoria": "MARINHA",
        "imagem_url": "/imgs/21-monkey-d-garp.jpg"
    },
    {"id": 22,
        "nome": "Sengoku", 
        "categoria": "MARINHA",
        "imagem_url": "/imgs/22-sengoku.jpg"
    },
    {"id": 23,
        "nome": "Dracule Mihawk", 
        "categoria": "MARINHA",
        "imagem_url": "/imgs/23-dracule-mihawk.jpg"
    },
    {"id": 24,
        "nome": "Smoker", 
        "categoria": "MARINHA",
        "imagem_url": "/imgs/24-smoker.jpg"
    },
    {"id": 25,
        "nome": "Koby", 
        "categoria": "MARINHA",
        "imagem_url": "/imgs/25-koby.jpg"
    },
    {"id": 26,
        "nome": "Gol d roger", 
        "categoria": "LENDAS",
        "imagem_url": "/imgs/26-gol-d-roger.jpg"
    },
    {"id": 27,
        "nome": "Silvers Rayleigh", 
        "categoria": "LENDAS",
        "imagem_url": "/imgs/27-silvers-rayleigh.jpg"
    },
    {"id": 28,
        "nome": "Edward Newgate", 
        "categoria": "LENDAS",
        "imagem_url": "/imgs/28-edward-newgate.jpg"
    },
    {"id": 29,
        "nome": "Kozuki Oden", 
        "categoria": "LENDAS",
        "imagem_url": "/imgs/29-kozuki-oden.jpg"
    },
    {"id": 30,
        "nome": "Eustass Kid", 
        "categoria": "LENDAS",
        "imagem_url": "/imgs/30-eustass-kid.jpg"
    },
]

# Define a rota raiz que lista todas as figurinhas
@app.get('/figurinhas')
def listar_figurinhas():
    # Retorna a lista de figurinhas
    return figurinhas

