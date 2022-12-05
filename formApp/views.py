from django.shortcuts import render, HttpResponse
from .forms import OrderForm


# Create your views here.
def index(request):
    return render(request, 'index.html')


def appointment(request):
    name = request.POST.get("name")
    email = request.POST.get('email')
    phone_number = request.POST.get('phone')
    select = request.POST.get('select')
    description = request.POST.get('description')
    return HttpResponse(f"""<p>Name: {name}</p>
                                <p>Email: {email}</p>
                                <p>Phone: {phone_number}</p>
                                <p>Select service: {select}</p>
                                <p>Description: {description}<p>
    """)


def check_order(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Ivan')
        surname = request.POST.get('surname', 'Ivanov')
        email = request.POST.get('email', 'Ivanovich')
        country = request.POST.get('country', 'Russia')
        city = request.POST.get('city', 'Moscow')
        street = request.POST.get('street', 'Arbat')
        number_of_house = request.POST.get('number_of_house', '1')
        flat = request.POST.get('flat', '1')
        return HttpResponse(f"""<p>Name: {name}</p>
                                <p>Surname: {surname}</p>
                                <p>Email: {email}</p>
                                <p>Country: {country}</p>
                                <p>City: {city}</p>
                                <p>Street: {street}</p>
                                <p>House number: {number_of_house}</p>
                                <p>Number of flat: {flat}</p>
                                """)
    else:
        order_form = OrderForm()
        return render(request, 'order.html', {'form': order_form})