import re

cpf = '034.447.885-89'

cpf_validade = re.sub(r'[^0-9]','', cpf)

print(cpf_validade)