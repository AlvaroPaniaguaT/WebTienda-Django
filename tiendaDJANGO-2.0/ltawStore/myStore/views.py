from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpRequest, HttpResponse, JsonResponse
import datetime


# ---------------------------------VIEWS----------------------------------
def myAJAX_view(request):
    if request.method == 'POST':
        searchText = request.body
        prodList = Product.objects.all().filter(name__icontains=str(searchText))

        res = getSingleNames(prodList)
        return HttpResponse(res)

def index_view(request):
    response = render(request, 'index.html', {'item_num':'0'})
    if 'carro' in request.COOKIES:
        total_products = parse_cart(request.COOKIES['carro'])
        response = render(request, 'index.html', {'item_num':total_products})
        print('Cookie already exists')
    else:
        print('Setting cookie')
        response.set_cookie('carro', '', max_age = 86400)

    return response

def bike_view(request, prod_num):
    total_products = parse_cart(request.COOKIES['carro'])
    if prod_num == '0':
        the_bikes = Bikes.objects.all()
        return render(request, 'items.html', {'items': the_bikes, 'item_num':total_products})
    elif prod_num == '1':
        m_bikes = get_list_or_404(Bikes,b_type='montana')
        return render(request, 'items.html', {'items':m_bikes, 'item_num':total_products})
    elif prod_num == '2':
        m_bikes = get_list_or_404(Bikes,b_type='descenso')
        return render(request, 'items.html', {'items':m_bikes, 'item_num':total_products})
    elif prod_num == '3':
        m_bikes = get_list_or_404(Bikes,b_type='carretera')
        return render(request, 'items.html', {'items':m_bikes, 'item_num':total_products})
    else:
        return render(request, 'index.html', {'item_num':total_products})


def cd_type_view(request, prod_num):
    total_products = parse_cart(request.COOKIES['carro'])
    if prod_num == '0':
        the_CDs = CD.objects.all()
        return render(request, 'items.html', {'items': the_CDs, 'item_num':total_products})
    elif prod_num == '1':
        g_CD = get_list_or_404(CD, cd_genre='rock')
        return render(request, 'items.html',{'items':g_CD, 'item_num':total_products})
    elif prod_num == '2':
        g_CD = get_list_or_404(CD, cd_genre='hip hop')
        return render(request, 'items.html',{'items':g_CD, 'item_num':total_products})
    elif prod_num == '3':
        g_CD = get_list_or_404(CD, cd_genre='pop')
        return render(request, 'items.html',{'items':g_CD, 'item_num':total_products})
    elif prod_num == '4':
        g_CD = get_list_or_404(CD, cd_genre='heavy')
        return render(request, 'items.html',{'items':g_CD, 'item_num':total_products})
    elif prod_num == '5':
        g_CD = get_list_or_404(CD, cd_genre='house')
        return render(request, 'items.html',{'items':g_CD, 'item_num':total_products})
    else:
        return render(request, 'index.html', {'item_num':total_products})


def book_type_view(request, prod_num):
    total_products = parse_cart(request.COOKIES['carro'])
    if prod_num == '0':
        the_books = Books.objects.all()
        return render(request, 'items.html', {'items': the_books, 'item_num':total_products})
    elif prod_num == '1':
        g_Books = get_list_or_404(Books, book_genre='poesia')
        return render(request, 'items.html', {'items':g_Books, 'item_num':total_products})
    elif prod_num == '2':
        g_Books = get_list_or_404(Books, book_genre='misterio')
        return render(request, 'items.html', {'items':g_Books, 'item_num':total_products})
    elif prod_num == '3':
        g_Books = get_list_or_404(Books, book_genre='ficcion')
        return render(request, 'items.html', {'items':g_Books, 'item_num':total_products})
    else:
        return render(request, 'index.html', {'item_num':total_products})

def product_zoom_view(request, prod_name):
    total_products = parse_cart(request.COOKIES['carro'])
    prod_name = prod_name.replace("-"," ")
    the_product = get_object_or_404(Product, name=prod_name)

    if the_product.p_type == 'bike':
        p_extension = get_object_or_404(Bikes, name=prod_name)
    elif the_product.p_type == 'cd':
        p_extension = get_object_or_404(CD, name=prod_name)
    elif the_product.p_type == 'book':
        p_extension = get_object_or_404(Books, name=prod_name)

    return render(request, 'p-buy.html', {'item':the_product, 'item_type':p_extension, 'item_num':total_products})

def endbuy_view(request, prod_name):
    total_products = parse_cart(request.COOKIES['carro'])
    error_msg = 'Su formulario esta incompleto.'

    prod_name = prod_name.replace("-"," ")
    the_product = get_object_or_404(Product, name=prod_name)

    if the_product.p_type == 'bike':
        p_extension = get_object_or_404(Bikes, name=prod_name)
    elif the_product.p_type == 'cd':
        p_extension = get_object_or_404(CD, name=prod_name)
    elif the_product.p_type == 'book':
        p_extension = get_object_or_404(Books, name=prod_name)

    payForm = PaymentForm()
    if request.method == 'POST':
        final_form = PaymentForm(request.POST)
        if final_form.is_valid():
            prod_name = prod_name.replace("-"," ")
            the_product = Product.objects.get(name=prod_name)
            date_n = datetime.datetime.now()

            #Uncomment to clean Orders Database
            #BuyOrders.objects.all().delete()

            fill_order(final_form, date_n, the_product)

            latest_order = BuyOrders.objects.latest('id')

            return render(request, 'confirm.html', {'data':final_form, 'product':the_product, 'date_now':date_n, 'order_id': latest_order.id, 'item_num':total_products})

        return render(request, 'buy.html', {'item':the_product, 'item_type': p_extension, 'message': error_msg, 'payment_form':payForm, 'item_num':total_products})
    else:
        return render(request, 'buy.html', {'item':the_product, 'item_type':p_extension, 'payment_form':payForm, 'item_num':total_products})

