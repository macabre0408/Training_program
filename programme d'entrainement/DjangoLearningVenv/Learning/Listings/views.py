from django.http import HttpResponse
from django.shortcuts import render
from Listings.models import Band, Listings
from Listings.forms import contactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect 

def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = contactUsForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["nom"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
        return redirect('email-sent')  # ajoutez cette instruction de retour
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
    # ceci doit être une requête GET, donc créer un formulaire vide
        form = contactUsForm()
    return render(request,
            'listings/contactUs.html',
            {'form': form})

def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/bands_list.html', {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band': band})

def aboutUs(request):
    return render(request, 'listings/aboutUS.html')

def listings_list(request):
    listings = Listings.objects.all()
    return render(request, 'listings/listings_list.html', {'listings': listings})

def listings_detail(request, id):
    listing =Listings.objects.get(id=id)
    return render(request, 'listings/listings_detail.html', {'listing': listing})


def contactUs(request):
    return render(request, 'listings/contactUs.html')

def band_create(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = contactUsForm(request.POST)