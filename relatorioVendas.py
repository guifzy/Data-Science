import pandas as pd
import matplotlib.pyplot as plt


class Armazem:
    def __init__(self):
        self.data = pd.DataFrame({'Mercadoria': range(1, 101)})
        self.data['Preço'] = 0.0
        self.data['Quantidade Vendida'] = 0
        self.faturamento = 0
        self.i = 0

    def menu(self):
        while True:
            print("****** MENU DE OPÇÕES ******")
            print("|-----------------------------|")
            print("|   1- Registrar venda        |")
            print("|   2- Imrpimir faturamento   |")
            print("|   3- Imprimir Porcentuais   |")
            print("|   4- Gravar arquivo         |")
            print("|   5- Imrpimir gráfico       |")
            print("|   6- Sair                   |")
            print("|-----------------------------|")
            opcao = input("Insira o número da operação desejada: ")
            print()

            if opcao == '1':
                self.registrar_vendas()
            elif opcao == '2':
                self.imprimir_faturamento()
            elif opcao == '3':
                self.imprimir_percentuais()
            elif opcao == '4':
                self.gravar_dados_em_arquivo()
            elif opcao == '5':
                self.grafico()
            elif opcao == '6':
                print("Programa Encerrado.")
                break
            else:
                print("Opção inválida!")

    def registrar_vendas(self):
        flag = input(f"Deseja limpar as mercadorias registradas S/N?")
        flag = flag.upper()
        if flag == 'S':
            for i in range(self.i):
                self.data.at[i, 'Quantidade Vendida'] = 0
                self.data.at[i, 'Preço'] = 0.0
            self.i = 0
        print(f"Registrando vendas a partir da mercadoria {self.i + 1}")

        tam = int(input("Digite a quantidade de mercadorias que deseja registrar: "))
        print()
        for i in range(tam):
            preco = float(input(f"Digite o preço da mercadoria {self.i + 1}: R$"))
            quant = int(input("Digite a quantidade vendida: "))
            if quant < 0 or preco < 0.0:
                print("Quantidade ou preço não podem ser negativos!")
            else:
                self.data.at[self.i, 'Preço'] = preco
                self.data.at[self.i, 'Quantidade Vendida'] = quant
                self.i = self.i + 1
        print()
        print("Vendas registradas com sucesso!\n")

    def imprimir_faturamento(self):
        self.faturamento = sum(self.data['Quantidade Vendida'] * self.data['Preço'])
        print("Faturamento mensal: ")
        print(self.data.head(100))
        print(f"Total faturado R${self.faturamento:.2f}\n")

    def imprimir_percentuais(self):
        if self.faturamento == 0:
            print("Nenhuma venda ou faturamento registrado.")
            print("Por favor, conferir se foi realizada a impressão do fatoramento!")
        else:
            pencentuais = (self.data['Quantidade Vendida'] * self.data['Preço']) / self.faturamento
            self.data['Percentual'] = pencentuais * 100

            print("Percentuais de venda por mercadoria: ")
            print(self.data[['Mercadoria', 'Percentual']])

    def gravar_dados_em_arquivo(self):
        if self.faturamento == 0:
            print("Nenhuma venda ou faturamento registrado.")
            print("Por favor, conferir se foi realizada a impressão do fatoramento!")
        else:
            nome = input("Digite o nome do arquivo:\n(ex: dados_vendas.txt): ")
            try:
                with open(nome, 'w') as arquivo:
                    titulo = "Mercadoria/Preço/Total de Vendidas\n"
                    arquivo.write(titulo)
                    for i in range(len(self.data)):
                        linha = f"{self.data.at[i, 'Mercadoria'], self.data.at[i, 'Preço'], self.data.at[i, 'Quantidade Vendida'],}\n"
                        arquivo.write(linha)
                    faturamento = self.faturamento
                    arquivo.write(f"\nFaturamento: R${faturamento}")
                    print(f"\nDados gravados em {nome} com sucesso! ")
                    arquivo.close()
            except Exception as erro:
                print(f"Erro em gravar os arquivos em {nome}.\nErro: {erro}")

    def grafico(self):
        if self.faturamento == 0:
            print("Nenhuma venda ou faturamento registrado.")
        else:
            top5 = self.data.nlargest(5, 'Quantidade Vendida')
            plt.figure(figsize=(10, 6))
            plt.bar(top5['Mercadoria'], top5['Quantidade Vendida'])
            plt.title('Cinco Mercadorias Mais Vendidas')
            plt.xlabel('Mercadoria')
            plt.ylabel('Quantidade Vendida')
            plt.show()


if __name__ == "__main__":
    armazem = Armazem()
    armazem.menu()
