class PRODUCT:

    _product = []
    # Initialized
    def __init__(self,id:int,tittle:str,short_description:str,description:str,slug:int,permalink:str,is_available:bool,sku:str,price:float,regular_price:float,sale_price:float,manage_stock:int,stock_quantity:int,is_visible:bool,date_created_gmt,date_modified_gmt):

        assert price >= 0
        assert regular_price >= 0
        assert sale_price >= 0
        assert stock_quantity >= 0

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




    def __repr__(self):
        return f'Product({self.id},{self.tittle},{self.short_description},{self.description},{self.slug}' \
               f'{self.sku},{self.permalink},{self.is_available},{self.price},{self.regular_price},{self.sale_price}' \
               f'{self.manage_stock},{self.stock_quantity},{self.is_visible},{self.date_created_gmt},{self.date_modified_gmt}) '



     def add_product(self):
       self._product.append(self)
       return self.__repr__()

        #return self._product.append([self.id,self.tittle,self.short_description,self.description,self.slug,
         #                            self.permalink,self.is_available,self.sku,self.price,self.regular_price,
          #                           self.sale_price,self.manage_stock,self.stock_quantity])



    def read_product(self):
        for item in self._product:
            print(item)

    def update_product(self):
        new = [self.id,self.tittle,self.short_description,self.description,self.slug,self.permalink,self.is_available,
               self.sku,self.price,self.regular_price,self.sale_price,self.manage_stock,self.is_visible,self.date_created_gmt,
               self.date_modified_gmt]

        self._product[:16] = new.__repr__()




    def delete_product(self):
        if self._product ==[]:
            print('nothing')
        else:
            print(self._product.clear())
