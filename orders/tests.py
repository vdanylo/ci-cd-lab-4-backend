from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import Order, OrderItem, ShippingAddress
from products.models import Product

User = get_user_model()

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.order = Order.objects.create(
            user=self.user,
            payment_method='Credit Card',
            tax_price=10.50,
            shipping_price=5.00,
            total_price=100.00,
            is_paid=True,
            paid_at=timezone.now(),
            is_delivered=False,
            created=timezone.now()
        )

    def test_order_creation(self):
        self.assertEqual(self.order.user.username, 'testuser')
        self.assertEqual(self.order.payment_method, 'Credit Card')
        self.assertEqual(self.order.tax_price, 10.50)
        self.assertEqual(self.order.shipping_price, 5.00)
        self.assertEqual(self.order.total_price, 100.00)
        self.assertTrue(self.order.is_paid)
        self.assertFalse(self.order.is_delivered)
        self.assertIsNotNone(self.order.created)


class OrderItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.product = Product.objects.create(
            user=self.user,  # Provide the user here
            name='Test Product',
            price=50.00
        )
        self.order = Order.objects.create(
            user=self.user,
            payment_method='Credit Card',
            tax_price=10.50,
            shipping_price=5.00,
            total_price=100.00,
            is_paid=True,
            paid_at=timezone.now(),
            is_delivered=False,
            created=timezone.now()
        )
        self.order_item = OrderItem.objects.create(
            order=self.order,
            product=self.product,
            name='Test Product',
            qty=2,
            price=50.00
        )

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.order, self.order)
        self.assertEqual(self.order_item.product, self.product)
        self.assertEqual(self.order_item.name, 'Test Product')
        self.assertEqual(self.order_item.qty, 2)
        self.assertEqual(self.order_item.price, 50.00)


class ShippingAddressModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.order = Order.objects.create(
            user=self.user,
            payment_method='Credit Card',
            tax_price=10.50,
            shipping_price=5.00,
            total_price=100.00,
            is_paid=True,
            paid_at=timezone.now(),
            is_delivered=False,
            created=timezone.now()
        )
        self.shipping_address = ShippingAddress.objects.create(
            order=self.order,
            address='123 Test St',
            city='Test City',
            postal_code='12345',
            country='Test Country'
        )

    def test_shipping_address_creation(self):
        self.assertEqual(self.shipping_address.order, self.order)
        self.assertEqual(self.shipping_address.address, '123 Test St')
        self.assertEqual(self.shipping_address.city, 'Test City')
        self.assertEqual(self.shipping_address.postal_code, '12345')
        self.assertEqual(self.shipping_address.country, 'Test Country')
