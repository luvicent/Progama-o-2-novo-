class ContaBancaria():
    def __init__(self, titular, saldo, numero_conta, tipo_conta):
        self.titular = titular
        self.saldo = saldo
        self.numero_conta = numero_conta
        self.tipo_conta = tipo_conta

    def depositar(self):
        valor = float(input("Digite o valor a ser depositado: "))
        self.saldo += valor
        print(f"O saldo da conta do(a) {self.titular} é de R$ {self.saldo}")
    
    def sacar(self):
        valor = float(input("Digite o valor a ser sacado: "))
        self.saldo -= valor
        print(f"O saldo da conta atual do(a) {self.titular} é de R$ {self.saldo} e ele acabou de sacar R$ {valor}")
    
    def transferir(self, saldo):
        valor = float(input("Qual que deseja tranferir?: "))
        self.saldo -= valor
        saldo += valor
        return saldo


    def verificar_saldo(self):
        print(f"O saldo da conta do(a) {self.titular} é de R$ {self.saldo}")

conta1 = ContaBancaria("lucas", 2000, 0.2, "corrente")
conta2 = ContaBancaria("manu", 2000, 0.2, "corrente")
print(f"saldo conta 1:{conta1.saldo}")
conta1.saldo = conta2.transferir(conta1.saldo)
conta1.verificar_saldo()
conta2.verificar_saldo()

