# -*- coding utf-8 -*- 

import csv

arquivo = open("contatos\contatos.csv")

#dicionário contatos
contatos = csv.DictReader(arquivo)

#for tabelaContatos in contatos:
 #   print(tabelaContatos)
s = len(contatos)
print(s)