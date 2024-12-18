from app import create_app
from models import db, user_datastore, Category, Product, ShoppingCart, Order, OrderItem
app, _, _ = create_app()

with app.app_context():
    db.create_all()

    # Get users
    admin_user = user_datastore.find_user(email='a@a.com')
    manager_user = user_datastore.find_user(email='m@a.com')
    customer_user = user_datastore.find_user(email='c@a.com')

    # Create categories
    category1 = Category(name='Fruits', description='Fresh Fruits', status=True, created_by=admin_user.id)
    category2 = Category(name='Vegetables', description='Green Vegetables', status=True, created_by=admin_user.id)
    db.session.add(category1)
    db.session.add(category2)
    db.session.commit()
    print("Created categories")

    # Create products
    product1 = Product(name='Apple', description='Fresh Red Apples', price=100.0, stock=50, category_id=category1.id, created_by=manager_user.id)
    product2 = Product(name='Banana', description='Ripe Yellow Bananas', price=50.0, stock=100, category_id=category1.id, created_by=manager_user.id)
    product3 = Product(name='Carrot', description='Organic Carrots', price=30.0, stock=200, category_id=category2.id, created_by=manager_user.id)
    product4 = Product(name='Spinach', description='Fresh Spinach', price=25.0, stock=150, category_id=category2.id, created_by=manager_user.id)
    db.session.add(product1)
    db.session.add(product2)
    db.session.add(product3)
    db.session.add(product4)
    db.session.commit()
    print("Created products")

    # Create shopping cart for customer
    cart_item1 = ShoppingCart(user_id=customer_user.id, product_id=product1.id, quantity=2, total_price=200.0)
    cart_item2 = ShoppingCart(user_id=customer_user.id, product_id=product3.id, quantity=1, total_price=30.0)
    db.session.add(cart_item1)
    db.session.add(cart_item2)
    db.session.commit()
    print("Created shopping cart items")

    # Create order for customer
    order = Order(user_id=customer_user.id, total_amount=230.0, status='Completed')
    db.session.add(order)
    db.session.commit()
    print("Created order")

    # Create order items
    order_item1 = OrderItem(order_id=order.id, product_id=product1.id, quantity=2, product_price=100.0)
    order_item2 = OrderItem(order_id=order.id, product_id=product3.id, quantity=1, product_price=30.0)
    db.session.add(order_item1)
    db.session.add(order_item2)
    db.session.commit()
    print("Created order items")

    print("Initialization complete")