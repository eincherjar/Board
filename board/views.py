from django.views import generic
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from .models import Notice
from .forms import UserForm


class BoardIndexView(generic.ListView):
    template_name = 'notice_index.html'
    context_object_name = 'all_notices'

    def get_queryset(self):
        return Notice.objects.all().order_by('-id')


class BoardDetailView(generic.DetailView):
    model = Notice
    template_name = 'notice_detail.html'
    
class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'
    
#    display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    
#    preocess form data
    def post(self, request):
        form = self.form_class(request.POST)
        
        if form.is_valid():
            
            user = form.save(commit=False)
            
#            cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
#            return User obj if correct
            user = authenticate(username=username, password=password)
    
            if user is not None:
            
                if user.is_active:
                    login(request, user)
                    return redirect('board:index')
                
        return render(request, self.template_name, {'form': form})