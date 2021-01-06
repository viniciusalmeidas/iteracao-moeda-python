# Essa função exibe todas as possibilidades de combinação de pagamento em moedas de 100,50,25,10 e 5 centavos
# Batas informar o valor da COMPRA (em centavos) e o valor da MaiorMoeda(em centavos) disponível para pagamento

# Exemplo Questão
# Uma máquina automática que vende doces só aceita moedas de 1 centavo, 5 centavo e 10 centavos.
# Quantas possibilidades você tem para combinar essas moedas e MaiorMoedar um doce que custa 25 centavos?
#asdadasdadasdad
def combinacao_moedas(compra, MaiorMoeda):
    cont = 0;

    if MaiorMoeda == 100:
        for a in range(0, int(compra/100)+1):
            for b in range(0, int(compra/50)+1):
                for c in range(0, int(compra/25)+1):
                    for d in range(0, int(compra/10)+1):
                        for e in range(0, int(compra/5)+1):
                            formula = 100 * a + 50 * b + 25 * c + 10 * d + 5 * e
                            if formula == compra:
                                cont = cont + 1
                                print(f'id= {cont}, $100|{a}, $50|{b}, $25|{c}, $10|{d}, $5|{e}')
        print('---------------------------------------')
        print(f'Acima temos todas as {cont} possibilidades!')
        print('---------------------------------------fim')

    elif MaiorMoeda == 50:
        for b in range(0, int(compra/50)+1):
            for c in range(0, int(compra/25)+1):
                for d in range(0, int(compra/10)+1):
                    for e in range(0, int(compra/5)+1):
                        formula = 50 * b + 25 * c + 10 * d + 5 * e
                        if formula == compra:
                            cont = cont + 1
                            print(f'id= {cont}, $50|{b}, $25|{c}, $10|{d}, $5|{e}')
        print('---------------------------------------')
        print(f'Acima temos todas as {cont} possibilidades!')
        print('---------------------------------------fim')

    elif MaiorMoeda == 25:
        for c in range(0, int(compra/25)+1):
            for d in range(0, int(compra/10)+1):
                for e in range(0, int(compra/5)+1):
                    formula = 25 * c + 10 * d + 5 * e
                    if formula == compra:
                        cont = cont + 1
                        print(f'id= {cont}, $25|{c}, $10|{d}, $5|{e}')
        print('---------------------------------------')
        print(f'Acima temos todas as {cont} possibilidades!')
        print('---------------------------------------fim')

    elif MaiorMoeda == 10:
        for d in range(0, int(compra/10)+1):
            for e in range(0, int(compra/5)+1):
                formula = 10 * d + 5 * e
                if formula == compra:
                    cont = cont + 1
                    print(f'id= {cont}, $10|{d}, $5|{e}')
        print('---------------------------------------')
        print(f'Acima temos todas as {cont} possibilidades!')
        print('---------------------------------------fim')

    elif MaiorMoeda == 5:
        for e in range(0, int(compra/5)+1):
            formula = 5 * e
            if formula == compra:
                cont = cont + 1
                print(f'id= {cont}, $5|{e}')

        print(f'Acima temos todas as {cont} possibilidades!')


combinacao_moedas(100, 100)
