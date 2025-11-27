import json
import os

class BaseModel:
    arquivo = "carros.json"

    def salvar(self, dados):
        #1 = Lê todos os dados novos
        lista = self.carregar_dados()
        #2 - Adicionar os dados novos
        lista.append(dados)
        # 3 - Reescrever tudo (write)
        with open(self.arquivo, "w", encoding="utf-8") as f: 
            json.dump(lista,f, indent=4, ensure_ascii=False)
    
    def carregar_dados(self):
        # Se o arquivo ainda nao existe, começamos com uma lista vazia
        if not os.path.exists(self.arquivo):
            return []
        
        # Caso exista, carregamos tudo
        with open(self.arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
