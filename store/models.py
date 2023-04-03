from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"

    @staticmethod
    def get_all_categories():
        return Category.objects.all()    

        
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return self.name
    
    class Meta:
        app_label = "store"
        db_table = "product"

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_products_by_id_by_list(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_product_by_id(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.objects.all()
 

class Customer(models.Model):
        firstname = models.CharField(max_length=50)
        lastname = models.CharField(max_length=50)
        mobile = models.CharField(max_length=15)
        email = models.EmailField()
        password = models.CharField(max_length=500)

        def __str__(self):
            return self.firstname
       
        class Meta:
            db_table = "customer"

        def isExists(self):
            if Customer.objects.filter(email = self.email):
                return True
            return False   
        
        @staticmethod
        def get_custmer_by_email(email):
            try:
                return Customer.objects.get(email=email)
            except:
                return False
            

class Order(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    date = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.products.name
    
    class Meta:
        db_table = "order"

    def place_order(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')    