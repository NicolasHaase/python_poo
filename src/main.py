from frota import *

def operar_carro(carro: Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')

    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)

if __name__ == "__main__":
    print('Cadastre o primeiro carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    tanque = float(input('Digite a quantidade de litros no tanque: '))
    consumo = float(input('Digite o consumo médio: '))


    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0, motor = False, tanque = tanque, consumo_medio = consumo)

    print('Cadastre o segundo carro')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    tanque = float(input('Digite a quantidade de litros no tanque: '))
    consumo = float(input('Digite o consumo médio: '))

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, motor = False, tanque = tanque, consumo_medio = consumo)

    '''
    Controlando o carro até ele atingir 10000 Km
    '''
    while carro1.odometro < 600 and carro2.odometro < 600 and carro1.tanque > 0 and carro2.tanque > 0:
        try:
            op = 0
            while op not in (1, 2):
                op = int(input("Qual carro [1,2]?"))

            if op == 1:
                operar_carro(carro1)
            else:
                operar_carro(carro2)

            print('Infos atuais do carro')
            print(carro1)
        except Exception as e:
            print("Erro!")
            print(e)

    if carro1.motor_on:
        carro1.desligar()
    if carro2.motor_on:
        carro2.desligar()

    print(carro1)
    print(carro2)

    if carro1.odometro >= 600:
        print("O carro 1 ganhou")
    elif carro2.odometro >= 600:
        print("O carro 2 ganhou")
    elif carro1.tanque == 0:
        print("Acabou a gasosa do carro 1")
    else:
        print("Acabou a gasosa do carro 2")