def confirm_view(request, orderID):
    total_products = parse_cart(request.COOKIES['carro'])
    confirm_message = 'Su peticion ha sido tramitada con exito.'
    order_to_confirm = BuyOrders.objects.get(id=orderID)
    product_update = Product.objects.get(name=order_to_confirm.product_n)
    product_update.stock = product_update.stock - 1
    product_update.save()
    order_to_confirm.confirmed = True
    order_to_confirm.save()
    return render(request, 'index.html', {'message': confirm_message, 'item_num':total_products})


def cart_view(request):
    cart_form = PaymentFormCart()
    total_products = parse_cart(request.COOKIES['carro'])
    q_array, prod_array = getAllCart(request.COOKIES['carro'])
    array_of_products = get_from_DB(prod_array)
    full_array = create_my_array(array_of_products, q_array)
    f_price = calculatePrice(full_array)

    if request.body == 'update':
        matrix_to_send = createMatrix(full_array)
        print(matrix_to_send)
        return JsonResponse({'matrix': matrix_to_send, 'total_p': f_price})
    else:
        return render(request, 'cart.html', {'item_num':total_products, 'prod_array': full_array, 'total_price':f_price, 'my_form': cart_form})

def confirm_cart(request):
    confirm_message = 'Su peticion ha sido tramitada con exito.'

    if 'carro' in request.COOKIES:
        quant_array, name_array = getAllCart(request.COOKIES['carro'])

        for i in range(0, len(quant_array)):
            if request.method == 'POST':
                final_form = PaymentFormCart(request.POST)
                print(final_form)
                if final_form.is_valid():
                    name_array[i].replace("-"," ")
                    the_product = Product.objects.get(name=name_array[i])
                    date_n = datetime.datetime.now()
                    fill_order_cart(final_form, quant_array[i], date_n, the_product)
                    
        response = render(request, 'index.html', {'item_num':0, 'message':confirm_message})
        response.set_cookie('carro', '', max_age = 86400)
        return response
    else:
        return render(request, 'index.html', {'message': confirm_message})

# ---------------------------------AUX FUNCTIONS-----------------------------

def fill_order(form_data, current_date, _product):

    new_order = BuyOrders()

    new_order.date = current_date
    new_order.product_n = _product.name
    new_order.quantity = form_data.cleaned_data['quantity']
    new_order.total_price = form_data.cleaned_data['quantity'] * _product.price
    new_order.payMeth = form_data.cleaned_data['payMeth']
    new_order.full_name = form_data.cleaned_data['full_name']
    new_order.email_address = form_data.cleaned_data['email_address']
    new_order.country = form_data.cleaned_data['country']
    new_order.city = form_data.cleaned_data['city']
    new_order.address = form_data.cleaned_data['address']
    new_order.add_comments = form_data.cleaned_data['aditional_comments']
    new_order.confirmed = False
    new_order.save()

def fill_order_cart(form_data, quant, current_date, my_product):

    new_order = BuyOrders()

    new_order.date = current_date
    new_order.product_n = my_product.name
    new_order.quantity = quant
    new_order.total_price = quant * my_product.price
    new_order.payMeth = form_data.cleaned_data['payMeth']
    new_order.full_name = form_data.cleaned_data['full_name']
    new_order.email_address = form_data.cleaned_data['email_address']
    new_order.country = form_data.cleaned_data['country']
    new_order.city = form_data.cleaned_data['city']
    new_order.address = form_data.cleaned_data['address']
    new_order.add_comments = form_data.cleaned_data['aditional_comments']
    new_order.confirmed = True
    new_order.save()

def parse_cart(cart_items):
    total_products = 0
    cart = cart_items.split('|')
    for product in cart:
        try:
            total_products = total_products + int(product)
        except ValueError:
            pass

    return total_products

def getAllCart(cart_items):
    cart =  cart_items.split('|')
    quant_array = []
    prod_n_array = []
    for product in cart:
        try:
            quant_array.append(int(product))
        except ValueError:
            if product != '':
                prod_n_array.append(product.replace("-",' '))

    return quant_array, prod_n_array

def get_from_DB(products_name_array):
    return_array = []
    for product_name in products_name_array:
        return_array.append(get_object_or_404(Product, name=product_name))

    return return_array

def create_my_array(prod_obj_array, quantity_array):
    aux_array = []
    for i in range(0, len(prod_obj_array)):
        aux_array.append({'product':prod_obj_array[i], 'quantity':quantity_array[i]})

    return aux_array

def calculatePrice(myArray):
    total = 0
    for prod in myArray:
        total = total + (int(prod['product'].price) * int(prod['quantity']))

    return total

def getSingleNames(prod_list):
    auxArray = []
    if prod_list:
        for prod in prod_list:
            if prod.p_type == 'bike':

                curProd = Bikes.objects.get(name=prod.name)
                auxArray.append(transformtoHTML(curProd))
            elif prod.p_type == 'cd':

                curProd = CD.objects.get(name=prod.name)
                auxArray.append(transformtoHTML(curProd))
            else:

                curProd = Books.objects.get(name=prod.name)
                auxArray.append(transformtoHTML(curProd))

    return auxArray

def transformtoHTML(curProd):
    auxName = curProd.name.replace(" ", "-")
    the_code = '<li><a href="/p-buy/' + auxName + '">' + curProd.name + '</a></li>'

    return the_code

def createMatrix(p_q_array):
    myMatrix = []

    for i in p_q_array:

        myMatrix.append([i['product'].name, i['product'].price, i['quantity'] ])


    return myMatrix
