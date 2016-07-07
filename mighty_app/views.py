from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.models import User
from mighty_app.models import Profile, MenuItem, Order
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


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
