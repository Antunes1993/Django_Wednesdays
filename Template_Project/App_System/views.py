from cgitb import text
import csv
import calendar 
import requests
from datetime import datetime
from calendar import HTMLCalendar
from django.shortcuts import render, redirect
from .models import Maintenance, Equipment
from .forms import EquipmentForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from requests.exceptions import RequestException

import io 
from django.http import FileResponse
from reportlab.pdfgen import canvas 
from reportlab.lib.units import inch 
from reportlab.lib.pagesizes import letter 

#Import pagination stuff
from django.core.paginator import Paginator



# Generate text file equipment list
def equipment_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=equipments.txt'  
    equipment_list = Equipment.objects.all()    
       
    lines = []

    for item in equipment_list:
        lines.append(f'{item}\n{item.type}\n{item.address}\n\n')
        

    #Write to a text file 
    response.writelines(lines)
    return response 

# Generate csv file equipment list
def equipment_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=equipments.csv'  
    
    # Create a csv writer 
    writer = csv.writer(response)
    
    equipment_list = Equipment.objects.all()    

    #  Add columns to the csv file 
    writer.writerow(['Tag','Address','Type'])

    for item in equipment_list:
        writer.writerow([item.tag,item.type,item.address])

    return response  

# Genereate PDF file equipment list 
def equipment_pdf(request):
    # Create bytestream buffer 
    buf = io.BytesIO()

    # Create a canvas 
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0) 

    # Create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    # Add some lines of text 
    lines = []
    equipment_list = Equipment.objects.all()    

    for item in equipment_list:
        lines.append(f'{item}')
        lines.append(f'{item.type}')
        lines.append(f'{item.address}')
        lines.append('=========================================')

        
    for line in lines:
        textob.textLine(line)


    # Finish Up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    # Return something
    return FileResponse(buf, as_attachment=True, filename='equipment_list.pdf')

# Create your views here.
def home(request):
    title = "COMOS PANEL"
    return render(request, 'maintenances/home.html', {
        "title": title 
    })

def home_calendar(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    title = "Event Calendar"

    #Convert month from name to number 
    month = month.capitalize()
    month_number = int(list(calendar.month_name).index(month))

    #Create a calendar 
    new_calendar = HTMLCalendar().formatmonth(
        year, 
        month_number)

    #Get current year 
    now = datetime.now() 
    current_year = now.year

    #Get current time 
    #Am / Pm format 
    #%I:%M:%S %p  - The %p is for am / pm
    #Full clock format
    #%H:%M:%S'

    time = now.strftime('%I:%M %p')   

    return render(request, 'maintenances/home.html', {
        "title": title,
        "year": year,
        "month": month,
        "month_number": month_number,
        "new_calendar": new_calendar,
        "current_year": current_year,
        "time": time,
    })    

def all_maintenances(request):
    maintenance_list = Maintenance.objects.all()
    return render(request, 'maintenances/events.html', {
        "maintenance_list": maintenance_list,
    })

def add_equipment(request):
    submitted = False
    if request.method == "POST":
        form = EquipmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = EquipmentForm    
        if 'submitted' in request.GET:
            submitted = True 

    return render(request, 'maintenances/add_venue.html', {'form':form, 'submitted':submitted})

def all_equipments(request):
    #equipment_list = Equipment.objects.all().order_by('?')
    equipment_list = Equipment.objects.all()

    #Set up the pagination 
    p = Paginator(Equipment.objects.all(), 2)
    page = request.GET.get('page')
    equipments = p.get_page(page)



    return render(request, 'maintenances/equipment_list.html', {
        "equipment_list": equipment_list,
        "equipments": equipments
    })

def show_equipment(request, equipment_id):
    equipment = Equipment.objects.get(pk=equipment_id)
    return render(request, 'maintenances/show_equipment_data.html', {
    "equipment": equipment,
})

def search_equipment(request):
    if request.method == "POST":
        searched = request.POST['searched']
        equipment_list = Equipment.objects.filter(tag__contains=searched)        

        return render(request, 'maintenances/search_equipment.html', {
            'searched': searched,
            'equipment_list':equipment_list            
        })

    else:
        return render(request, 'maintenances/search_equipment.html', {})
    return render(request, 'maintenances/search_equipment.html')

def update_equipment(request, equipment_id):
    equipment = Equipment.objects.get(pk=equipment_id)    
    form = EquipmentForm(request.POST or None, instance=equipment)
    if form.is_valid():
        form.save()
        return redirect('list_equipments')


    return render(request, 'maintenances/update_equipment.html', {
        'equipment':equipment,
        'form':form
    })

def json_response(request):
    return render(request, 'maintenances/json_response.html')

