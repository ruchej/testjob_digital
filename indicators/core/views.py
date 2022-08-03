from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView

from core.models import Indicator



#@login_required(login_url='/admin/login/?next=/')
#def index(request):
#    template = loader.get_template('core/index.html')
#    context = {}
#    return HttpResponse(template.render(context, request))


class IndexView(ListView):
    model = Indicator
    template_name = 'core/index.html'
    context_object_name = 'indicators'
