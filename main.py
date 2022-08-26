import TelefonesBr
import Cpf_cnpj
from acesso_cep import BuscaEndereco

cep = "01001000"
objeto_cep = BuscaEndereco(cep)

# r = requests.get('https://viacep.com.br/ws/01001000/json/')
# print(r.text)

bairro, cidade, uf = objeto_cep.acessa_viacep()

# print(bairro)
# print(cidade)
# print(uf)

# cpf_teste = Cpf_cnpj.DocCnpj("18688481000135")
# print(cpf_teste)

telefone_teste = TelefonesBr.Telefones("5511985510041")
print(telefone_teste)
