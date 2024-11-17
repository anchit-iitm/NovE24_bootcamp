from app import celery_app
from models import db, Category, test
from celery_context import flaskContext

@celery_app.task(base=flaskContext)
def celeryIndex():
    print("Hello world from celery")
    return True

@celery_app.task(base=flaskContext)
def plus(a, b):
    from time import sleep
    sleep(10)
    return a + b

@celery_app.task(base=flaskContext)
def dbUpdate():
    new_data = test(string="This is a test with celery", num=100, boolean=True)
    db.session.add(new_data)
    db.session.commit()
    return "Data added successfully", True


@celery_app.task(base=flaskContext)
def dbQuery(a, b):
    idAsArg = a
    category = Category.query.filter_by(id=idAsArg).first()
    print("id", category.id, "name", category.name, "description", category.description)
    if not category:
        return "No category found by that id", False
    return category.serialize(), True


@celery_app.task(base=flaskContext)
def reminder():
    from models import user_datastore
    user = user_datastore.find_user(email='m@a.com')
    if user:
        from flask_mail import Message
        from mailer import mail as mailer
        msg = Message(subject='Reminder', body='This is a reminder', recipients=[user.email])
        mailer.send(msg)
        return "Reminder sent successfully", True
    return "No user found", False

@celery_app.task(base=flaskContext)
def html():
    from models import user_datastore
    user = user_datastore.find_user(email='c@a.com')
    if user:
        from flask_mail import Message
        from mailer import mail as mailer
        msg = Message(subject='Reminder', body='This is a reminder', recipients=[user.email])
        msg.sender='admin@a.com'
        msg.html = '<html><body><h1>Hello, World</h1>'
        msg.html += '<p>This is a test email from Flask-Mail</p>'
        msg.html += f'<a>{user.email}</a></body></html>'
        mailer.send(msg)
        return "Reminder sent successfully", True
    return "No user found", False