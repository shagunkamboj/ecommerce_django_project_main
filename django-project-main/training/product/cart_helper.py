
from django.shortcuts import render,redirect,HttpResponse
from .models import Product,Cart
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# def add_to_cart(request,**kwargs):
#     if id:=kwargs.get('id'):
#         product=Product.objects.get(id=id)
#         # print(product.id)
#         cart = Cart.objects.create(product1_id=product.id)
#         cart.save()
#     cart=Cart.objects.all()
#     return render(request,'add_to_cart.html',{'cart':cart})
# WITH-----SESSION 
def add_cart(request,**kwargs):
    if id:=kwargs.get('id'):
        product=Product.objects.get(id=id)
        cart_session = request.session.get('cart', [])
        cart_items = {'Name': product.name, 'price':product.price,'quantity':product.quantity,'id':product.pk}
        cart_session.append(cart_items)
        request.session['cart'] = cart_session
        print(request.session['cart'])
    return request.session['cart']    


# def delete_cart(request,**kwargs):
#     if id:=kwargs.get('id'):
#         product=Product.objects.get(id=id)
#         cart = request.session.get('cart', [])
#         for i in cart:
#             if i['id']==product.pk:
#                 #print("yyes")
#                 cart.remove(i)
#         request.session['cart']  = cart
            
#         return request.session['cart']    
    
def remove_from_cart_helper(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session['cart'] = cart
    return request.session['cart']    

def register_user(request):
    # form = RegisterForms()
    if request.method == 'POST':
        # print(request.POST)
        # import pdb; pdb.set_trace()
        print(request.user)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password =password)
        user.save()
    
    return render(request, 'register.html')
# def wishlist_helper(request,**kwargs):
#     if id := kwargs.get('id'):
#         item = Product.objects.get(id = id)
#         wishlist = request.session.get('wishlist',[])
#         wishlist_items = {'id':item.pk,'price':item.price,'quantity':item.quantity}
#         wishlist.append(wishlist_items)
#         request.session['wishlist'] = wishlist
#     return request.session['wishlist',None]


# def add_cart(request,**kwargs):
#     if id:=kwargs.get('id'):
#         product=Product.objects.get(id=id)
#         cart_session = request.session.get('cart', [])
#         cart_items = {'Name': product.name, 'price':product.price,'quantity':product.quantity,'id':product.pk}
#         cart_session.append(cart_items)
#         request.session['cart'] = cart_session
#         print(request.session['cart'])
#     return request.session['cart']    
    
# def login(request):
#     if request.method == "POST":
#         print(request.user)
#         name = request.POST.get('fname')
#         password = request.POST.get('password')
#         user = authenticate(request,name,password)
#         if user is not None:
#             login(request,user)
#             return redirect('Base.html')
#         else:
#             return HttpResponse("please enter valid details for login ")
#     return render(request,'login.html')


