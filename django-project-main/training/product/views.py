from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import ProductForm,RegisterForms,login_product,AddressForm,UserProfile
from .models import Product,Cart,AddressModel,Order,UserProfile,Wishlist,Order_item
from product.cart_helper import add_cart,remove_from_cart_helper,register_user,login
from django.contrib.auth import authenticate,login as auth,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
   





class Product_Serializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class Address_Serializer(ModelSerializer):
    class Meta:
        model = AddressModel
        fields = "__all__"
class UserSerializer(ModelSerializer):
    class Meta:
        model = User 
        fields = ['username','password']
        
        
        
@api_view(http_method_names=('post',))
def login_user(request):
    username=request.data['username']
    password=request.data['password']
    user=authenticate(username=username,password=password)
    auth(request,user)
    user= User.objects.get(username=username)
    token=Token.objects.create(user=user)
    serializer = UserSerializer(user)
    return Response({'token':token.key},status=status.HTTP_200_OK)
@api_view()
@permission_classes([IsAuthenticated])
def logout_users(request):
    try:
        token=Token.objects.get(user_id=request.user.id)
        token.delete()
        logout(request)
    except:
        return Response({'message':"not loged"})
    return Response({'user':"successfully login"})          
@api_view()
def product_view(request):
    p = Product.objects.all()
    serializer = Product_Serializer(p, many=True)# models firlds name product
    return Response(serializer.data)
#with particular id 
# def product_view(request,pk):
#     p = Product.objects.get(id = pk )
#     serializer = Product_Serializer(p)
#     return Response(serializer.data)
@api_view(http_method_names=('post',))

def product_create(request,*args,**kwargs):
    p = Product_Serializer(data = request.data)
    if p.is_valid():
        p.save()
        return Response({"data":p.data})
    else:
        return Response({'error':p.errors})

@api_view(http_method_names=('put',))
#@permissions_classes([IsAuthenticated])
def update_product(request,pk):
    p = Product.objects.get(id = pk)
    Serializer = Product_Serializer(p,data = request.data)
    Serializer.is_valid(raise_exception=True)
    Serializer.save()
    return Response({"message":Serializer.data})
    
    
@api_view(http_method_names=('delete',))
def delete(request,pk):
    p = Product.objects.get(id = pk)
    p.delete()
    return Response({"message":"the object has been deleted"})
    
@api_view(http_method_names=('patch',))
def partial_update(request,pk):
    p = Product.objects.get(id = pk)
    serializer = Product_Serializer(p,data = request.data)
    serializer.is_valid(raise_exception= True)
    serializer.save()
    return Response({"message":serializer.data})
#################################Address VIEW #############################
@api_view()
def address_view(request):
    p = AddressModel.objects.all()
    serializer = Address_Serializer(p, many=True)# models firlds name product
    return Response(serializer.data)

@api_view(http_method_names=('post',))
@permission_classes([IsAuthenticated])
def address_create(request,*args,**kwargs):
    request.data['user_id'] = request.user.id
    p = Address_Serializer(data = request.data)
    if p.is_valid():
        p.save()
        return Response({"data":p.data})
    else:
        return Response({'error':p.errors},status=status.HTTP_400_BAD_REQUEST)

@api_view()
@permission_classes([IsAuthenticated])
def address_list(request):
    addresses = AddressModel.objects.all()
    return Response({'Address':AddressModelSerializer(addresses,many=True).data},status=status.HTTP_200_OK)
