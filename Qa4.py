###   A  toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000. On orders of more than Rs. 100 for key-based toys, a discount of 5% is given, and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively. Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.=================================


product_code=int(input("Enter product code(1,2,3) : "))
# product_code=int(input("Enter product code(1:Battary_based_toys,2:Key_base_toys, 3:Electrical_based_toys) : "))
order_amount=float(input("Enter the amount : "))
discount_amount=0
if product_code==1:
    product_name = "Battery-based toys"
    if order_amount>1000:
        discount_amount=order_amount*0.10   
elif product_code==2:
    product_name = "Key-based toys"
    if order_amount>100:
        discount_amount=order_amount*0.05
elif product_code==3:
    product_name = "Electrical charging-based toys"
    if order_amount>500:
        discount_amount=order_amount*0.10
else:
    product_name = "Invalid product"
    print("Invallid product code !")
net_amount=order_amount-discount_amount 
print(f" The net amount paid {net_amount} for {product_name}")















