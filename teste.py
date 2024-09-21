print(f"\033[32mBem vindo(a) a Calculadora Imperativa\033[0m")

def somar (n1, n2):
    return n1 + n2

def subtrair (n1, n2):
    return n1 - n2

def multiplicar (n1, n2):
    return n1 * n2

def dividir (n1, n2):
    if n1 == 0 or n2 == 0:
        print()
        print(f"\033[31mDivisão por 0 não permitida\033[0m")
    else:
       return n1 / n2
    
def calculadora():
    while True:
     try: 
           print()
           n1 = float(input("Primeiro número: "))
           n2 = float(input("Segundo número: "))
     except:
             print(ValueError)
     print(f"\033[31mOpções:\033[0m")
     print()
     print("1 - Somar")
     print("2 - Subtrair")
     print("3 - Multiplicar")
     print("4 - Divisão")
     print("5 - Sair")
     print()
     decisao = input("Opção escolhida: ")
     if decisao not in ['1', '2', '3', '4', '5']:
         print(f"\033[31mOPÇÃO INVÁLIDA\033[0m")
    

     if decisao == "5":
         print("Saindo da calculadora...")
         break
     
     if decisao in ['1', '2', '3', '4']:
         
         if decisao == '1':
             resultado = somar(n1, n2)
             print(f"{n1} + {n2} = \033[31m{resultado}\033[0m")
            
         if decisao == '2':
             resultado = subtrair(n1, n2)
             print(f"{n1} - {n2} = {resultado}")

         if decisao == '3':
             resultado = multiplicar(n1, n2)
             print(f"{n1} * {n2} = {resultado}")

         if decisao == '4':
             resultado = dividir(n1, n2)
             print(f"{n1} / {n2} = {resultado}")

calculadora()