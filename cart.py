from product import Product

class Cart:
    def __init__(self):
        # Inițializăm o listă goală pentru produsele din coș
        self.cart_items = []

    def add_to_cart(self, product):
        """Adaugă un produs în coșul de cumpărături."""
        self.cart_items.append(product)
        print(f"Produsul '{product.name}' a fost adăugat în coș.")

    def remove_from_cart(self, product_name):
        """Elimină un produs din coș după nume."""
        initial_count = len(self.cart_items)
        self.cart_items = [p for p in self.cart_items if p.name != product_name]
        
        if len(self.cart_items) < initial_count:
            print(f"Produsul '{product_name}' a fost eliminat din coș.")
        else:
            print(f"Produsul '{product_name}' nu se află în coș.")

    def calculate_total(self):
        """Calculează și returnează valoarea totală a coșului."""
        # Presupunem că produsul are proprietatea 'price'
        total = sum(product.price for product in self.cart_items)
        return total