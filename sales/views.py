from django.shortcuts import render
from django.utils import timezone
from datetime import datetime
from django.urls import reverse_lazy
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, FormView, ListView, CreateView
from django.views.generic.edit import ModelFormMixin, UpdateView, DeleteView
from .forms import NewSaleForm, NewItemForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Menu, Order
from .scale import data_test
import datetime

# Create your views here.

class HomePage(TemplateView):
    template_name = 'home.html'

class Dashboard(LoginRequiredMixin, ListView):
    template_name = 'dashboard.html'
    model = Order
    context_object_name = 'orders'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = context['orders'].filter(user=self.request.user)
        now = datetime.datetime.now()
        start_date = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        total_sum = Order.objects.filter(date__month=now.month).aggregate(total_sum=Sum('total'))['total_sum']
        context['total_sum'] = total_sum or 0
        day_sum = Order.objects.filter(date=now).aggregate(total_sum=Sum('total'))['total_sum']
        context['day_sum'] = day_sum or 0
        context['today'] = now
        month_str = datetime.date(1900, now.month, 1).strftime('%B')
        context['month'] = month_str
        return context


class NewSale(LoginRequiredMixin, CreateView):
    model = Menu
    form_class = NewSaleForm
    template_name = 'pos.html'
    success_url = 'new_sale'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu"] = Menu.objects.all()
        return context
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect('new_sale')

class NewItem(LoginRequiredMixin, FormView):
    form_class = NewItemForm
    template_name = 'new_item.html'
    success_url = 'menu_item_list'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())

class MenuItemList(LoginRequiredMixin, ListView):
    model = Menu
    template_name = 'menu_list.html'
    context_object_name = 'menulist'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menulist'] = context['menulist'].filter(user=self.request.user)
        return context

class OrderView(TemplateView):
    template_name = "order.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["menu_items"] = Menu.objects.all()
        context["orders"] = Order.objects.all()
        context["scale"] = data_test
 
        return context

    def post(self, request, *args, **kwargs):
        menu_item_id = request.POST.get("menu_item_id")
        if menu_item_id:
            menu_item = Menu.objects.get(pk=menu_item_id)
            request.session.setdefault("cart", {})
            cart = request.session["cart"]
            if str(menu_item_id) in cart:
                if "decrease_quantity" in request.POST:
                    if cart[str(menu_item_id)]["quantity"] > 1:
                        cart[str(menu_item_id)]["quantity"] -= 1
                    else:
                        del cart[str(menu_item_id)]
                else:
                    cart[str(menu_item_id)]["quantity"] += 1
                if "delete_item" in request.POST:
                    del cart[str(menu_item_id)]
            else:
                cart[str(menu_item_id)] = {
                    "name": menu_item.name,
                    "price": float(menu_item.price),
                    "quantity": data_test,
                }
            request.session.modified = True

        elif "collect" in request.POST:
            cart = request.session.get("cart", {})
            for menu_item_id, data in cart.items():
                name = data["name"]
                quantity = data["quantity"]
                price = data["price"]
                total_price = price * quantity
                user = request.user
                date = datetime.date.today()
                time = datetime.datetime.now()
                Order.objects.create(
                    user=user,
                    name=name,
                    quantity=quantity,
                    price=float(price),
                    total=float(total_price),
                    date=date,
                    time=time,
                )
            request.session["cart"] = {}
            request.session.modified = True

        return self.get(request, *args, **kwargs)

class TorItemUpdate(UpdateView):
    model = Menu
    fields = ["name", "price"]
    template_name = "update_item_tor.html"
    success_url = reverse_lazy('menu_item_list')
    
class TorItemDelete(DeleteView):
    # specify the model you want to use
    model = Menu
    template_name = "menu_item_list.html"
    success_url = reverse_lazy('menu_item_list')





