from models import Category, Product

# Create a new product with ID 1 (or let Django auto-generate the ID)
product = Product.objects.create(
    name="Test Product",
    price=100.00,
    category=Category.objects.first(),  # assuming you have categories
    description="This is a test product.",
    stock_out=False,
    sales_price=80.00,
)

# Check if it was created
print(product.id)  # Should print the ID of the created product
