from MiguelRampazzo import SistemaAtendimento
import os

def main():
    sistema = SistemaAtendimento(4)
    while True :
        print("Menu de Opções:")
        print("1 - Gerar senha")
        print("2 - Chamar cliente")
        print("3 - Consultar clientes em espera")
        print("4 - Consultar estado dos caixas")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            tipo_cliente = input("Digite o tipo de cliente (preferencial/comum): ")
            if tipo_cliente in ("preferencial", "comum"):
                cliente = sistema.gerar_senha(tipo_cliente)
                print(f"Senha gerada: {cliente.senha} ({cliente.tipo})")
            else:
                print("Tipo de cliente inválido.")
        
        elif opcao == "2":
                num_caixa = int(input("Digite o número do caixa: "))
                cliente = sistema.chamar_cliente(num_caixa)
                if cliente:
                    print(f"Cliente {cliente.senha} ({cliente.tipo}) está sendo atendido no caixa {num_caixa}.")
                else:
                    print("Nenhum cliente na fila para atendimento.")
        
        elif opcao == "3":
            sistema.consultar_clientes_em_espera()
        
        elif opcao == "4":
            sistema.consultar_estado_caixas()
        
        elif opcao == "5":
            os.system("cls")


if __name__ == "__main__":
    main()


