# -*- coding utf-8 -*- 

import csv

arquivo = open("contatos\contatos.csv")

#dicionário contatos
contatos = csv.DictReader(arquivo)


#txt = "Teste {nome}".format(nome = tabelaContatos['matricula'])

html_txt = """
<HTML>
<hr size="1" />
<table>
  <tr>
    <td style="font-family:tahoma,arial,verdana; font-size:11px; text-align:center" valign="top">
      <a href="{website}" target="_blank"><img src="https://www.montreal.com.br/wp-content/uploads/2017/04/montreal_logos.png" border="0" /></a>
    </td>
    <td style="font-family:tahoma,arial,verdana; font-size:12px; padding-left:10px">
      <strong>{nome}</strong>
      <br />
      <strong>Fone:</strong> {celularcorporativo} - {telcomercial}
      <br />
      <strong>Site:</strong> <a href="{website}" target="_blank">{website}</a>
      <br />
      <br /></td> </tr></table>
"""

for tabelaContatos in contatos:

   html_str = (html_txt.format(website = tabelaContatos['web-site'], nome = tabelaContatos['nome'], celularcorporativo = tabelaContatos['celular-corporativo'], telcomercial = tabelaContatos['tel-comercial']))
   print(html_str)
   
   Html_file= open("assinaturas\{matricula}.html".format(matricula = tabelaContatos['matricula']),"w")
   Html_file.write(html_str)
   Html_file.close()

   