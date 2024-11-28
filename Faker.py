# tests/factories.py
from faker import Faker
import random

fake = Faker()

class ProductFactory:
    @staticmethod
    def create_fake_product():
        return {
            'name': fake.company(),
            'description': fake.text(max_nb_chars=200),
            'price': round(random.uniform(10.99, 999.99), 2),
            'sku': fake.uuid4(),
            'category': fake.word()
        }

# Example usage:
if __name__ == '__main__':
    fake_product = ProductFactory.create_fake_product()
    print(fake_product)
