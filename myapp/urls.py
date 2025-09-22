from django.urls import path
from . import views
from .views import demo_class_view  
from . import views
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('education/',views.education,name='education'),
     path('donation/', views.donation_view, name='donation'),
    path('food/',views.food,name='food'),
    path('oldage1/',views.oldage1,name='oldage1'),
    path('admin/',views.admin,name='admin'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('demo/', demo_class_view, name='demo_classes'),
    path('sponsor/', views.sponsor, name='sponsor'),  # ✅ correct
    path('sponsor/child/<int:child_id>/', views.sponsor_child, name='sponsor_child'),  # for processing the form
    path('sponsor/general/', views.sponsor_child, name='sponsor_general'),
    path('suport/', views.suport, name='suport'),  # assuming typo here too
    path('sponsor/thank-you/', views.sponsor_thank_you, name='sponsor_thank_you'),
    path('donation/', views.donation_view, name='donation'),
    path('donation', views.donation_view, name='donation'),

   
   
    path('gallery/infrastructure/', views.infrastructure_gallery, name='infrastructure_gallery'),
    path('gallery/children/', views.children_gallery, name='children_gallery'),
    path('gallery/donations/', views.donations_gallery, name='donations_gallery'),
    path('gallery/oldage/', views.oldage_gallery, name='oldage_gallery'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/chart-data/', views.chart_data, name='chart_data'),

    path('children/',views.children,name='children'),
    path('oldage/', views.oldage, name='oldage'),
    
    path('submit_food/', views.submit_food, name='submit_food'),
    path('', views.meal_form_view, name='meal_donation_form'),
    path('payment_success/', views.payment_success, name='payment_success'), 
    

]

