def main():
    #Leitura do dinheiro
    dinheiro = int(input())
    print(dinheiro)
    #conta notas 100
    notas = int(dinheiro/100.0)
    print("%i nota(s) de R$ 100,00" %notas)
    #conta notas 50
    dinheiro -= notas*100
    notas = int(dinheiro/50)
    print("%i nota(s) de R$ 50,00" %notas)
    #conta notas 20
    dinheiro -= notas*50
    notas = int(dinheiro/20)
    print("%i nota(s) de R$ 20,00" %notas)
    #conta notas de 10
    dinheiro -= notas*20
    notas = int(dinheiro/10)
    print("%i nota(s) de R$ 10,00" %notas)
    #conta notas de 5
    dinheiro -= notas*10
    notas = int(dinheiro/5)
    print("%i nota(s) de R$ 5,00" %notas)
    #conta notas de 2
    dinheiro -= notas*5
    notas = int(dinheiro/2)
    print("%i nota(s) de R$ 2,00" %notas)
    #notas de 1 são o restante
    dinheiro -= notas*2
    print("%i nota(s) de R$ 1,00" %dinheiro)
main()