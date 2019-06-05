# Type code for classes here
class ItemToPurchase:
    
    total_cost = 0
    def __init__(self,item_name = 'none', item_price = 0, item_quantity = 0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        ItemToPurchase.total_cost += item_price * item_quantity
        
    def print_item_cost(self):
        print('%s %d @ $%d = $%d' % (self.item_name, self.item_quantity, self.item_price, (self.item_price * self.item_quantity)))

if __name__ == "__main__":
    print('Item 1')
    name = input('Enter the item name:\n')
    price = float(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))
    item_1 = ItemToPurchase(name, price, quantity)
    print('\nItem 2')
    name = input('Enter the item name:\n')
    price = float(input('Enter the item price:\n'))
    quantity = int(input('Enter the item quantity:\n'))
    item_2 = ItemToPurchase(name, price, quantity)
    
    print('\nTOTAL COST')
    item_1.print_item_cost()
    item_2.print_item_cost()
    print('\nTotal: $%d' % item_1.total_cost)
    
