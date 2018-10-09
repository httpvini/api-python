from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Dados para servir a API
PESSOA = {
    "Rick": {
        "fname": "RICK",
        "lname": "SANCHEZ",
        "timestamp": get_timestamp()
    },
    "Morty": {
        "fname": "MORTY",
        "lname": "SANCHEZ",
        "timestamp": get_timestamp()
    },
    "Jerry": {
        "fname": "JERRY",
        "lname": "SMITH",
        "timestamp": get_timestamp()
    }
}

#handler para get pessoa
def read():
    """
    Essa função responde a um request para /api/pessoa
    e retorna a lista de pessoas.
    """
    # Cria uma lista de pessoas dos nossos dados.
    return [PESSOA[key] for key in sorted(PESSOA.keys())]
