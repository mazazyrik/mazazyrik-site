from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render

from .forms import ContactForm


class IndexView(TemplateView):
    template_name = 'index.html'


class StackView(TemplateView):
    template_name = 'stack.html'


class StoryView(TemplateView):
    template_name = 'story.html'


def contact(request):
    template = 'contact.html'
    form = ContactForm(request.POST or None, files=request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main:index')
        return render(request, template, {'form': form})
    return render(request, template, {'form': form})
