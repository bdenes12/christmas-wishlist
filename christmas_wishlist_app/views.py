from django.shortcuts import get_object_or_404, redirect, render

from .forms import GiftForm
from .models import FamilyMember, Gift


def index(request):
    form = GiftForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = GiftForm()

        return redirect('christmas_wishlist_app:index')
    
    family_members = FamilyMember.objects.prefetch_related('gift_set').all() 
    
    context = {
        'form': form,
        'family_members': family_members
    }

    return render(request, "gifts/gift_create.html", context)

def delete_gift(request, id):
    obj = get_object_or_404(Gift, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('christmas_wishlist_app:index')
    context = {
        "object": obj
    }
    return render(request, "gifts/gift_delete.html", context)