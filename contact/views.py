from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from django.contrib import messages
from .forms import ContactUsForm


def contact_us(request):

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Your message has been sent!')
            return HttpResponseRedirect('/contact?submitted=True')

        else:
            form = ContactUsForm()
            messages.warning(request, 'Message not sent. Please try again.')

    else:
        form = ContactUsForm()
        if 'submitted' in request.GET:
            form = ContactUsForm()

    form = ContactUsForm()
    template = 'contact/contactus.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
