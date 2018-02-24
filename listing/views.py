from django.shortcuts import render, get_object_or_404
from .models import Listing
from .forms import ListingForm
import datetime
from userprofiles.models import UserProfile
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.http import HttpResponseRedirect


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def home(request, filter_id):
    loggedin = False
    if request.user.is_authenticated():
        loggedin = True
    btn1_background_color = '#FFFFFF'
    btn2_background_color = '#FFFFFF'
    btn3_background_color = '#FFFFFF'
    btn4_background_color = '#FFFFFF'
    dark_btn_color_when_active = '#b3b3cc'
    if filter_id == '1':
        listings = Listing.objects.filter(location='Lake Tahoe')
        btn1_background_color = dark_btn_color_when_active
    elif filter_id == '2':
        listings = Listing.objects.filter(location='Hawaii')
        btn2_background_color = dark_btn_color_when_active
    elif filter_id == '3':
        listings = Listing.objects.filter(location='SF Bay Area')
        btn3_background_color = dark_btn_color_when_active
    elif filter_id == '0':
        listings = Listing.objects.order_by('-pub_date')
        btn4_background_color = dark_btn_color_when_active
    context = {'listings': listings, 'loggedin': loggedin,
               'btn1_background_color': btn1_background_color,
               'btn2_background_color': btn2_background_color,
               'btn3_background_color': btn3_background_color,
               'btn4_background_color': btn4_background_color}
    if request.user.is_authenticated():
        request.session['current_member_id'] = request.user.user_profile.id.hex
    else:
        request.session['current_member_id'] = ''
    return render(request, 'listing/home.html', context)


def listing_detail(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    loggedin = False
    posted_by_current_user = False
    if request.user.is_authenticated():
        loggedin = True
        posted_by_current_user = listing.author.id.hex == request.user.user_profile.id.hex
    if request.user.is_authenticated():
        request.session['current_member_id'] = request.user.user_profile.id.hex
    else:
        request.session['current_member_id'] = ''

    context = {
        'listing': listing,
        'loggedin': loggedin,
        'listing_id': listing_id,
        'posted_by_current_user': posted_by_current_user
    }
    return render(request, 'listing/listing_detail.html', context)


def create_listing(request):
    if not request.user.is_authenticated():
        return render(request, 'userprofiles/login.html')
    else:
        request.session['current_member_id'] = request.user.user_profile.id.hex
        form = ListingForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            # listing = form.save(commit=False)
            cd = form.cleaned_data
            listing = Listing()
            listing.title = cd['title']
            listing.location = cd['location']
            listing.description = cd['description']
            listing.author = request.user.user_profile
            listing.bedrooms = int(cd['bedrooms'])
            listing.bathrooms = int(cd['bathrooms'])
            listing.square_footage = int(cd['square_footage'])
            listing.capacity = int(cd['capacity'])
            listing.street = cd['street']
            listing.city = cd['city']
            listing.zip_code = int(cd['zip_code'])
            listing.cats_ok = cd['cats_ok']
            listing.dogs_ok = cd['dogs_ok']
            listing.smoking_ok = cd['smoking_ok']
            listing.availability_from = cd['availability_from']
            listing.availability_to = cd['availability_to']
            listing.points_per_night = int(cd['points_per_night'])
            listing.deposit = int(cd['deposit'])
            listing.image_1 = request.FILES['image_1']
            listing.image_2 = request.FILES['image_2']
            listing.image_3 = request.FILES['image_3']
            listing.image_4 = request.FILES['image_4']
            listing.image_5 = request.FILES['image_5']
            listing.image_6 = request.FILES['image_6']
            listing.image_7 = request.FILES['image_7']
            listing.image_8 = request.FILES['image_8']
            listing.image_9 = request.FILES['image_9']
            listing.image_10 = request.FILES['image_10']
            file_type = listing.image_1.url.split('.')[-1]
            file_type = file_type.lower()
            listing.pub_date = datetime.datetime.now()
            # if file_type not in IMAGE_FILE_TYPES:
            #     context = {
            #         'listing': listing,
            #         'form': form,
            #         'error_message': 'Image file must be PNG, JPG, or JPEG',
            #     }
            #     return render(request, 'listing/create_listing.html', context)
            listing.save()
            context = {
                'listing': listing,
                'listing_id': listing.pk.hex,
                'loggedin': True,
                'posted_by_current_user': True
            }
            return render(request, 'listing/listing_detail.html', context)
        else:
            print("Form was not valid")
        context = {
            'form': form,
            'loggedin': True
        }
        return render(request, 'listing/create_listing.html', context)


class EditListingView(UpdateView):
    form_class = ListingForm
    template_name = 'listing/create_listing.html'
    # success_url = '/listing/0' #reverse_lazy('user_profile')

    def get_context_data(self, **kwargs):
        context = super(EditListingView, self).get_context_data(**kwargs)
        context['listing_id'] = self.kwargs['pk']
        context['loggedin'] = True
        return context

    def get_success_url(self):
        return '/listing/' + self.kwargs.get("pk", None)

    def get_queryset(self):
        return Listing.objects.filter(pk=self.kwargs.get("pk", None))


class DeleteListingView(DeleteView):
    model = ListingForm
    success_url = '/0' #reverse_lazy('user_profile')
    items_to_delete = []

    def get_context_data(self, **kwargs):
        context = super(DeleteListingView, self).get_context_data(**kwargs)
        context['loggedin'] = True
        return context

    def get_queryset(self):
        return Listing.objects.filter(pk=self.kwargs.get("pk", None))

    def post(self, request, *args, **kwargs):
        self.items_to_delete = self.request.POST.getlist('itemsToDelete')
        if self.request.POST.get("confirm_delete"):
            # when confirmation page has been displayed and confirm button pressed
            queryset = self.get_queryset()
            queryset.delete()  # deleting on the queryset is more efficient than on the model object
            return HttpResponseRedirect(self.success_url)
        elif self.request.POST.get("cancel"):
            # when confirmation page has been displayed and cancel button pressed
            return HttpResponseRedirect(self.success_url)
        else:
            # when data is coming from the form which lists all items
            return self.get(self, *args, **kwargs)


def beta(request):
    if request.method == "POST":
        if request.POST['pin'] == 'ND18':
            return HttpResponseRedirect('/0')
    return render(request, 'listing/beta_page.html', {})
