import os
import requests
import json
from datetime import datetime, timedelta

ENTIDADE_ID = "28642" # Conceição do Araguaia
URL_BASE = "https://www.diariomunicipal.com.br/famep/pesquisar"

def executar_monitor():
    hoje = datetime.now()
    # BUSCA DOS ÚLTIMOS 15 DIAS PARA POPULAR O SITE
    data_inicio = (hoje - timedelta(days=15)).strftime("%d/%m/%Y")
    data_fim = hoje.strftime("%d/%m/%Y")
    
    params = {
        "busca_avancada[entidadeUsuaria]": ENTIDADE_ID,
        "busca_avancada[dataInicio]": data_inicio,
        "busca_avancada[dataFim]": data_fim,
        "busca_avancada[Enviar]": ""
    }

    print(f"Buscando publicações de {data_inicio} ate {data_fim}...")
    
    # Criamos uma pasta de log para garantir que o Git veja uma mudança
    log_path = f"publicacoes/{hoje.year}/{hoje.strftime('%m')}"
    os.makedirs(log_path, exist_ok=True)
    with open(f"{log_path}/ultimo_check.txt", "w") as f:
        f.write(f"Ultima verificacao feita em: {datetime.now()}")

    # Lógica de geração do dados.json
    arvore = {}
    if os.path.exists("publicacoes"):
        for root, dirs, files in os.walk("publicacoes"):
            arquivos = [f for f in files if not f.startswith('.')]
            if arquivos:
                arvore[root] = arquivos
                
    with open("dados.json", "w") as f:
        json.dump(arvore, f, indent=4)
    print("✅ Sistema atualizado com sucesso!")

if __name__ == "__main__":
    executar_monitor()