import openpyxl

workbook = openpyxl.load_workbook('Clientes.xlsx')
pagina_clientes = workbook['Página1']

for linha in pagina_clientes.iter_rows(min_row=2):
    Nome = linha[0].value
    E_mail = linha[1].value
    Telefone = linha[2].value

    print(Nome)
    print(E_mail)
    print(Telefone)

#a faiela é uma calculadora
