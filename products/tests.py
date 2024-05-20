from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Product, Category, Review

User = get_user_model()

class ModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='test@example.com',
            username='testuser',
            first_name='Test',
            last_name='User',
            password='password'
        )
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            user=self.user,
            name='Test Product',
            description='Test Description',
            category=self.category,
            price=10.99,
            countinStock=100
        )

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.first()
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('password'))

    def test_product_creation(self):
        self.assertEqual(Product.objects.count(), 1)
        product = Product.objects.first()
        self.assertEqual(product.name, 'Test Product')
        self.assertEqual(product.user, self.user)
        self.assertEqual(product.category, self.category)
        self.assertEqual(float(product.price), 10.99)
        self.assertEqual(product.countinStock, 100)

    def test_category_creation(self):
        self.assertEqual(Category.objects.count(), 1)
        category = Category.objects.first()
        self.assertEqual(category.name, 'Test Category')

    def test_review_creation(self):
        review = Review.objects.create(
            user=self.user,
            product=self.product,
            name='Test Review',
            rating=4,
            comment='Test Comment'
        )
        self.assertEqual(Review.objects.count(), 1)
        review = Review.objects.first()
        self.assertEqual(review.name, 'Test Review')
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.product, self.product)
        self.assertEqual(review.rating, 4)
        self.assertEqual(review.comment, 'Test Comment')

    def test_slug_generation(self):
        product = Product.objects.create(
            user=self.user,
            name='Test Product 2',
            description='Test Description 2',
            category=self.category,
            price=20.99,
            countinStock=50
        )
        self.assertEqual(product.slug, 'test-product-2')

    def test_user_str_representation(self):
        user = User.objects.create_user(
            email='test2@example.com',
            username='testuser2',
            first_name='Test2',
            last_name='User2',
            password='password'
        )
        self.assertEqual(str(user), 'test2@example.com')

    def test_category_str_representation(self):
        category = Category.objects.create(name='Test Category 2')
        self.assertEqual(str(category), 'Test Category 2')

    def test_product_str_representation(self):
        self.assertEqual(str(self.product), 'Test Product')

    def test_review_str_representation(self):
        review = Review.objects.create(
            user=self.user,
            product=self.product,
            name='Test Review 2',
            rating=5,
            comment='Test Comment 2'
        )
        self.assertEqual(str(review), 'Test Review 2')

    def test_superuser_creation(self):
        superuser = User.objects.create_superuser(
            email='superuser@example.com',
            username='superuser',
            first_name='Super',
            last_name='User',
            password='password'
        )
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)

    # Add more tests as needed
