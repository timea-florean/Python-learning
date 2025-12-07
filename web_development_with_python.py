#introduction to Web Frameworks
#flask tutorial
#pip install flask

#a simple Flask Application
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello, Flask!'
if __name__ == '__main__':
    app.run(debug=True)

#Django Tutorial
#pip install Django

#starting a Django Project
#django-admin startproject myproject
#cd myproject

#running Django's Development Server
#python manage.py runserver

#creating a simple view
#from django.http import HttpResponse
#def home(request):
#    return HttpResponse("Hello, Django!")

#from django.urls import path
#from .views import home # Import the view
#urlpatterns = [
 #   path('', home, name='home'), # Connects the URL to the view
#]