@api_view(http_method_names=('put',))
@permission_classes([IsAuthenticated])
def update_address(request, pk):
    address = AddressModel.objects.get(id=pk)
    serializer = Address_Serializer(address, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({'Address':serializer.data}, status=status.HTTP_200_OK)



@api_view(http_method_names=('delete',))
@permission_classes([IsAuthenticated])
def delete_address(request,pk):
    p = AddressModel.objects.get(id = pk)
    p.delete()
    return Response({"message":"the object has been deleted"}, status=status.HTTP_202_ACCEPTED)

@api_view(http_method_names=('patch',))
@permission_classes([IsAuthenticated])

def partial_update_address(request,pk):
    address = AddressModel.objects.get(id=pk)
    serializer = Address_Serializer(address, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({'Address':serializer.data}, status=status.HTTP_200_OK)




# Create your views here.
def work(request):
    return render(request,'staticblog.html')
def home_product(request):
    
    return render(request,'index_product.html')
def knowaboutus(request):
    return render(request,'knowaboutus.html')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(commit = False)
            tag = request.POST.getlist('tag')
            product.save()
            product.tag.set(tag)
    else:
        form = ProductForm()
    return render(request,'add.html', {'form': form})
# @login_required
# def wishlist(request):
#     if request.method == 'POST':
#         product_id = request.POST.get('product_id')
#         action = request.POST.get('action')
#         product = Product.objects.get(id=product_id)
#         if action == 'add':
#             wishlist = Wishlist.objects.create(user=request.user, product=product)
#             wishlist.save()
#         elif action == 'remove':
#             wishlist = Wishlist.objects.get(user=request.user, product=product)
#             wishlist.delete()
#         return redirect('home')
#     else:
#         #wishlist_items = wishlist.objects.filter(user=request.user)
#         wishlist = Wishlist.objects.get_or_create(user=request.user)
#         context = {
#             'wishlist_items': wishlist_items
#         }
#         return render(request, 'wishlist.html', context)

def register_user(request):
    form=RegisterForms()
    if request.method=='POST':
        userName = request.POST.get('username', None)
        userPass = request.POST.get('password', None)
        user = User.objects.create_user(userName, userPass)
        user.save()
    return render(request,'register.html', {'form': form})

    
def create_product(request): 
    form_Product = ProductForm()
    if request.method == 'POST':
        form_Product = ProductForm(request.POST, request.FILES)
        if form_Product.is_valid():
            form_Product.save()
    return render(request,'create.html', {'form': form_Product})
    
# def list_all_products(request):
#     product = Product.objects.all()
#     paginator = Paginator(product,5)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     #return render(request,'list_all_product.html', {'products': product})
#     return render(request,'list_all_product.html', {'page_obj': page_obj}) 
class list_all_products(ListView):
    model = Product
    template_name = "product_get.html"
    paginate_by = 5
    context_object_name= "products"
      

def delete_product(request,**kwargs):
    if id:=kwargs.get('id'):
        product = Product.objects.get(id=id)
        product.delete()
    product = product.objects.all()
    return render(request,'list_all.html', {'product': product})
# class remove_cart(DetailView):
#     model = Product
#     template_name = "add_to_cart.html"
    

# def add_to_cart(request,**kwargs):
#     helper_cart=add_cart(request,**kwargs)
#     return render(request,'add_to_cart.html', {'helper_cart': helper_cart})



def remove_cart(request,**kwargs):
    if pk:=kwargs.get('id'):
        cart_delete =remove_from_cart_helper(request, pk)
    print(cart_delete)
    messages.success(request,'Product remove from Cart!!')
    return render(request, 'add_to_cart.html') and redirect('/cart/list')
    cart=delete_cart(request,**kwargs)
    print(cart)
    return redirect('/cart/list')


# def cart_list(request):
#     cart= request.session['cart']
#     print(cart)
#     return render(request,'add_to_cart.html', {'cart':cart})
def cart_list(request):
    cart = Cart.objects.all()
    total_price  = sum(p.product1.price  for p in cart )
    return render(request,'cart_list.html', {'Cart': cart, 'amount':total_price}) 
def add_to_cart(request,**kwargs):
     if id:=kwargs.get('id'):
            product = Product.objects.get(id=id)
            
            Cart.objects.create(product1_id=product.pk,quantity=1,user_id_id=request.user.id)
     return redirect('cart-list')
def increment_item(request, **kwargs):
    if id:=kwargs.get('id'):
        cart  = Cart.objects.get(id=id)
      
        cart.quantity= int(cart.quantity)+ 1
        print(cart.quantity)
        cart.save()
        return redirect('cart-list')
    return render(request, 'cart_list.html')
   

def del_cart(request,**kwargs):
    if id:=kwargs.get('id'):
            cart= Cart.objects.get(id=id)
            cart.delete()
    return redirect('cart-list')
def cart_list(request):
    cart = Cart.objects.all()
    # for p in cart:
    #     print(p.product1.price)
    # total_price  = sum(p.product1.price  for p in cart )
    return render(request,'cart_list.html', {'Cart': cart}) 

# def registered_user(request):
#     user_login=request.session['user_login']   
#     return render(request)  


# def register(request):
#     return render(request,'register.html')
def register_user(request):
    form =  RegisterForms()
    if request.method == "POST":
        print(request.user)
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username,password = password,email=email)
        user.save()
        messages.success(request, f'Hi {username}, your account was created successfully')
            

    return render(request, 'register.html', {'form': form})

# def login(request):
#     form = login_product()
#     if request.method == "POST":
#         print(request.user)
#         name = request.POST.get('fname')
#         password = request.POST.get('password')
#         user = authenticate(request,name,password)
#         if user is not None:
#             login(request,user)
#             print(request.user)
#             return redirect('Base.html')
#         else:
#             return HttpResponse("please enter valid details for login ")
#     return render(request,'login.html',{'form':form})
def login(request):
    form = login_product()
    if request.method == "POST":
        print(request.user)
        name= request.POST['username']
        password = request.POST.get('password')
        user = authenticate(request,username=name,password=password)
        if user is not None:
            print("yes")
            auth(request,user)
            print(request.user)
            messages.success(request,'You were successfully login')
            return redirect('home')
        else:
            print("please enter valid details for login ")
    return render(request,'login.html',{'form':form})
def logout(request):
    logout(request)   
    return render(request,'Base.html')

# def add_to_cart(request,**kwargs):
#     if id:=kwargs.get('id'):
#         product=Product.objects.get(id=id)
#         # print(product.id)
#         cart = Cart.objects.create(product1_id=product.id)
#         cart.save()
#     cart=Cart.objects.all()
#     return render(request,'add_to_cart.html',{'cart':cart})
# # WITH-----SESSION 
# def add_to_cart(request,**kwargs):
#     if id:=kwargs.get('id'):
#         product=Product.objects.get(id=id)
#         cart_session = request.session.get('cart', [])
#         cart_items = {'Name': product.name, 'price':product.price,'quality':product.quality}
#         cart_session.append(cart_items)
#         request.session['cart'] = cart_session
#         print(request.session['cart'])
#     return render(request,'add_cart.html')

def delete_cart(request,**kwargs):
    if id:=kwargs.get('id'):
        cart = Cart.objects.get(id=id)
        cart.delete()
    cart = Cart.objects.all()
    return render(request,'add_to_cart.html', {'cart': cart})

def privacypolicy(request):
    return render(request,'privacy.html')

# def checkout(request):
#     cart =request.session['cart']
#     address = AddressModel.objects.get(user_id= request.user.id)
#     for pr_id, p in cart.items():
#         total = sum(int(p['price']) * p['quantity'] )
#         print("total sum = ",total)
#         return render(request,'checkout_page.html',{'address':address, 'amount':total})
# def checkout(request):
#     cart = AddressModel.objects.filter(id = request.id)
#     for item in cart:
#         if item.product1>item.quantity:
#             Cart.objects.delete(id = item.id)
#     cartitems = Cart.objects.filter(user = request.user)
#     total_price = 0 
#     for item in cartitems:
#         total_price = total_price+item.product1
#     context = {'cartitems':cartitems,'total_price':total_price}
#     return render(request,'checkout_page.html',context)
# def checkout_page(request):
#     cart = request.session.get('cart',[])
#     #cart = request.session['cart']
#     address = AddressModel.objects.filter(user_id = request.user.id)
    
#     total_price = (sum(int(sp['price'] * sp['quantity']))for sp in cart )
    
#     return render(request,'checkout_page.html',{'address':address, 'total_amount':total_price})
def decrement_item(request, **kwargs):
    if id:=kwargs.get('id'):
        cart  = Cart.objects.get(id=id)
      
        cart.quantity= int(cart.quantity)- 1
        print(cart.quantity)
        cart.save()
        return redirect('cart-list')
    return render(request, 'cart_list.html')  
def checkout(request):
    cart = Cart.objects.filter(user_id_id = request.user.id)
    address = AddressModel.objects.get(user_id_id = request.user.id)
    total_cost = sum(p.product1.price for p in cart)
    print(total_cost)
    return render(request,'checkout_page.html',{'cart':cart,'address':address, 'total_amount':total_cost})  

    #return render(request, 'address.html')
def order_create(request):
    cart = Cart.objects.filter(user_id_id=request.user.id)
    address = AddressModel.objects.get(user_id_id=request.user.id)
    for p in cart:
        total_cost = int(p.quantity) * p.product1.price
        Order.objects.create(user_id_id=request.user.id, product_id=p.product1.pk,address_id=address.pk, total_cost=total_cost)
        messages.success(request , "YOUR ORDER WAS SUCCESFULLY PLACED KEEP SHOPPING!!")
    return redirect('home')

def  add_address(request):
    form  = AddressForm()
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            forms  = form.save(commit=False)
            forms.user_id_id = request.user.id
            forms.save()
           
    return render(request, 'address.html', {'form':form})
def continueshopping(request):
    return render(request,'continue.html')

def profile(request):
    return render(request, 'profile.html')
def change_password(request):
    print(request.method)
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            # /main_pass = request.POST.get('confirm_password')
            user = User.objects.get(username = username)
            print(user)
            user.set_password(password)
            user.save()
            return redirect('login')
    return render(request,'change_password.html')

def add_wishlist(request,**kwargs):
    if pk := kwargs.get('id'):
        product = Product.objects.get(id = pk)
        Wishlist.objects.create(user_id=request.user.id,product_id = product.pk)
    return redirect('get-wishlist')

def get_wishlist(request):
    wishlist  = Wishlist.objects.filter(user_id = request.user.id)
    return render(request, 'wishlist.html', {'wishlist':wishlist})


def del_to_wishlist(request,**kwargs):
    if pk:= kwargs.get('id'):
        wishlist = Wishlist.objects.get(id=pk)
        wishlist.delete()
        return redirect('home')
    return render(request,'wishlist.html', {'wishlist':wishlist})

def similar_product(request,**kwargs):
    if pk:=kwargs.get('id'):
        print("yes")
        product = Product.objects.get(id=pk)
        category = Product.objects.filter(category = product.category)
            
    return render(request,'product_list.html',{'product': product,'category':category})
def searchMatch(query, item):
    if query in item.name or query in item.category:
        return True
    else:
        return False
def search(request):
    query= request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + int((n / 4) - (n // 4))
        if len(prod)!= 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg":""}
    if len(allProds)==0 or len(query)<4:
        params={'msg':"Please make sure to enter relevant search query"}
    return render(request, 'search.html', params)

# def product_detail(request,id):
#     product = Product.objects.get(id=id)
# 	related_products = Product.objects.filter(category=product.category).exclude(id=id)[:4]
#     return render(request, 'product_detail.html',{'data':product,'related':related_products})
def product_detail(request,id):
    product = Product.objects.get(id = id)
    related_product = Product.objects.filter(category=product.category).exclude(id = id )[:4]
    return render(request, 'product_detail.html',{'data':product,'related':related_products})

def order_item(request, order_id):
    cart =request.session['cart']
    for p_id , p in cart.items():
        total_sum = int(p['price']) * p['quantity']
        Order_item.objects.create(order_id=order_id,product_id=p['id'],item_price=total_sum)
        print("yes Done ")
def searchMatch(query, item):
    if query in item.name or query in item.category:
        return True
    else:
        return False
# def search(request):
#     query= request.GET.get('search')
#     allProds = []
#     catprods = Product.objects.values('category', 'id')
#     cats = {item['category'] for item in catprods}
#     for cat in cats:
#         prodtemp = Product.objects.filter(category=cat)
#         n = len(prod)
#         nSlides = n // 4 + int((n / 4) - (n // 4))
#         if len(prod)!= 0:
#             allProds.append([prod, range(1, nSlides), nSlides])
#     params = {'allProds': allProds, "msg":""}
#     if len(allProds)==0 or len(query)<4:
#         params={'msg':"Please make sure to enter relevant search query"}
#     return render(request, 'search.html', params)