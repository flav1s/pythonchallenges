class Geladeira:
    def __init__(self, modelo, cor, congeladorInterno, qtItems):
        self.modelo = modelo
        self.cor = cor
        self.congeladorInterno = congeladorInterno
        self.qtItems = qtItems

        self.pegarItem()

    def pegarItem(self):
        if self.qtItems > 0:
            print("Voce pegou um item")
        else:
            print("Geladeira vazia!")
            self.qtItems = input("Entre a quantida de items: ")
            print("Voce adicionou", self.qtItems, "Items")
        
        self.mudarCor()

    def mudarCor(self):
        self.cor = input("Qual cor voce deseja? ")
        print("Nova cor eh", self.cor)


g1 = Geladeira("Mondial", "Preta", False, 0)
