import os, requests, json
from datetime import datetime

ENTIDADE_ID = "28642" # CDA
URL_BASE = "https://www.diariomunicipal.com.br/famep/pesquisar"

def executar():
    hoje = datetime.now()
    data_str = hoje.strftime('%d/%m/%Y')
    print(f"Monitorando FAMEP - CDA: {data_str}")
    
    # Define o caminho da pasta de hoje
    caminho_dia = f"publicacoes/{hoje.year}/{hoje.strftime('%m')}/{hoje.strftime('%d')}"
    os.makedirs(caminho_dia, exist_ok=True)

    # Aqui você pode remover o arquivo de teste se ele existir
    teste_file = os.path.join(caminho_dia, "ultimo_check.txt")
    if os.path.exists(teste_file):
        os.remove(teste_file)

    # Lógica para atualizar o índice dados.json
    arvore = {}
    if os.path.exists("publicacoes"):
        for root, dirs, files in os.walk("publicacoes"):
            # Filtra apenas arquivos úteis (PDFs)
            arquivos = [f for f in files if f.endswith('.pdf')]
            if arquivos:
                # Ajusta o caminho para o formato do site
                caminho_formatado = root.replace("\\", "/")
                arvore[caminho_formatado] = arquivos
                
    with open("dados.json", "w", encoding="utf-8") as f:
        json.dump(arvore, f, indent=4, ensure_ascii=False)
    
    print("✅ Índice atualizado com sucesso!")

if __name__ == "__main__":
    executar()