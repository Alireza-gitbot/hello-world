from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_GET
from django.views.generic import ListView, FormView

from shipping.forms import ShippingAddressForm
from shipping.models import ShippingAddress


# Create your views here.

@login_required
@require_GET
def address_list(request):
    queryset = ShippingAddress.objects.filter(user=request.user)
    return render(request, 'shipping/list.html', {'queryset': queryset})


class CustomUserListView(ListView):
    # model = ShippingAddress

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)


class AddressListView(CustomUserListView):
    model = ShippingAddress
    #    template_name = 'shipping/list.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=object_list, **kwargs)
        context['extra_data'] = self.get_queryset().count()
        return context


#    @method_decorator(login_required)
#    def get(self, request):
#        queryset = ShippingAddress.objects.filter(user=request.user)
#        return render(request, 'shipping/list.html', {'queryset': queryset})


@login_required
@require_http_methods(request_method_list=['GET', 'POST'])
def address_create(request):
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('address-list')
    else:
        form = ShippingAddressForm()
    return render(request, 'shipping/create.html', {'form': form})


class AddressCreateView(FormView):
    form_class = ShippingAddressForm
    template_name = 'shipping/create.html'
    # success_url = '/shipping/list/'
    success_url = reverse_lazy('address-list')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)
