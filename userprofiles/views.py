from django.shortcuts import render
from .models import UserProfile
from listing.models import Listing
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from listing.forms import ListingForm
from .forms import UserForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
import datetime
from django.core.urlresolvers import reverse_lazy
from django.template import RequestContext
from uuid import UUID

def logout_user(request):
    logout(request)
    request.session['current_member_id'] = ''
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'userprofiles/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # albums = Album.objects.filter(user=request.user)
                listings = Listing.objects.order_by('-pub_date')
                request.session['current_member_id'] = user.user_profile.id.hex
                return render(request, 'listing/home.html', {'listings': listings, 'loggedin': True})
            else:
                return render(request, 'userprofiles/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'userprofiles/login.html', {'error_message': 'Invalid login'})
    return render(request, 'userprofiles/login.html')


def register(request):
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user_profile = form.save(commit=False)
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.create_user(username=email,
                                        email=email,
                                        password=password)
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                user_profile = UserProfile(user=user, email=email, password=password,
                                           firstname=form.cleaned_data['firstname'],
                                           lastname=form.cleaned_data['lastname'],
                                           location=form.cleaned_data['location'],
                                           occupation=form.cleaned_data['occupation'],
                                           about=form.cleaned_data['about'],
                                           profile_pic=request.FILES['profile_pic'],
                                           points=0,
                                           last_logged=datetime.datetime.now(),
                                           joined=datetime.datetime.now())
                user_profile.save()
                # albums = Album.objects.filter(user=request.user)
                listings = Listing.objects.order_by('-pub_date')
                request.session['current_member_id'] = user.user_profile.id.hex
                return render(request, 'listing/home.html', {'listings': listings, 'loggedin': True})
    context = {
        "form": form,
    }
    return render(request, 'userprofiles/register.html', context)


# class RegisterView(FormView):
#     form_class = UserForm
#     template_name = 'userprofiles/edit_profile.html'
#     success_url = '/0'
#     title = 'Create an account:'
#
#     def form_valid(self, form):
#         email = form.cleaned_data['email']
#         password = form.cleaned_data['password']
#         user = User.objects.create_user(username=email,
#                                         email=email,
#                                         password=password)
#         user.save()
#         user = authenticate(username=email, password=password)
#         form.instance.user = user
#         form.instance.points = 0
#         form.instance.last_logged = datetime.datetime.now()
#         form.save()
#         self.request.session['current_member_id'] = ''
#         return super(RegisterView, self).form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super(RegisterView, self).get_context_data(**kwargs)
#         context['loggedin'] = True
#         return context


class UserProfileView(generic.DetailView):
    model = UserProfile
    template_name = 'userprofiles/profile_page.html'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['loggedin'] = True
        context['user_pk'] = self.kwargs['pk']
        context['is_own_profile'] = self.request.user.pk == UserProfile.objects.get(pk=self.kwargs['pk']).user.pk
        return context


class EditUserProfileView(UpdateView):
    form_class = UserForm
    template_name = 'userprofiles/edit_profile.html'
    # success_url = '/user/0' #reverse_lazy('user_profile')
    title = 'Edit your profile:'

    def get_context_data(self, **kwargs):
        context = super(EditUserProfileView, self).get_context_data(**kwargs)
        context['loggedin'] = True
        return context

    def get_success_url(self):
        return '/user/' + self.kwargs.get("pk", None)

    def get_queryset(self):
        return UserProfile.objects.filter(pk=self.kwargs.get("pk", None))

