from inventory_manager import InventoryManager
from seller import Seller
from item import Item
from buyer import Buyer
from payment_type_gpay import Gpay

inventory = InventoryManager()


def perform_seller_task(seller):
    seller.add_or_update_item(1, 5, inventory)

def perform_buyer_task(buyer):
    buyer.buy(1, 1, inventory)


def create_few_sellers_and_buyers():
    seller_1 = Seller('s1', 1)
    buyer_1 = Buyer('b1', 1, Gpay())
    return seller_1, buyer_1

def main():
    seller_1, buyer_1 = create_few_sellers_and_buyers()
    print('provide input: 1 for sell, 2 for buy, 0 for exit')
    while(True):
        inp = int(input())
        if(inp == 1):
            perform_seller_task(seller_1)
        if(inp == 2):
            perform_buyer_task(buyer_1)
        if(inp == 0):
            break



if __name__ == '__main__':
    main()