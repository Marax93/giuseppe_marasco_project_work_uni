# Questa classe rappresenta un prodotto nella linea di produzione.
class Product:

    # Costruttore della classe Product.
    # Serve per inizializzare gli attributi del prodotto.
    def __init__(self, name, quantity, unit_time):
        self.name = name              # Nome del prodotto
        self.quantity = quantity      # Numero di unità da produrre per questo prodotto
        self.unit_time = unit_time    # Tempo necessario per produrre una singola unità (in minuti)

    # Calcola il tempo totale di produzione per questo prodotto.
    def total_time(self):
        return self.quantity * self.unit_time
    