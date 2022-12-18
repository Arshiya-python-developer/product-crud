class PRODUCT:

    # Initialized
    def __init__(self,id,tittle,short_description,description,slug,permalink,is_available,sku,price,regular_price,sale_price,manage_stock,stock_quantity,is_visible,date_created_gmt,date_modified_gmt):
        self.id = id
        self.tittle = tittle
        self.short_description = short_description
        self.description = description
        self.slug = slug
        self.permalink = permalink
        self.is_available = is_available
        self.sku = sku
        self.price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.manage_stock = manage_stock
        self.stock_quantity = stock_quantity
        self.is_visible = is_visible
        self.date_created_gmt = date_created_gmt
        self.date_modified_gmt =  date_modified_gmt


    def add_product(self):
        self.tittle = input('please enter tittle of product: ')
        self.short_description = input('please write short description:')
        self.description = input('please write more description: ')
        self.slug = int('please enter how many slug:')
        self.permalink = input('write your permanent link:')



    def read_product(self):
        pass


    def update_product(self):
        pass


    def delete_product(self):
        pass

"""items = []
while True:
    #display = input('Press enter to continue.')
    print('1. Add items\n 1. View items\n3. Delete items \n4. Edit items\n5. Exit')
    choice = input('Enter the number of your choice : ')
    if choice == '1':
        Create()
"""



