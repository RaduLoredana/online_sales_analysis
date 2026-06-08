from product import Product
from product_manager import ProductManager
from cart import Cart

# 1. Cream managerul de produse
manager = ProductManager()


#Schimbam denumirile si cantitatile produselor initiale
p1 = Product("Laptop Gaming Pro", 5500, 5)
p2 = Product("Smartphone Ultra", 3500, 10)
p3 = Product("Casti Noise Cancelling", 450, 20)

# Setam noile cantitati
p1.quantity = 2
p2.quantity = 4
p3.quantity = 8

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

# REZOLVARE ETAPA 7: Liniile de afisare a inventarului magazinului au fost sterse!

# 2. Cream instanta pentru Cosul de Cumparaturi
cos_client = Cart()

# Adaugam cele 3 produse in cos
cos_client.add_to_cart(p1)
cos_client.add_to_cart(p2)
cos_client.add_to_cart(p3)

# 3. Afisam continutul cosului si valoarea totala (Cerinta finala)
print("\n")
cos_client.display_cart()
print(f"Valoarea totala de plata a cosului.")
