from django.shortcuts import render
from .models import Product
from .models import Customer, Order

app_name = 'demo'
# View trả về danh sách các sản phẩm
def product_list(request):
    products = Product.objects.all().order_by('-price')  # Sắp xếp sản phẩm theo giá giảm dần
    return render(request, 'product_list.html', {'products': products})

# View trả về thông tin khách hàng và đơn hàng của họ
def customer_orders(request, customer_id):
    customer = Customer.objects.get(id=customer_id)  # Lấy thông tin khách hàng theo ID
    orders = Order.objects.filter(customer=customer, complete=True)  # Lấy các đơn hàng đã hoàn thành
    return render(request, 'customer_orders.html', {'customer': customer, 'orders': orders})

 #Tìm kiếm khách hàng bằng Lookup Expressions
from .models import Customer

# View để tìm kiếm khách hàng dựa trên từ khóa
def search_customers(request):
    query = request.GET.get('q', '')
    customers = Customer.objects.filter(name__icontains=query)  # Tìm kiếm tên chứa từ khóa không phân biệt hoa thường
    return render(request, 'customer_search.html', {'customers': customers})

from .models import Order

# View để lọc đơn hàng dựa trên nhiều điều kiện
def filter_orders(request):
    status = request.GET.get('status', 'completed')  # Trạng thái đơn hàng (mặc định là 'completed')
    orders = Order.objects.filter(complete=(status == 'completed'))  # Lọc đơn hàng dựa trên trạng thái hoàn thành
    return render(request, 'order_list.html', {'orders': orders})
#Tính tổng số tiền đơn hàng với aggregate()
from django.db.models import Sum
from .models import OrderItem

# View tính tổng giá trị các sản phẩm đã bán
def total_sales(request):
    total_sales_value = OrderItem.objects.aggregate(total=Sum('product__price'))['total']
    return render(request, 'sales_total.html', {'total_sales_value': total_sales_value})


from .models import Product

# View trả về danh sách sản phẩm sắp xếp theo giá giảm dần và giới hạn 5 sản phẩm đầu tiên
def top_products(request):
    products = Product.objects.all().order_by('-price')[:5]  # Sắp xếp giá giảm dần và giới hạn 5 sản phẩm
    return render(request, 'top_products.html', {'products': products})


#Sử dụng annotate() để đếm số lượng đơn hàng của mỗi khách hàng
from django.db.models import Count
from .models import Customer

# View trả về danh sách khách hàng cùng số lượng đơn hàng của họ
def customer_order_count(request):
    customers = Customer.objects.annotate(order_count=Count('order'))
    return render(request, 'customer_order_count.html', {'customers': customers})

