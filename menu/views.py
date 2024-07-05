from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReservationForm, DishForm
from .models import Reservation, Dish

@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST, user=request.user)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, "Reservation successfully created!")
            return redirect('reservation_list')  # Redirect to a page where reservations are listed
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = ReservationForm(user=request.user)
    return render(request, 'create_reservation.html', {'form': form})

@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservation_list.html', {'reservations': reservations})

@login_required
def reservation_delete(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    
    if request.user != reservation.user:
        return redirect('home')

    if request.method == 'POST':
        reservation.delete()
        return redirect('reservation_list')
    
    context = {
        'reservation': reservation
    }
    return render(request, 'reservation_delete.html', context)


def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = DishForm()
    return render(request, 'add_dish.html', {'form': form})

def dish_detail(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    return render(request, 'dish_detail.html', {'dish': dish})


def dish_delete(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    dish.delete()
    return redirect('menu')

def home(request):
    form = ReservationForm(user=request.user if request.user.is_authenticated else None)
    return render(request, 'home.html', {'form': form})

def menu(request):
    dishes = Dish.objects.all()
    return render(request,'menu.html', {'dishes': dishes})

def main_menu(request):
    return render(request,'main menu.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')



