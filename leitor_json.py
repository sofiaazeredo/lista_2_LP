"""
Created on Sun Sep  8 07:53:43 2024

@author: sofia
"""
import modulo
import json
import pprint

while True:
    try:
        # Recebe input do usuário e aplica a função
        file = input("Insira o arquivo json que deve ser reproduzido: ")
        arquivo = modulo.carrega_conteudos_json(file)
        pprint.pprint(arquivo)
        
        # Se obtém sucesso, quebra o loop
        break
    
    # Tratamento de exceções
    except TypeError:
        print("O parâmetro 'file' não era uma string.")
    except FileNotFoundError:
        print("O arquivo não pôde ser encontrado.")
    except IsADirectoryError:
        print("A string passada representa um diretório.")
    except PermissionError:
        print("Não há autorização para acessar o arquivo.")
    except OSError:
        print("Houve um problema do Sistema Operacional durante a leitura do arquivo.")
    except json.JSONDecodeError:
        print("Os conteúdos dentro do arquivo não estavam no formato de um `json`.")