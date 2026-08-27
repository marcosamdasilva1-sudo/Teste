#2 questao

print(f"valores pares entre{inicio e {fim}}")
for n in range(inicio,fim+1)


#3
senha = input("digite sua senha):")
has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in senha:
    if ch.isupper():
        has_upper = True
    if ch.islower():
        has

# erroos

errors = []
if len (senha) < 8:
    error.append




    #ativ
    # 4
notas = []
for i in range(4):
    while True:
 try:

    valor = float(input(f"Digite a nota {i+1}: "))

    if valor <0 or valor> 10:

    print("Informe uma nota entre 0 e 10.")
    continue
notas.append(valor)
break

except Exception:
print(" Entrada invalida".Digite um numero")


    media = sum(notas) / 4
    status = ""
    if media < 5:
        status = "Reprovado"

        elif5< media <7:
        status = "exame"

    else:
        status = "Aprovado"

        print(f"Media: {media.2f} - {status}")



        ###5


        #ativ5


        try:
        n = int(input("digite um numero:).strip())
    except Exception:
        print("entrada invalida.")
        for 


#ativ 6

valores = []
while True:
    try:
        valor = int(input("digite um valor (0 para encerrar): ").strip())
    except  Exception:
    print(" entrada invalida. digite um numero inteiro.")
    continue

    if valor == 0:
     break
valores.append(valor)

 if not valores:
     print(" nenhum valor foi informado.")

 n= len(valores)
 if n % 2 == 1:
    mid = n // 2
    print(f"valor central: {valores[mid]}")
else:
    a = valores[n//2 - 1]
    b = valores[n//2]
    print(f"lista com comprimento par. valores centrais:{a} e {b}")







    # ativ7
    nomes []

    for i in range(3):
    nome = input(f"digite o nome {i+1}: ").strip()
    nomes.append(nome)
    try:
        with open("usuraios.txt". "w", encoding="utf-8") as f:
            for n in nomes:
                f.write(n + "\n")
    except Exception:
         print("Erro ao gravar o arquivo.")

    print("nomes gravados em usuarios.txt")
        
        




    



