from django.shortcuts import render


def about(request):
    """ A view to return the About Us page """

    return render(request, 'about.html')


def contact(request):
    """ A view to return the Contact Us page """

    return render(request, 'contact.html')
