# Aula python, 27/03/2023
# Aula de rastreamento de programa 

      #sequencias e tempos( slide 133)

divida = 0

compra = 100
divida = divida + compra

compra = 200
divida = divida + compra

compra = 300
divida = divida + compra

compra = 0
divida = divida + compra

print(divida)

# #Variaveis e Entrada de dados
# #fazer exercicios slides 153/154/155 


x = input("Digite um numero ");
print(x);

#-------------------------------

y = input("Digite um nome");

print("voce digitou %s"%y);

print("Olá, %s!"%y);

#-------------------------------

anos = int(input("Anos de serviço"));
valor_por_ano = float(input("Valor por ano:"));

bonus = anos*valor_por_ano

print("bonus de R$ %5.2f" %bonus);

# # Condições  (slide160)

a = int(input("valor 1: "));
b = int(input("valor 2: "));

if a>b:
    print("o valor 1 é maior");

if a<b:
    print("o valor 2 é maior");

# # Exercicios slide 167

idade = int(input("digite a idade do seu corra "));

if idade <= 3:
    print("seu carro é novo");
if idade > 3:
    print("seu carro é velho");10

# # Exercicio slide 171
# utilizando de equacoes e if dentro do sistema condiçao

salario = float(input("Digite o salario para calculo de imposto"));
base = salario
imposto = 0

if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35);
    base = 3000

if base >1000:
    imposto = imposto + ((base - 1000) * 0.20);
    
print("Salário: R$%6.2f Imposto a pagar: R$%6.2f" % (salario, imposto))
    
    #exercicio slide 177
# como utilizar condiçao else ex:Else

idade_carro = int(input("qual a idade do seu carro? "));

if idade_carro <= 3:
    print("seu carro é novo");
else:
    print("seu carro é velho");
    
#-----------------------------------------------------------------------

    # Exercicio slide 180
    #utilizando elif(else + if para facilitar o cod)
    
categoria = int(input("categoria do porduto"));

if categoria == 1:
    preço = 10
elif categoria == 2:
    preço = 18
elif categoria == 3:
    preço = 23
elif categoria == 4:
    preço = 26
elif categoria ==5:
    preço = 31
else:
    print("categoria invalida, digite um valor entre 1 e 5!");
    preço = 0
    
print("o preço do produto é: R$%6.2f" % preço);

    # exercicio slide 188
 #---------------------------------------------------------------------   
    #REPETIÇOES (sistemas)
x = 0
while x <= 50:
    print(x)
    x = x + 10

       # Exercicio slide 198
       
        #programa para mostrar na tela apenas os numeros pares
        #( numeros que quando divididos por dois apresentam resto zero)
 #---------------------------------------------------------------------
       
fim = int(input("ultimo numero a ser considerado: "));
x = 0
while x <= fim:
    if x %2 == 0:
        print(x)
    x = x + 1

    # maneira mais simples de realizar o porgrama acima:
       
fim = int(input("ultimo numero a ser considerado: "));
x = 0
while x <= fim:
        print(x)
        x = x + 2
#---------------------------------------------------
       # Exercicios slide 205
n = int(input("tabuada de: "));
x = 1
while x<= 10:
    print(n*x)
    x = x + 1
    
#----------------------------------------------------------
  
pontos = 0
questão = 1
while questão <= 3:
    resposta = input("Resposta da questão %d: " % questão)
    if questão == 1 and resposta == "b":
        pontos = pontos + 1
   
    if questão == 2 and resposta == "a":
        pontos = pontos + 1
    
    if questão == 3 and resposta == "d":
        pontos = pontos + 1
    
    questão +=1
print("O aluno fez %d ponto(s)" % pontos);

#--------------------------------------------
#ACUMULADORES

n = 1 
soma = 0 

while n<=10:
    x = int(input("Digite o %d número:"%n));
    soma = soma + x
    n = n + 1
print("soma: %d"%soma);

#--------------------------------------------------------

x = 1 
soma = 0 
while x <=5:
    n = int(input("%d digite o numero:" %x));
    soma  = soma + n
    x = x + 1
print("media: %5.2f"%(soma/5));

#Exercicios slides 216/219

    






















