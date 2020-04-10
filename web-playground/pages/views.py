from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .forms import PageForm
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.
class PagesListView(ListView):
    model = Page

    pages = get_list_or_404(Page)
    #return render(request, 'pages/pages.html', {'pages':pages})

class PageDetailViews(DetailView):
    model = Page
    
@method_decorator(staff_member_required, name ='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    #fields = ['title','content','order']
    success_url = reverse_lazy('pages:pages')

@method_decorator(staff_member_required, name ='dispatch')
class PageUpdate(UpdateView):
    model = Page
    fields = ['title','content','order']
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) +'?ok'

@method_decorator(staff_member_required, name ='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
