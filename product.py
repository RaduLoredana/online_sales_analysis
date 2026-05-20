class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
# Afisarea infornatiilor despre produs.
     print(f"Produs: {self.name:<15}, Pret: {self.price:>7.2f}, Cantitate: {self.quantity:>4}")     

    def update_quantity(self, new_quantity: int):
#Actualizarea cantitatii produsului.
     self.quantity =new_quantity       
        