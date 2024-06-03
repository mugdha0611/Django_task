import os
import sys
import django
import random
from faker import Faker

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom.settings')

# Print current working directory and environment variable for debugging
print("Current Working Directory:", os.getcwd())
print("DJANGO_SETTINGS_MODULE:", os.environ.get('DJANGO_SETTINGS_MODULE'))

# Setup Django
django.setup()
from products.models import Product
fake = Faker()

categories = {
    "Clothing": ["Men's Shirts", "Women's Dresses", "Shoes", "Accessories"],
    "Electronics": ["Laptops", "Smartphones", "Televisions", "Audio Equipment"],
    "Home & Kitchen": ["Furniture", "Appliances", "Kitchen Utensils", "Decor"]
}

shapes = ['square', 'rectangular', 'circular', 'triangular']
locations = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']

def generate_products(num_products):
    for product_id in range(1, num_products + 1):
        category_name = random.choice(list(categories.keys()))
        subcategory = random.choice(categories[category_name])
        shape = random.choice(shapes)
        size = round(random.uniform(1, 10), 2)
        location = random.choice(locations)
        price = round(random.uniform(10, 1000), 2)
        product_name = f"{category_name} {subcategory} by {fake.company()}"

        product = Product(
            id=product_id,
            name=product_name,
            shape=shape,
            size=size,
            location=location,
            price=price,
            category=category_name
        )
        product.save()

# Generate 1,000,000 products
generate_products(100)