from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import messages

from .forms import ContactForm
from .models import Services, Employee, Features


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Services.objects.order_by('?').all()
        context['employees'] = Employee.objects.order_by('name').all()
        context['features'] = Features.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email sent successfully')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Error sent email')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)