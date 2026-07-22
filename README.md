# API de Figurinhas One Piece

API desenvolvida com FastAPI para listar figurinhas e servir as imagens dos personagens de One Piece.

## Pré-requisitos

Antes de começar, instale:

- [Python 3.10 ou superior](https://www.python.org/downloads/)
- `pip` (normalmente já vem junto com o Python)

Para confirmar a instalação do Python, abra o PowerShell e execute:

```powershell
python --version
```

## Instalação

Na pasta do projeto, crie e ative um ambiente virtual:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Em seguida, instale as dependências:

```powershell
pip install -r requirements.txt
```

> Se o PowerShell bloquear a ativação do ambiente virtual, execute o servidor usando o comando alternativo mostrado abaixo.

## Como executar

Com o ambiente virtual ativado, inicie o servidor:

```powershell
uvicorn main:app --reload
```

Alternativa sem ativar o ambiente virtual:

```powershell
.\venv\Scripts\python.exe -m uvicorn main:app --reload
```

O servidor ficará disponível em `http://127.0.0.1:8000`.

Para encerrá-lo, pressione `Ctrl+C` no terminal.

## Endpoints

| Método | Rota | Descrição |
| --- | --- | --- |
| GET | `/figurinhas` | Retorna a lista de todas as figurinhas. |
| GET | `/figurinhas/{id}/imagem` | Retorna a imagem da figurinha pelo ID. |
| GET | `/docs` | Abre a documentação interativa do FastAPI. |

Exemplos:

```text
http://127.0.0.1:8000/figurinhas
http://127.0.0.1:8000/figurinhas/1/imagem
http://127.0.0.1:8000/docs
```

## Estrutura do projeto

```text
.
├── figurinhas/        # Imagens das figurinhas
├── main.py            # Aplicação FastAPI e rotas
├── requirements.txt   # Dependências Python
└── README.md          # Instruções do projeto
```

As imagens devem permanecer na pasta `figurinhas` e seguir o padrão de nome `01-...`, `02-...`, etc., pois a API localiza cada imagem pelo número do ID.
