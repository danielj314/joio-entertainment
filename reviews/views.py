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


@login_required
def submit_review(request):
    """ A view to submit review form """

    review_form = ReviewForm(data=request.POST)
    author = request.user

    if review_form.is_valid():
        review_form.instance.review_author = author
        review_form.instance.review_text = request.POST.get("review_text")
        review_form.instance.review_rating = request.POST.get("review_rating")

        review_form.save()

        messages.success(request, 'Thank You! Your review \
            has been added!')

        return render(request, 'reviews/reviews.html')
    else:
        messages.error(request, 'Oops, something went wrong! \
            Please try adding your review again.')


def submit_review(request):
    """ A view to submit review form """

    review_form = ReviewForm(data=request.POST)
    author = request.user

    if review_form.is_valid():
        review_form.instance.review_author = author
        review_form.instance.review_text = request.POST.get("review_text")
        review_form.instance.review_rating = request.POST.get("review_rating")

        review_form.save()

        messages.success(request, 'Thank You! Your review \
            has been added!')
        return redirect(reverse('reviews'))

    else:
        messages.error(request, 'Failed to add review. \
            Please try adding your review again.')

    return render(request, 'reviews/review_form.html')


@login_required
def delete_review(request, review_id):
    """ Delete a review """
    review = get_object_or_404(Review, id=review_id)

    # Allow superuser or author of review to delete
    if not (request.user.is_superuser or review.review_author == request.user):
        messages.error(request, 'Sorry, you are not authorized to delete this review.')
        return redirect(reverse('reviews'))

    review.delete()

    messages.success(request, f'Review has been deleted!')

    return redirect(reverse('reviews'))
