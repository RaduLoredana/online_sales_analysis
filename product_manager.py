from product import Product

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)  
        print(f"Produsul {product.name}, a fost adaugat in magazin")

    def display_all_products(self):
        if not self.products:
            print("Nu exista produse in magazin.")
            return
        print(f"Lista produselor disponibile.")
        for product in self.products:
            product.display_info()      

    def display_total_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"valoarea totala a stocului magazinului: {total_value}.")

    def remove_product_by_name(self, name):
        self.products = [product for product in self.products if product.name != name]

        