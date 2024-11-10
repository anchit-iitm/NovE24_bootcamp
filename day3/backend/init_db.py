# from app import app
# from flask import current_app as app
from models import db, user_datastore
from app import create_app

app, _ = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    '''new_role = Role(name='admin', description='Suepruser') #user_datatore
    db.session.add(new_role) #user_datatore
    db.session.commit()'''
    user_datastore.find_or_create_role(name='admin', description='Suepruser')
    user_datastore.find_or_create_role(name='manager', description='Mid-level user')
    user_datastore.find_or_create_role(name='customer', description='Low-level user')

    db.session.commit()

    admin_user = user_datastore.find_user(email='a@a.com')
    # user_datastore.find_user(id=1)
    if not admin_user:
        # user_datastore.create_user(email="a@a.com", password='a', roles=['admin'])
        new_user = user_datastore.create_user(email="a@a.com", password='a')
        user_datastore.add_role_to_user(new_user, 'admin')
        # user_datastore.add_role_to_user(new_user, 'manager')
        db.session.commit()

    admin_user = user_datastore.find_user(email='m@a.com')
    # user_datastore.find_user(id=1)
    if not admin_user:
        # user_datastore.create_user(email="a@a.com", password='a', roles=['admin'])
        new_user = user_datastore.create_user(email="m@a.com", password='m')
        # user_datastore.add_role_to_user(new_user, 'admin')
        user_datastore.add_role_to_user(new_user, 'manager')
        db.session.commit()

    admin_user = user_datastore.find_user(email='c@a.com')
    # user_datastore.find_user(id=1)
    if not admin_user:
        # user_datastore.create_user(email="a@a.com", password='a', roles=['admin'])
        new_user = user_datastore.create_user(email="c@a.com", password='c')
        user_datastore.add_role_to_user(new_user, 'customer')
        # user_datastore.add_role_to_user(new_user, 'manager')
        db.session.commit()