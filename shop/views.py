from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from .models import Category, Product

#we import this from the cart app
from cart.forms import CartAddProductForm


#catalogue view
def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	return render(request,'shop/product/list.html',{'category': category,'categories': categories,'products': products})



def product_detail(request, id, slug):
	#The product_detail view expects the id and slug parameters 
	#in order to retrieve the Product instance.
	product = get_object_or_404(Product,id=id,slug=slug,available=True)

	#from the cart app
	cart_product_form = CartAddProductForm()

	return render(request,'shop/product/detail.html',{'product': product,'cart_product_form': cart_product_form})

