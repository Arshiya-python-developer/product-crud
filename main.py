from product import PRODUCT


Item = PRODUCT(1,'laptop','grea laptop','new model',2,'hhhhh',True,'5',55,56,75,5,5,True,'2022/12/01','2022/12/5')


print(Item.add_product())
print(Item.read_product())
print(Item.delete_product())
print(Item.update_product())
x = isinstance(Item,PRODUCT)
print(x)
