from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import ReviewForm
from profiles.models import UserProfile
from django.contrib.auth.models import User

from django.db.models import Q, Avg


def reviews(request):
    """ A view to show all customer reviews """

    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/reviews.html', context)


def review_form(request):
    """ A view to load review form """

    review_form = ReviewForm()

    context = {
        "review_form": review_form,
    }

    return render(request, 'reviews/review_form.html', context)


def submit_review(request):
    """ A view to submit review form """

    review_form = ReviewForm(data=request.POST)
    author = request.user

    if review_form.is_valid():
        review_form.instance.review_author = author
        review_form.instance.review_text = request.POST.get("review_text")
        review_form.instance.review_rating = request.POST.get("review_rating")

        review_form.save()

    return render(request, 'reviews/reviews.html')
