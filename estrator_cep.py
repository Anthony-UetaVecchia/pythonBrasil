# import do Regular Expressions ou RegEx
import re

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# 5 digitos + hifen (opcional) + 3 digitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)  # vai retornar o Match, que retornará o objeto Match ou None caso não encontre
if busca:
    cep = busca.group()
    print(cep)
