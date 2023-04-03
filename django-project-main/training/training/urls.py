"""training URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static 
from product import views
# from django.confimport setting
from blog.views import update_blog,blogs_view,blogslistcreate,blogslist,blogsr,blogscreate,blogs_create,delete_blog,login_user,home_blog,logout_user,registered_user,publish_blog,update_user,publish_blog,CreateFormview, list_all_blogs, Blogview
from product.views import work,productscreate,address_list,logout_users,product_create,login_user,address_view,delete_address,update_address,address_create,partial_update_address,partial_update,delete,create_product,list_all_products,delete_product,add_to_cart,remove_cart,cart_list,login,register_user,home_product,knowaboutus,privacypolicy,logout,del_cart,checkout,add_address,order_create,increment_item,decrement_item,continueshopping,profile,change_password,add_wishlist,get_wishlist,del_to_wishlist,similar_product,search,product_detail,product_view,add_product,update_product,productlist

urlpatterns = [
     path('',views.home_product,name='home'),
    path('create/blog',CreateFormview.as_view(),name='create-blog'),
    path('del/blog',Blogview.as_view(),name='blog'),
    path('product/view', product_view),
    path('product/create',product_create),
    path('update/<int:pk>',update_product),
    path('delete/<int:pk>',delete),
    path('pupdate/<int:pk>',partial_update),
    ########## address view #####
    path('address/view', address_view),
    path('address/create',address_create),
    path('addupdate/<int:pk>',update_address),
    path('adddelete/<int:pk>',delete_address),
    path('partialupdate/<int:pk>',partial_update_address),
    path('address/list',address_list),
    
    path('login/users/', login_user),
    path('logout/users/',logout_users,name='logoutusertoken'),
    #"794dcbf112f6ee6d19f099b7fd0887b4853347b5"
    #path('aproduct/<int:pk>/', product_view),
    path('',home_product,name='home'),
    path('work',work),
    path('shop/add',add_product,name='add'),
    path('productcreate',create_product.as_view(),name='create'),
    #path('product/list',list_all_products.as_view(),name='productlist'),
    path('product/delete',delete_product,name = 'delete'),
    path('add_to_cart/<int:id>/add',add_to_cart,name = "add_to_cart"),
    #path('cart/details', list_cart, name='List_cart'),
    #path('cart/<int:id>/del',del_cart,name = "del_cart"),
    path('remove_from_cart/<int:id>',remove_cart, name='remove_from_cart'),
    path('wishlist-product/<int:id>',add_wishlist,name='wishlist'),
    path('wishlist-get/',get_wishlist,name='get-wishlist'),
    path('wishlist-del/<int:id>',del_to_wishlist,name='del-wishlist'),
    path('shop/search/',search,name = 'search'),
    #path('cart/<int:id>',del_cart),
    path('privacypolicy',privacypolicy,name = "privacypolicy"),
    # path('register/user',registered_user),
    path('cart/list', cart_list,name='cart_list'),
    path('register/', register_user,name='register'),
    path('login_product/',login,name='login'),
    path('admin/', admin.site.urls),
    path('create/blog',CreateFormview.as_view(),name='create-blog'),
    path('del/blog',Blogview.as_view(),name='blog'),
    path('logout/',logout,name = "logout"),
    path('product/list',list_all_products.as_view(),name='product-list'),
    path('product/delete',delete_product),
    path('add_to_cart/<int:id>',add_to_cart,name='add_cart'),
    # path('cart/<int:id>',del_cart),
    # path('register/user',registered_user),
    path('cart/list', cart_list,name='cart-list'),
    path('cart/del/<int:id>',del_cart, name='delete-cart'),
    path('product/<int:id>',similar_product,name = 'product'),
    #path('wishlist/', wishlist, name='wishlist'),
    # path('',home,name='home page'),
    # path('hi/',csrf_exempt(hello)),
    # path('form/',form_view),
    # path('demo/create',create_blog,name='creating'),
    path('checkout',checkout, name='checkout'),
    # path('demo/list',list_all_blogs,name='listing'),
    path('listallblog/',list_all_blogs.as_view(),name = "l"),
    path('demo/<int:id>/update',update_blog,name='updating'),
    path('demo/<int:id>/delete',delete_blog,name='deleting'),
    path('login/',login_user,name='bloglogin'),  
    path('change_pass/',update_user,name='pasword_update'),
    path('logout/',logout_user,name='logout'),
    path('registered/',registered_user,name='registered'),
    # path('publish/',publish_blog,name='published')
    path('publish/blog_publish/<int:id>',publish_blog,name='publish-blog'),
    path('know/',knowaboutus,name = "know"),
    path('ship_details/', add_address , name='address'),
    path('order', order_create, name='order'),
    path('increment/<int:id>',  increment_item, name='increment'),
    path('decrement/<int:id>',  decrement_item, name='decrement'),
    path('continue/',  continueshopping, name='continue'),
    path('profile/', profile, name='profile'),
    path('change-pass/',change_password ,name='change'),
    path('product/<int:id>',product_detail,name='product_detail'),
   
    path('productlist/',productlist.as_view(),name = "p"),
    
    path('productscreate/',productscreate.as_view(),name = "p"),
    path('blogss/',blogs_view,name='blog'),
    path('blogsscreate/',blogs_create,name='blog'),
    path('blogslist/',blogslist.as_view(),name = "b1"),
    path('blogscreate/',blogscreate.as_view(),name = "b2"),
    path('blogsr/<int:pk>',blogsr.as_view(),name = "b3"),
    path('blogslistcreate/',blogslistcreate.as_view(),name = "b4"),

 
    
    
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
