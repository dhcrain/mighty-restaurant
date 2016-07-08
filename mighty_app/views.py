from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.models import User
from mighty_app.models import Profile, MenuItem, Order, OrderLine
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from mighty_app.forms import OrderForm, OrderLineForm


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    # add login form
    # if loged in, show if server: add order/owner: menuitem/cook: view orders

class ProfileListView(LoginRequiredMixin, ListView):
    template_name = 'profile.html'
    model = Order

class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("login")


class OrderCreateView(CreateView):
    model = Order
    fields = ['customer_name', 'order_items', 'note', 'is_complete', 'is_paid']
    # form_class = OrderForm
    success_url = reverse_lazy("order_list_view")

    def form_valid(self, form):
        order = form.save(commit=False)
        order.server = self.request.user
        return super().form_valid(form)

class OrderListView(ListView):
    model = Order

class OrderDetailView(UpdateView):
    model = Order
    fields = ['customer_name', 'order_items', 'note', 'is_complete', 'is_paid']
    template_name = 'mighty_app/order_detail.html'
    # form_class = OrderForm
    success_url = reverse_lazy("order_list_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['object'] = Order.objects.get(id=pk)
        return context

class MeunItemCreateView(CreateView):
    model = MenuItem
    fields = ['title', 'description', 'price']
    success_url = reverse_lazy("menu_item_list_view")

    def form_valid(self, form):
        menu_item = form.save(commit=False)
        menu_item.created_by = self.request.user
        return super().form_valid(form)

class MenuItemListView(ListView):
    model = MenuItem

class MenuUpdateView(UpdateView):
    model = MenuItem
    fields = ['id', 'title', 'description', 'price']
    success_url = reverse_lazy("menu_item_list_view")
