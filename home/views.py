from django.shortcuts import render
from reviews.models import Review
import random


def index(request):
    """ A view to return the index page """
    reviews = list(Review.objects.all())
    random_reviews = random.sample(reviews, k=3)

    context = {
        "random_reviews": random_reviews,
    }

    return render(request, 'home/index.html', context)
