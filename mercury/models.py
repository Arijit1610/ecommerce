from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class
class Product(models.Model):
	product_type = models.CharField(max_length=20, unique=True)
	def __str__(self):
		return self.product_type

class Fashion(models.Model):
	fashiontypes = {'M':'Mens', 'F':'Womens', 'C':'Children'}
	product_type = models.ForeignKey(Product, on_delete=models.CASCADE)
	brand_name = models.CharField(max_length=100)
	fashion_name = models.CharField(max_length=100)
	fashion_section = models.CharField(max_length=20, choices=fashiontypes)
	differentfashion = models.CharField(max_length=20, choices={
		'Shirt' : 'Shirt',
		'Trousers' : 'Trousers',
		'T-Shirt' : 'T-Shirt',
		'Formal' : 'Formal',
		'Shorts': 'Shorts'
	})
	size = models.CharField(max_length=3)
	price = models.DecimalField(decimal_places=2, max_digits=10)
	qty = models.IntegerField()
	description = models.CharField(max_length=1000)
	photo1 = models.ImageField(upload_to='product_images/', blank= True)
	photo2 = models.ImageField(upload_to='product_images/' ,blank= True)
	photo3 = models.ImageField(upload_to='product_images/', blank= True)
	photo4 = models.ImageField(upload_to='product_images/', blank= True)
	discount = models.IntegerField()

	def __str__(self):
		return self.fashion_name

class Eletronices(models.Model):

	product_type = models.ForeignKey(Product, on_delete=models.CASCADE)
	# photo1 = models.ImageField()
	company_name = models.CharField(max_length=100)
	product_name = models.CharField(max_length=100)
	types = models.CharField(max_length=20, choices={
		'Laptops' : 'Laptops',
		'Phone' : 'Phone',
		'Headphone' : 'Headphone',
		'Desktop' : 'Desktop',
		'Speaker': 'Speaker',
		'Watch' : 'Watch',
	})
	price = models.DecimalField(decimal_places=2, max_digits=10)
	qty = models.IntegerField()
	description = models.CharField(max_length=1000)
	photo1 = models.ImageField(upload_to='product_images/', blank= True)
	photo2 = models.ImageField(upload_to='product_images/' ,blank= True)
	photo3 = models.ImageField(upload_to='product_images/', blank= True)
	photo4 = models.ImageField(upload_to='product_images/', blank= True)
	discount = models.IntegerField()

	def __str__(self):
		return self.product_name
	

class BeautyCosmetics(models.Model):
	product_type = models.ForeignKey(Product, on_delete=models.CASCADE)
	# photo1 = models.ImageField()
	company_name = models.CharField(max_length=100)
	product_name = models.CharField(max_length=100)
	types = models.CharField(max_length=20, choices={
		'Hair cosmetics' : 'Hair cosmetics',
		'Foundation' : 'Foundation',
		'Concealer' : 'Concealer',
		'Skincare' : 'Skincare',
		'Nails': 'Nails',
		'Eyeshadow': 'Eyeshadow',
		'Bodycare': 'Bodycare',
		'Facemask' : 'Facemask',
		'Lips': 'Lips',
	})
	price = models.DecimalField(decimal_places=2, max_digits=10)
	qty = models.IntegerField()
	description = models.CharField(max_length=1000)
	photo1 = models.ImageField(upload_to='product_images/', blank= True)
	photo2 = models.ImageField(upload_to='product_images/' ,blank= True)
	photo3 = models.ImageField(upload_to='product_images/', blank= True)
	photo4 = models.ImageField(upload_to='product_images/', blank= True)
	discount = models.IntegerField()
	def __str__(self):
		return self.product_name


class BooksAndStationery(models.Model):
	product_type = models.ForeignKey(Product, on_delete=models.CASCADE)
	# photo1 = models.ImageField()
	publisher_name = models.CharField(max_length=100,blank=True)
	author_name = models.CharField(max_length=100, blank=True)
	edition = models.CharField(max_length=100, blank=True)
	title = models.CharField(max_length=100,blank=False,)
	types = models.CharField(max_length=20, choices={
		'Books' : 'Books',
		'Bag' : 'Bag',
		'School Essentials' : 'School Essentials',		
		'Office Essentials' : 'Office Essentials',		
	})
	price = models.DecimalField(decimal_places=2, max_digits=10)
	qty = models.IntegerField()
	description = models.CharField(max_length=1000)
	photo1 = models.ImageField(upload_to='product_images/', blank= True)
	photo2 = models.ImageField(upload_to='product_images/' ,blank= True)
	photo3 = models.ImageField(upload_to='product_images/', blank= True)
	photo4 = models.ImageField(upload_to='product_images/', blank= True)
	discount = models.IntegerField()
	def __str__(self):
		return self.title


class Sportsandoutdoor(models.Model):
	product_type = models.ForeignKey(Product, on_delete=models.CASCADE)
	# photo1 = models.ImageField()
	company_name = models.CharField(max_length=100)
	product_name = models.CharField(max_length=100)
	sportscatagory = models.CharField(max_length=20, choices={
		'Cricket' : 'Cricket',
		'Football' : 'Football',
		'Badminton' : 'Badminton',
		'Hocky' : 'Hocky',
		'Tennis' : 'Tennis',
	})
	price = models.DecimalField(decimal_places=2, max_digits=10)
	qty = models.IntegerField()
	description = models.CharField(max_length=1000)
	photo1 = models.ImageField(upload_to='product_images/', blank= True)
	photo2 = models.ImageField(upload_to='product_images/' ,blank= True)
	photo3 = models.ImageField(upload_to='product_images/', blank= True)
	photo4 = models.ImageField(upload_to='product_images/', blank= True)
	discount = models.IntegerField()
	def __str__(self):
		return self.product_name


class HomeandKitchen(models.Model):
	product_type = models.ForeignKey(Product, on_delete=models.CASCADE)
	# photo1 = models.ImageField()
	company_name = models.CharField(max_length=100)
	product_name = models.CharField(max_length=100)
	Productcatagory = models.CharField(max_length=20, choices={
		'Furniture' : 'Furniture',
		'Kitchen' : 'Kitchen',
		'Home Decor' : 'Home Decor',
	})
	price = models.DecimalField(decimal_places=2, max_digits=10)
	qty = models.IntegerField()
	description = models.CharField(max_length=1000)
	photo1 = models.ImageField(upload_to='product_images/', blank= True)
	photo2 = models.ImageField(upload_to='product_images/' ,blank= True)
	photo3 = models.ImageField(upload_to='product_images/', blank= True)
	photo4 = models.ImageField(upload_to='product_images/', blank= True)
	discount = models.IntegerField()
	def __str__(self):
		return self.product_name
