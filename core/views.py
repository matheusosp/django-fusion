from django.views.generic import TemplateView
from .models import Services, Employee, Features


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Services.objects.order_by('?').all()
        context['employees'] = Employee.objects.order_by('name').all()
        context['features'] = Features.objects.all()
        return context
