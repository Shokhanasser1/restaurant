from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReservationForm, DishForm, OrderForm
from .models import Reservation, Dish, Order, Category
from django.db.models import Count



@login_required
def order_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    order = None
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.dish = dish
            order.user = request.user
            order.save()
            return redirect('menu')
    else:
        form = OrderForm()
    return render(request, 'order_dish.html', {'dish': dish, 'form': form})


@login_required
def user_orders_list(request):
        orders = Order.objects.filter(user=request.user)
        return render(request, 'orders.html', {'orders': orders})


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

@login_required
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


@login_required
def dish_delete(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    
    if request.method == 'POST':
        if 'confirm_delete' in request.POST:
            dish.delete()
            messages.success(request, 'Блюдо успешно удалено.')
            return redirect('menu')
        else:
            return redirect('menu')
    
    return render(request, 'confirm_delete.html', {'dish': dish})


def get_top_dishes_for_all_categories():
    categories = Category.objects.all()
    category_dishes = {}
    for category in categories[:2]:
        top_dishes = Dish.objects.filter(category=category).annotate(order_count=Count('order')).order_by('-order_count')[:3]
        category_dishes[category] = top_dishes
    return category_dishes

def top_dishes_view(request):
    category_dishes = get_top_dishes_for_all_categories()
    context = {
        'category_dishes': category_dishes,
    }
    return render(request, 'top_dishes.html', context)

def full_menu_view(request):
    categories = Category.objects.all()
    dishes = Dish.objects.all()
    category_dishes = {}
    for category in categories:
        all_dishes = Dish.objects.filter(category=category)
        category_dishes[category] = all_dishes
    context = {
        'dishes': dishes,
        'categories': categories,
        'category_dishes': category_dishes,
    }
    return render(request, 'full_menu.html', context)

def home(request):
    form = ReservationForm(user=request.user if request.user.is_authenticated else None)
    top_dishes = get_top_dishes_for_all_categories()
    return render(request, 'home.html', {'form': form, 'top_dishes': top_dishes})

    
def menu(request):
    categories = Category.objects.all()
    dishes = Dish.objects.all()
    return render(request,'menu.html', {'dishes': dishes, 'categories': categories})

def main_menu(request):
    return render(request,'main menu.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')



