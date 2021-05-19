from django.shortcuts import render, redirect
from .forms import TopBackForm
from django.views.generic import View

def contact(request):
    return render(request, 'index.html')

class TopBackView(View):
    def post(self, request):
        form = TopBackForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("/")