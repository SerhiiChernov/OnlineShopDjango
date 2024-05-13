from django.shortcuts import render
from .models import ClothCategory
from .forms import OrderForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def home(request):
    categories = ClothCategory.objects.filter(is_visible=True)
    form = OrderForm()

    return render(request, 'main.html ', context= {
        'categories': categories,
        'form': form,
    })

def order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your order has been successfully submitted!')
        else:
            messages.error(request, 'Something went wrong!')
        return redirect('home')
    else:
        form = OrderForm()
    return render(request, 'order.html', {'form': form})
