from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .models import Contact
from .forms import ContactForm


def contact(request):
    """ A view to return and submit contact form """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, 'Thank You! Your message \
            has been sent. We will respond as soon as we can.')

            return redirect('home')

        else:
            messages.error(request, 'Failed to send message. \
                Please try sending your message again.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
