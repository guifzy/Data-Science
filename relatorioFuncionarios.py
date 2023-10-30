import pandas as pd
import matplotlib.pyplot as plt


class Funcionario:
    def __init__(self, nome, cargo, salario, horas_trab):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.horasTrab = horas_trab
        self.imposto = ""

    def calcular_desconto(self):
        if self.salario <= 1500.00:
            self.imposto = "ISENTO"
            return 0
        elif 1500.00 < self.salario <= 3000.00:
            self.imposto = "15%"
            return self.salario * 0.15
        elif 3000.00 < self.salario <= 5000.00:
            self.imposto = "20%"
            return self.salario * 0.20
        else:
            self.imposto = "27%"
            return self.salario * 0.27

    def calcular_desconto_liquido(self):
        desconto = self.calcular_desconto()
        return self.salario - desconto

class FolhaPagamento:
    def __init__(self):
        self.funcionarios = []

    def inserir_func(self, funcionario):
        self.funcionarios.append(funcionario)

    def gravar_arqv(self):
        if not self.funcionarios:
            print("Nenhum funcionário registrado.")
        else:
            nome_arquivo = input("Digite o nome do arquivo (ex: folha_pag.txt): ")
            try:
                with open(nome_arquivo, 'w') as arquivo:
                    for funcionario in self.funcionarios:
                        gravar = f"{funcionario.nome},{funcionario.cargo},{funcionario.salario},{funcionario.horasTrab},{funcionario.imposto}\n"
                        arquivo.write(gravar)
                    print(f"\nDados gravados em {nome_arquivo} com sucesso!")
            except Exception as erro:
                print(f"Erro ao gravar os arquivos em {nome_arquivo}.\nErro: {erro}")

    def gerar_relatorio(self):
        nome_arquivo = input("Digite o nome do arquivo (ex: folha_pag.txt): ")
        try:
            with open(nome_arquivo, 'r') as arquivo:
                data = [line.strip().split(",") for line in arquivo]
                print("Dados dos Funcionários:")
                df = pd.DataFrame(data, columns=["Nome", "Cargo", "Salário Bruto", "HorasTrabalho", "Imposto"])
                print(df)
                print()
                df['Total IR'] = df['Salário Bruto'].apply(float).apply(lambda x: Funcionario('', '', x, 0).calcular_desconto())
                df['Total líquido'] = df['Salário Bruto'].apply(float).apply(lambda x: Funcionario('', '', x, 0).calcular_desconto_liquido())
                print(df[['Nome', 'Imposto', 'Salário Bruto', 'Total IR', 'Total líquido']])
                print()
                print("Valores totais:")
                total_bruto = df['Salário Bruto'].astype(float).sum()
                total_liquido = df['Total líquido'].astype(float).sum()
                total_desconto = df['Total IR'].astype(float).sum()
                print(f"Total Bruto: {total_bruto:.2f}")
                print(f"Total Líquido: {total_liquido:.2f}")
                print(f"Total Desconto: {total_desconto:.2f}")
                print()

                flag = input("Deseja imprimir um gráfico sobre o relatório S/N?")
                flag = flag.upper()
                if flag == 'S':
                    self.gerar_grafico(df)
        except Exception as erro:
            print(f"Erro ao ler os dados do arquivo {nome_arquivo}.\nErro: {erro}")

    def gerar_grafico(self, df):
        if df is None:
            print("Nenhum Data Frame gerado.")
        else:
            nomes = df['Nome']
            descontos = df['Total IR']
            funcoes = df['Cargo'].unique()
            salario_medio = [df[df['Cargo'] == cargo]['Salário Bruto'].astype(float).mean() for cargo in funcoes]

            plt.figure(figsize=(10, 6))
            plt.barh(nomes, descontos, color='skyblue')
            plt.xlabel('Imposto Pago')
            plt.ylabel('Funcionários')
            plt.title('Imposto Pago por Funcionário')

            plt.show()

            plt.figure(figsize=(10, 6))
            plt.barh(funcoes, salario_medio, color='lightcoral')
            plt.xlabel('Salário Médio')
            plt.ylabel('Cargo')
            plt.title('Salário Médio por Cargo')

            plt.show()

def menu():
    folha_pagamento = FolhaPagamento()
    while True:
        print("****** MENU DE OPÇÕES ******")
        print("|------------------------------------|")
        print("|   1- Registrar funcionário         |")
        print("|   2- Gravar arquivo                |")
        print("|   3- Imprimir dados de um arquivo  |")
        print("|   4- Sair                          |")
        print("|------------------------------------|")
        opcao = input("Insira o número da operação desejada: ")
        print()
        if opcao == '1':
            nome = input("Nome do funcionário: ")
            cargo = input("Cargo: ")
            salario = float(input("Salário: "))
            horas_trabalhadas = float(input("Horas trabalhadas: "))
            funcionario = Funcionario(nome, cargo, salario, horas_trabalhadas)
            funcionario.calcular_desconto()
            folha_pagamento.inserir_func(funcionario)

        elif opcao == '2':
            folha_pagamento.gravar_arqv()
        elif opcao == '3':
            folha_pagamento.gerar_relatorio()
        elif opcao == '4':
            print("\nPrograma Encerrado!")
            break
        else:
            print("\nOpção inválida")


if __name__ == "__main__":
    menu()
