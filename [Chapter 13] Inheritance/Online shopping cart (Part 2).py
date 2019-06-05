# Type code for classes here
class ItemToPurchase:
    
    total_cost = 0
    
    def __init__(self,item_name = 'none', item_price = 0, item_quantity = 0, item_description = 'none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
        ItemToPurchase.total_cost += item_price * item_quantity
    
    def print_item_cost(self):
        print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price, (self.item_price * self.item_quantity)))
    
    def print_item_description(self):
        print('%s: %s'%(self.item_name,self.item_description,))
        
class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2016', cart_items = []):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items
    
    def add_item(self,item):
        self.cart_items.append(item)
    
    def remove_item(self):
        print('\nREMOVE ITEM FROM CART')
        string = input('Enter name of item to remove:\n')
        i = 0
        item_removed = False
        for item in self.cart_items:
            if(item.item_name == string):
                del self.cart_items[i]
                item_removed = True
            i += 1
        if not item_removed:
            print('Item not found in cart. Nothing removed.')
    
    def modify_item(self):
        print('\nCHANGE ITEM QUANTITY')
        name = input('Enter the item name:\n')
        quantity = int(input('Enter the new quantity:\n'))
        item_removed = False
        for item in self.cart_items:
            if(item.item_name == name):
                item.item_quantity = quantity
                item_removed = True
        if not item_removed:
            print('Item not found in cart. Nothing modified.')        
                
    def get_num_items_in_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.item_quantity
        return total
        
    def get_cost_of_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.item_quantity * item.item_price
        return total
        
    def print_total():
        total_cost = get_cost_of_cart()
        if (total_cost == 0):
            print('SHOPPING CART IS EMPTY')
        else:
            output_cart()
            
    def print_descriptions(self):
        print('\nOUTPUT ITEMS\' DESCRIPTIONS')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('\nItem Descriptions')
        for item in self.cart_items:
            print('{}: {}'.format(item.item_name, item.item_description))
            
    def output_cart(self):
        print('OUTPUT SHOPPING CART')
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        total_items = 0
        for item in self.cart_items:
            total_items += item.item_quantity
        print('Number of Items:', total_items)
        print()
        tc = 0
        for item in self.cart_items:
            print('%s %d @ $%d = $%d' % (item.item_name, item.item_quantity, item.item_price, (item.item_quantity * item.item_price)), end='\n')
            tc += (item.item_quantity * item.item_price)
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        print('\nTotal: $%d' % (tc))
    
def print_menu(ShoppingCart):
    customer_Cart = newCart
    menu = ('\nMENU\n'
            'a - Add item to cart\n'
            'r - Remove item from cart\n'
            'c - Change item quantity\n'
            'i - Output items\' descriptions\n'
            'o - Output shopping cart\n'
            'q - Quit\n')
    command = ''
    while(command != 'q'):
        string=''
        print(menu)
        command = input('Choose an option:\n')
        while(command != 'a' and command != 'o' and command != 'i' and command != 'r' and command != 'c' and command != 'q'):
            command = input('Choose an option:\n')
        if(command == 'a'):
            print('\nADD ITEM TO CART')
            item_name = input('Enter the item name:')
            item_description = input('\nEnter the item description:')
            item_price = float(input('\nEnter the item price:'))
            item_quantity = int(input('\nEnter the item quantity:\n'))
            customer_Cart.add_item(ItemToPurchase(item_name, item_price, item_quantity, item_description))
        if(command == 'o'):
            customer_Cart.output_cart()
        if(command == 'i'):
            customer_Cart.print_descriptions()
        if(command == 'r'):
            customer_Cart.remove_item()
        if(command == 'c'):
            customer_Cart.modify_item()
    
if __name__ == "__main__":
    # Type main section of code here
    customer_name = str(input('Enter customer\'s name:\n'))
    current_date = str(input('Enter today\'s date:\n\n'))
    print('Customer name:', customer_name)
    print('Today\'s date:', current_date)
    newCart = ShoppingCart(customer_name, current_date)
    print_menu(newCart)
                
