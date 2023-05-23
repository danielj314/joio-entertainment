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
        return redirect(reverse('reviews'))

    else:
        messages.error(request, 'Failed to add review. \
            Please try adding your review again.')

    return render(request, 'reviews/review_form.html')


@login_required
def edit_review(request, review_id):
    """ Edit a product review """

    review = get_object_or_404(Review, id=review_id)

    # Allow superuser or author of review to edit
    if not (request.user.is_superuser or review.review_author == request.user):
        messages.error(request, 'Sorry, you are not authorized \
            to delete this review.')
        return redirect(reverse('reviews'))

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated review!')
            return redirect(reverse('reviews'))
        else:
            messages.error(request, 'Failed to update review. \
                Ensure form is valid.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, f'You are editing your review')

    template = 'reviews/edit_review.html'
    context = {
        'form': form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, review_id):
    """ Delete a review """
    review = get_object_or_404(Review, id=review_id)

    # Allow superuser or author of review to delete
    if not (request.user.is_superuser or review.review_author == request.user):
        messages.error(request, 'Sorry, you are not authorized \
            to delete this review.')
        return redirect(reverse('reviews'))

    review.delete()

    messages.success(request, f'Review has been deleted!')

    return redirect(reverse('reviews'))
