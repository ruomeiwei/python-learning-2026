class ShoppingCart:
    def __init__(self, ):
        self.cart = {}
    
    def add_product(self, product_name, quantity, price):
        if product_name in self.cart:
            self.cart[product_name][quantity] += quantity
        else:
            self.cart[product_name] = {'quantity': quantity, 'price':price}
    
    def remove_product(self, product_name, quantity = None):
        if product_name in self.cart: 
            if quantity is None or quantity >= self.cart[product_name]['quantity']: 
                del self.cart[product_name]
            elif 0 <= quantity < self.cart[product_name]['quantity']:
                self.cart[product_name]['quantity'] -= quantity
        else:
            print('This product is not in the shopping cart.')
    
    def view_cart(self):
        if not self.cart:
            print('Shopping cart is empty.')
        else:
            for product_name, detail in self.cart.items():
                print(f'Product name is {product_name}, quantity is {detail['quantity']}, price is {detail['price']}')
    
    def calculate_total_price(self):
        total_price = 0
        for product_name, detail in self.cart.items():
            total_price += detail['quantity']*detail['price']
        
        return total_price


shoppingcart = ShoppingCart()

shoppingcart.add_product('Apple', 2, 3.5)
shoppingcart.add_product('Banana', 2, 1)

shoppingcart.view_cart()

print(shoppingcart.calculate_total_price())

shoppingcart.remove_product('Apple')

shoppingcart.view_cart()