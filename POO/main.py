from conta_bancaria_final import Conta

conta = input("Informe o número da conta: ");
titular = input("Informe o titular da conta: ");
saldo = float(input("Informe o saldo da conta: "));

#Criando uma instância da classe
minhaConta = Conta(conta, titular, saldo);

#Realizando operações na conta
depositar = float(input("Informe o valor para depósito: "));
sacar     = float(input("Informe o valor de saque: "));

minhaConta.depositar(depositar);
minhaConta.sacar(sacar);

#Exibindo as informações
minhaConta.exibir_informacoes();

