#Solução orientada a objetos para um banco com a entidade "Conta"

class Conta:
  #Criar um método construtor
  def __init__(self, numero, titular, saldo = 0):
    self.numero  = numero;
    self.titular = titular;
    self.saldo   = saldo;

  def depositar(self, valor):
    self.saldo += valor;
  
  def sacar(self, valor):
    if valor <= self.saldo:
      self.saldo -= valor;
    else:
      print("Saldo insuficiente!");
  
  def exibir_informacoes(self):
    print(f"Conta: {self.numero}");
    print(f"Titular: {self.titular}");
    print(f"Saldo antes da conversão para real: {self.saldo:,.2f}")
    valorEmReal = f"R$ {self.saldo:_.2f}"
    valorEmReal = valorEmReal.replace('.', ',').replace('_', '.');
    print(f"Saldo: {valorEmReal}");
    
#Criação de uma conta e realização de operações

conta = Conta(123, "Diego");
conta.depositar(1000000)
conta.exibir_informacoes();
