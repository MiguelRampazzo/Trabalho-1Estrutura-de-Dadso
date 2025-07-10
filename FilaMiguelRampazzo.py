class No:
    """No de uma fila encadeada."""
    def __init__(self, valor):
        self.valor = valor 
        self.proximo: No | None = None 

class FilaEncadeada:
    """Fila implementada com encadeamento de nós."""
    def __init__(self) -> None:
        self.inicio: No | None = None 
        self.fim: No | None = None

    def vazia(self) -> bool:
        """Verifica se a fila está vazia."""
        return self.inicio is None

    def enfileirar(self, valor) -> None:
        """Adiciona um elemento no final da fila."""
        novo_no = No(valor)
        if self.vazia():
            self.inicio = self.fim = novo_no
        else:
            if self.fim is not None:
                self.fim.proximo = novo_no
                self.fim = novo_no

    def desenfileirar(self) -> object | None:
        """Remove e retorna o primeiro elemento da fila."""
        if self.vazia():
            return None
        valor = self.inicio.valor 
        self.inicio = self.inicio.proximo  
        if self.inicio is None: 
            self.fim = None
        return valor
