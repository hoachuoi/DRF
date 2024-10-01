from django.db import models

# Model đại diện cho Khách hàng
class Customer(models.Model):
    # CharField: lưu trữ chuỗi ký tự cho tên khách hàng
    name = models.CharField(max_length=200)
    
    # EmailField: lưu địa chỉ email khách hàng
    email = models.EmailField(unique=True)

    # DateTimeField: lưu thời gian khách hàng được tạo, auto_now_add tự động thêm ngày tạo
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Meta options để sắp xếp danh sách khách hàng theo thời gian tạo
        ordering = ['-created_at']
        verbose_name = "Khách hàng"
        verbose_name_plural = "Các khách hàng"

    def __str__(self):
        return self.name


# Model đại diện cho Sản phẩm
class Product(models.Model):
    name = models.CharField(max_length=200)  # Tên sản phẩm
    description = models.TextField()  # Mô tả sản phẩm chi tiết
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Giá sản phẩm
    stock = models.IntegerField()  # Số lượng hàng tồn kho

    class Meta:
        # Thêm index để tối ưu hóa tìm kiếm sản phẩm theo tên
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = "Sản phẩm"
        verbose_name_plural = "Các sản phẩm"

    def __str__(self):
        return self.name


# Model đại diện cho Đơn hàng
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Mối quan hệ khóa ngoại với Customer
    order_date = models.DateTimeField(auto_now_add=True)  # Ngày đặt hàng
    complete = models.BooleanField(default=False)  # Đơn hàng đã hoàn thành hay chưa
    transaction_id = models.CharField(max_length=100, unique=True)  # ID giao dịch duy nhất

    class Meta:
        ordering = ['-order_date']
        verbose_name = "Đơn hàng"
        verbose_name_plural = "Các đơn hàng"

    def __str__(self):
        return f"Order {self.transaction_id} by {self.customer.name}"

    # Phương thức để tính tổng giá trị đơn hàng
    @property
    def get_cart_total(self):
        # Tính tổng giá tiền từ tất cả các OrderItem liên quan đến đơn hàng này
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        return total

    # Phương thức để tính tổng số lượng mặt hàng trong đơn hàng
    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total


# Model đại diện cho từng mục trong Đơn hàng (OrderItem)
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)  # Sản phẩm trong đơn hàng
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  # Đơn hàng liên quan
    quantity = models.IntegerField(default=0)  # Số lượng sản phẩm
    date_added = models.DateTimeField(auto_now_add=True)  # Thời gian sản phẩm được thêm vào đơn hàng

    class Meta:
        verbose_name = "Mục đơn hàng"
        verbose_name_plural = "Các mục đơn hàng"

    def __str__(self):
        return f"{self.product.name} in order {self.order.transaction_id}"

    # Tính tổng giá trị của mục đơn hàng (product price * quantity)
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
