from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url')
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    if item_id in bag:
        # If item already in bag, check if quantity exceeds quantity available
        if quantity + bag[item_id] > product.qty_available:
            messages.error(request, f"Sorry, only {product.qty_available} '{product.name}' available on this day.")
            return redirect(redirect_url)
        else:
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        # If item not in bag, add it to the bag after checking that quantity is available
        if quantity > product.qty_available:
            messages.error(request, f"Sorry, only {product.qty_available} '{product.name}' available on this day.")
            return redirect(redirect_url)
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your booking')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    if quantity > product.qty_available:
        messages.error(request, f"Sorry, only {product.qty_available} '{product.name}' available on this day.")
    elif quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your booking')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove the item from the shopping bag """

    try:
        bag = request.session.get('bag', {})
        product = get_object_or_404(Product, pk=item_id)

        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your booking')
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
