num = int(input('Digite um numero inteiro: ' ))
print('''(Escolha uma das opções para conversão:
    [B] Converter para binario
    [O] Converter para octal
    [H] Converter para Hexadecimal
    [T] Converter para todas bases''')
tipo = input('Sua opção: ')
    
num2 = num
num3 = num

binario = ""
while num!=0:
    r = num%2
    binario = str(r) + binario
    num = num//2

octal = ""
while num2 > 0:
    r = num2%8
    octal = str(r) + octal
    num2 = num2//8

    
he = ''
dic = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

hexa = ""
while num3!=0:
    c = num3%16
    he = dic[c] + he
    num3 = int(num3/16)

if tipo=='b' or tipo=='B':
    print ('o valor binario é: ', binario)

elif tipo=='o' or tipo=='O':
    print ('o valor octal é: ', octal)

elif tipo=='h' or tipo=='H':
    print ('o valor hexa é: ', he)

elif tipo=='t' or tipo=='T':
    print ('o valor binario é: ', binario)
    print ('o valor octal é: ', octal)
    print ('o valor hexa é: ', he)

else:
    print ('Tipo de coversão invalida!')

while:
    num = int(input('Digite um numero inteiro: ' ))

