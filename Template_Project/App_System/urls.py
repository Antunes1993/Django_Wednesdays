from django.urls import path 
from . import views

urlpatterns = [
    # PATH CONVERTERS
    # int numbers
    # str strings 
    # path whole urls /
    # slug hyphen-and_underscores_stuff
    # UUID universally unique identifier


    path('', views.home, name="home"),
    path('<int:year>/<str:month>', views.home_calendar, name="home_calendar"),
    path('maintenances', views.all_maintenances, name="list_maintenances"),
    path('add_equipment', views.add_equipment, name="add_equipment"),
    path('list_equipments', views.all_equipments, name="list_equipments"),
    path('show_equipment/<equipment_id>', views.show_equipment, name='show_equipment'),
    path('search_equipment', views.search_equipment, name='search_equipment'),
    path('update_equipment/<equipment_id>', views.update_equipment, name='update_equipment'),
    path('equipment_text', views.equipment_text, name='equipment_text'),
    path('equipment_csv', views.equipment_csv, name='equipment_csv'),
    path('equipment_pdf', views.equipment_pdf, name='equipment_pdf'),
    path('json_response', views.json_response, name='json_response'),
]