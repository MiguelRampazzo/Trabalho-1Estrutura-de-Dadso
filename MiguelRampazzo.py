from FilaMiguelRampazzo import FilaEncadeada

class Cliente:
    def __init__(self, senha, tipo):
        self.senha = senha
        self.tipo = tipo

class SistemaAtendimento:
    def __init__(self, num_caixas):
        self.num_caixas = num_caixas
        self.caixas = [None] * num_caixas
        self.fila_geral = FilaEncadeada()  
        self.senha_contador = 1
        self.contador_preferenciais_atendidos = 0 

    def gerar_senha(self, tipo_cliente):
        """Gera a senha do cliente e insere na fila."""
        senha = self.senha_contador
        self.senha_contador += 1
        cliente = Cliente(senha, tipo_cliente)
        self.fila_geral.enfileirar(cliente)  
        return cliente

    def chamar_cliente(self, num_caixa: int) -> Cliente | None:
        """Chama um cliente para atendimento."""
        if num_caixa < 1 or num_caixa > self.num_caixas:
            raise ValueError("Número de caixa inválido.")
        
        if self.fila_geral.vazia():
            return None

        cliente_atendido = None
        no_atual = self.fila_geral.inicio
        anterior = None

        if self.contador_preferenciais_atendidos < 2:
            while no_atual:
                if no_atual.valor.tipo == "preferencial":
                    cliente_atendido = no_atual.valor
                    break
                anterior = no_atual
                no_atual = no_atual.proximo

        if cliente_atendido:
            if anterior is None: 
                self.fila_geral.inicio = no_atual.proximo
                if self.fila_geral.inicio is None:  
                    self.fila_geral.fim = None
            else:  
                anterior.proximo = no_atual.proximo
                if no_atual.proximo is None:  
                    self.fila_geral.fim = anterior
            self.contador_preferenciais_atendidos += 1
        else:
            cliente_atendido = self.fila_geral.desenfileirar()
            self.contador_preferenciais_atendidos = 0  

        if cliente_atendido:
            self.caixas[num_caixa - 1] = cliente_atendido

        return cliente_atendido

    def consultar_clientes_em_espera(self):
        """Exibe os clientes em espera."""
        print("\nClientes em espera:")

        if self.fila_geral.vazia():
            print("Nenhum cliente na fila.")
        else:
            atual = self.fila_geral.inicio
            while atual:
                cliente = atual.valor
                print(f"[Senha {cliente.senha} ({cliente.tipo})]", end=" -> ")
                atual = atual.proximo
            print("Fim")

    def consultar_estado_caixas(self):
        """Consulta o estado dos caixas."""
        print("Estado dos Caixas:")
        i = 1 
        for cliente in self.caixas:
            if cliente:
                print(f"Caixa {i}: Cliente {cliente.senha} ({cliente.tipo})")
            else:
                print(f"Caixa {i}: Vazio")
            i += 1



        
  

