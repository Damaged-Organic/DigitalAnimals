from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Benefit, Feature, Step, Pricing, Contact
from .forms import OrderForm

def index(request):
    benefits = get_list_or_404(Benefit)
    features = get_list_or_404(Feature)
    steps = get_list_or_404(Step)
    pricings = get_list_or_404(Pricing)
    contact = Contact.objects.all()[:1].get()

    return render(request, 'website/index.html', {
        'benefits': benefits,
        'features': features,
        'steps': steps,
        'pricings': pricings,
        'contact': contact
    })


def order(request):
    form = OrderForm()

    return render(request, 'website/order.html', {
        'form': form
    })


def handler400(request):
    return render(request, 'website/errors/400.html', {}, status=400)


def handler403(request):
    return render(request, 'website/errors/403.html', {}, status=403)


def handler404(request):
    return render(request, 'website/errors/404.html', {}, status=404)


def handler500(request):
    return render(request, 'website/errors/500.html', {}, status=500)
