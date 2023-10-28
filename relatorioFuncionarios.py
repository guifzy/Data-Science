import pandas as pd
import matplotlib.pyplot as plt


class Funcionario:
    def __init__(self, nome, cargo, salario, horas_trab):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.horasTrab = horas_trab

    def calcular_desconto(self):
        if self.salario <= 1500:
            return 0
        elif 1500 < self.salario <= 3000:
            return self.salario * 0.15
        elif 3000 < self.salario <= 5000:
            return self.salario * 0.20
        else:
            return self.salario * 0.27

    def calcular_desconto_liquido(self):
        desconto = self.calcular_desconto()
        return self.salario - desconto


class FolhaPagamento:
    def __init__(self):
        self.funcionarios = []
        self.total_desconto = 0
        self.total_bruto = 0
        self.total_liquido = 0

    def inserir_func(self, funcionario):
        self.funcionarios.append(funcionario)

    def gravar_arqv(self):
        if not self.funcionarios:
            print("Nenhum funcionário registrado.")
        else:
            nome_arquivo = input("Digite o nome do arquivo (ex: folha_pag.txt): ")
            try:
                with open(nome_arquivo, 'w') as arquivo:
                    titulo = "Nome,Cargo,Salário,HorasTrabalho\n"
                    arquivo.write(titulo)
                    for funcionario in self.funcionarios:
                        gravar = f"{funcionario.nome},{funcionario.cargo},{funcionario.salario},{funcionario.horasTrab}\n"
                        arquivo.write(gravar)
                    print(f"\nDados gravados em {nome_arquivo} com sucesso!")
            except Exception as erro:
                print(f"Erro ao gravar os arquivos em {nome_arquivo}.\nErro: {erro}")

    def calculo_total(self):
        self.total_desconto = 0
        self.total_bruto = 0
        self.total_liquido = 0

        for funcionario in self.funcionarios:
            desconto_ir = funcionario.calcular_desconto()
            salario_liquido = funcionario.calcular_desconto_liquido()

            self.total_bruto += funcionario.salario
            self.total_liquido += salario_liquido
            self.total_desconto += desconto_ir

    def gerar_relatorio(self):
        nome = input("Digite o nome do arquivo:\n(ex: folha_pag.txt): ")
        try:
            with open(nome, 'r') as arquivo:
                data = [line.strip().split(",") for line in arquivo]
                df = pd.DataFrame(data, columns=["Nome", "Cargo", "Salário", "HorasTrabalho"])
                print(df)
        except Exception as erro:
            print(f"Erro em gravar os arquivos em {nome}.\nErro: {erro}")


def menu():
    folha_pagamento = FolhaPagamento()
    while True:
        print("****** MENU DE OPÇÕES ******")
        print("|------------------------------|")
        print("|   1- Registrar funcionário   |")
        print("|   2- Gravar arquivo          |")
        print("|   3- Imprimir dados          |")
        print("|   4- Imrpimir gráfico        |")
        print("|   5- Sair                    |")
        print("|------------------------------|")
        opcao = input("Insira o número da operação desejada: ")
        print()
        if opcao == '1':
            nome = input("Nome do funcionário: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário: "))
            horas_trabalhadas = float(input("Horas trabalhadas: "))
            funcionario = Funcionario(nome, cargo, salario, horas_trabalhadas)
            folha_pagamento.inserir_func(funcionario)

        elif opcao == '2':
            folha_pagamento.gravar_arqv()
        elif opcao == '3':
            folha_pagamento.gerar_relatorio()
        #elif opcao == '4':

        elif opcao == '5':
            print("\nPrograma Encerrado!")
            break
        else:
            print("\nOpção inválida")


if __name__ == "__main__":
    menu()