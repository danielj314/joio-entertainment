from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm
from profiles.models import UserProfile
from django.contrib.auth.models import User

from django.db.models import Q, Avg

# Create your views here.


from django.shortcuts import render


def reviews(request):
    """ A view to show all customer reviews """

    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/reviews.html', context)
