class Bomba_combustivel:

    def __init__(self, tipo_combustivel,valor_litro, quantidade_armazenada):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_armazenada = quantidade_armazenada



    def abastercerPorlitro(self):
        litro = int(input('Digite o número de litros que deseja abastecer: '))
        total_pagar = self.valor_litro * litro
        self.quantidade_armazenada = self.quantidade_armazenada - litro
        print(f'Voce abasteceu {litro} litros de {self.tipo_combustivel}. Total a pagar: R$ {total_pagar} reais')


    def abastercerPorvalor(self):
        valor = int(input('Digite um valor em dinheiro para abastecer: '))
        total_litros = 1 / self.valor_litro * valor
        self.quantidade_armazenada = self.quantidade_armazenada - total_litros
        print(f'Você colocou R$ {valor} reias, totalizando {total_litros:.2f} litros abastecidos')



    def mudar_valorLitro(self,novo):
        self.valor_litro = novo
        print(f'Valor alterado com sucesso: {self.valor_litro}')











bomba_gasolina = Bomba_combustivel('gasolinas',5.25,200)
bomba_alcool = Bomba_combustivel('alcool',3.85, 200)
bomba_Diesel = Bomba_combustivel('diesel', 6.35, 200)

print('=-'*20)
print(f'POSTO DO ARTHUR'.center(40))
print('=-'*20)

combustivel = int(input('''
Digite o número do combustível que deseja colocar: 


[1] Gasolina
[2] Alcool
[3] Diesel

'''))
print('=-'*20)
escolha = int(input('Digite 1 para abastecer por litro e 2 para abastecer por valor em dinheiro: '))
if combustivel == 1 and escolha == 1:
    bomba_gasolina.abastercerPorlitro()
elif combustivel == 1 and escolha == 2:
    bomba_gasolina.abastercerPorvalor()
if combustivel == 2 and escolha == 1:
    bomba_alcool.abastercerPorlitro()
elif combustivel == 2 and escolha == 2:
    bomba_alcool.abastercerPorvalor()
if combustivel == 3 and escolha == 1:
    bomba_Diesel.abastercerPorlitro()
elif combustivel == 3 and escolha == 2:
    bomba_Diesel.abastercerPorlitro()


print('=-'*20)
nivel = " "
while nivel not in 'SN':
    nivel = input('Deseja ver o nivel das bombas de combutivel? [S/N]').upper()[0]
    if nivel == 'S':
        print(f' O volume {bomba_gasolina.tipo_combustivel} é de {bomba_gasolina.quantidade_armazenada} litros')
        print(f' O volume {bomba_alcool.tipo_combustivel} é de {bomba_alcool.quantidade_armazenada} litros')
        print(f' O volume {bomba_Diesel.tipo_combustivel} é de {bomba_Diesel.quantidade_armazenada} litros')
    if bomba_alcool.quantidade_armazenada < 50:
        print(f'O nivel de armazenamento de Alcool está em:{bomba_alcool.quantidade_armazenada} litros.\n É necessário reabastecer o armazenamento')
    if bomba_gasolina.quantidade_armazenada < 50:
        print(f'O nivel de armazenamento de Gasolina está em:{bomba_gasolina.quantidade_armazenada} litros.\n É necessário reabastecer o armazenamento')
    if bomba_Diesel.quantidade_armazenada < 50:
        print(f'O nivel de armazenamento de Diesel está em:{bomba_Diesel.quantidade_armazenada} litros.\n É necessário reabastecer o armazenamento')
