
#inicial


"""
class invoice:
    def __init__(self, numero, descricao, quantidade, preco):
        self.numero = numero
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco
#com get e set
"""
class Invoice:
    def __init__(self, numero, descricao, quantidade, preco):
        self.numero = numero
        self.descricao = descricao
        self.quantidade = quantidade
        self.preco = preco
        self.set_numero(numero)
        self.set_descricao(descricao)
        self.set_quantidade(quantidade)
        self.set_preco(preco)

    def set_preco(self, num):
       if(not(isinstance(num, float) and (num > 0))):
            num = 0.0
       self.preco = num
    def set_numero(self, num):
        if(not(isinstance(num,int) and (num>0))):
            raise ValueError("o número é inválido: {}".format(num))
            num = 0
        self.numero = num
    def set_descricao(self, dec):
        if(not(isinstance(dec,str))):
            raise ValueError("o atributo é inválido: {}".format(dec))
        self.descricao = dec
    def set_quantidade(self, num):
        if(not(isinstance(num, int) and (num > 0))):
            raise ValueError("O atributo é inválido ")
        self.quantidade = num
    
    def get_descricao(self):
        return self.descricao

    def get_preco(self):
        return self.preco
    
    def get_numero(self):
        return self.numero
        
    
    def get_quantidade(self):
        return self.quantidade
    #aqui calculamos o valor da fatura
    def getInvoiceAmout(self):
        return float(self.preco * self.quantidade)


#agora salvando em um arquivo txt 
def Nota_escrita(arquivox,codigo, descricao, preco, quantidade, quantidade_total):
   arquivo = open(arquivox, 'w')
   cabecalho = 'Código   Descricao   Preco   Quantidade   Preco Total \n'
   arquivo.write(cabecalho)
   arquivo.write(str(codigo))
   arquivo.write('   ')
   arquivo.write(str(descricao))
   arquivo.write('   ')
   arquivo.write(str(preco))
   arquivo.write('   ')
   arquivo.write(str(quantidade))
   arquivo.write('   ')
   arquivo.write(str(quantidade_total) + "/n")
   arquivo.close()

#produto = Invoice(775,"Maiones Heelmans", 1, 22.45)
produto = Invoice(1,"null", 1, 1)

lista = []
n = 0
print("bem vindo ao supermercado \n")
print("O que deseja? \n")
"""
a = int(input("informe o código"))

produto.set_numero(a)
#print(produto.get_numero())
a = int(input("informe o código"))
produto.set_numero(a)
"""




"""
1ª tentativa
while n == 0:
    print("Passe o produto")
    a = int(input ("informe o código"))
    produto.set_numero(a)
    b = str(input("Qual a descrição deste produto ?"))
    produto.set_descricao(b)
    c = int(input("qual a quantidade ?"))
    produto.set_quantidade(c)
    d = float(input("qual o preço"))
    produto.set_preco(d)
    lista.append(produto)
   
    print("se desejar continuar digite 0 /n")
    print("se não quiser continuar digite 1  /n")
    
    input = n
"""
#2ª tentativa
m = 0 

while n < 1000 :
    print("Passe o produto \n")
    a = int(input ("informe o código \n"))
    produto.set_numero(a)
    b = str(input("Qual a descrição deste produto ? \n"))
    produto.set_descricao(b)
    c = int(input("qual a quantidade ? \n"))
    produto.set_quantidade(c)
    d = float(input("qual o preço \n"))
    produto.set_preco(d)
    lista.append(produto)
    Nota_escrita('notafiscal.txt' ,produto.get_numero(), produto.get_descricao(), produto.get_quantidade(), produto.get_preco(), produto.getInvoiceAmout())
   
    print("se desejar continuar digite 0 /n")
    print("se não quiser continuar digite 1  /n")
    
    m = int(input())
    if m == 1:
        break
    n = n + 1

#print(lista[0].get_preco())






    
    



#agora vai passar na maquininha bip bip 





