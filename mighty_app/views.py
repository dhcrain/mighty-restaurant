from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.models import User
from mighty_app.models import Profile, MenuItem, Order, OrderLine
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView
from extra_views.generic import GenericInlineFormSet
from mighty_app.forms import ProfileForm, MenuItemForm
from django.db.models import Q


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_queryset(self):
        return Order.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_item'] = MenuItem.objects.all()
        context['create_menu_item_form'] = MenuItemForm
        context['order_list'] = Order.objects.filter(server=self.request.user).filter(Q(is_paid=False) | Q(is_complete=False))
        if self.request.user.is_authenticated():
            context["profile"] = Profile.objects.get(user=self.request.user)
            context["profile_form"] = ProfileForm
        else:
            context["login_form"] = AuthenticationForm()
        return context


    # add login form
    # if loged in, show if server: add order/owner: menuitem/cook: view orders

class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'profile.html'
    # model = Profile
    fields = ['job']
    success_url = reverse_lazy("index_view")


    def get_object(self, queryset=None):
        return self.request.user.profile

class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("login")


# https://github.com/AndrewIngram/django-extra-views
class OrderLineInline(InlineFormSet):
    model = OrderLine
    extra = 5
    fields = ['quantity', 'order_menu_item']


class OrderCreateView(LoginRequiredMixin, CreateWithInlinesView):
    model = Order
    inlines = [OrderLineInline]
    fields = ['customer_name', 'note', 'is_complete', 'is_paid']
    template_name = 'mighty_app/order_form.html'
    success_url = reverse_lazy("order_create_view")

    def forms_valid(self, form, inlines):
        """
        If the form and formsets are valid, save the associated models.
        """
        order = form.save(commit=False)
        order.server = self.request.user
        self.object = form.save()
        for formset in inlines:
            formset.save()
        return super().forms_valid(form, inlines)


class OrderDetailView(LoginRequiredMixin, UpdateWithInlinesView):
    model = Order
    inlines = [OrderLineInline]
    fields = ['customer_name', 'note', 'is_complete', 'is_paid']
    template_name = 'mighty_app/order_detail.html'
    success_url = reverse_lazy("order_list_view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['object'] = Order.objects.get(id=pk)
        return context


class OrderListView(LoginRequiredMixin, ListView):
    model = Order


class MeunItemCreateView(LoginRequiredMixin, CreateView):
    model = MenuItem
    fields = ['title', 'description', 'price']
    success_url = reverse_lazy("index_view")

    def form_valid(self, form):
        menu_item = form.save(commit=False)
        menu_item.created_by = self.request.user
        return super().form_valid(form)

class MenuItemListView(LoginRequiredMixin, ListView):
    model = MenuItem

class MenuUpdateView(LoginRequiredMixin, UpdateView):
    model = MenuItem
    fields = ['id', 'title', 'description', 'price']
    success_url = reverse_lazy("index_view")
