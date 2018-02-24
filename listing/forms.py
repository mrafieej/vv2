from django import forms
import datetime
from .models import Listing



class ListingForm(forms.ModelForm):
    title = forms.CharField(max_length=80)
    location = forms.ChoiceField(choices=[(x, x) for x in ['SF Bay Area', 'Hawaii', 'Lake Tahoe']])
    description = forms.CharField(widget=forms.Textarea)
    bedrooms = forms.ChoiceField(choices=[(x, x) for x in range(0, 9)])
    bathrooms = forms.ChoiceField(choices=[(x, x) for x in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7]])
    capacity = forms.IntegerField(label='Sleeps')
    square_footage = forms.IntegerField(label='Sq. Ft.')
    street = forms.CharField(max_length=120)
    city = forms.CharField(max_length=80)
    zip_code = forms.IntegerField(label='Zip Code')
    cats_ok = forms.BooleanField(required=False, label='Cats Ok')
    dogs_ok = forms.BooleanField(required=False, label='Dogs Ok')
    smoking_ok = forms.BooleanField(required=False, label='Smoking Ok')
    availability_from = forms.DateField(initial=datetime.date.today, label='Available From')
    availability_to = forms.DateField(initial=datetime.date.today() + datetime.timedelta(days=30), label='Available Until')
    # points_per_night = forms.IntegerField(label='Points/Night')
    # deposit = forms.IntegerField(label='Security Deposit')
    image_1 = forms.ImageField(required=True)
    image_2 = forms.ImageField(required=True)
    image_3 = forms.ImageField(required=True)
    image_4 = forms.ImageField(required=True)
    image_5 = forms.ImageField(required=True)
    # image_6 = forms.ImageField(required=False)
    # image_7 = forms.ImageField(required=False)
    # image_8 = forms.ImageField(required=False)
    # image_9 = forms.ImageField(required=False)
    # image_10 = forms.ImageField(required=False)
    required_css_class = 'required'

    class Meta:
        model = Listing
        fields = ['title', 'location', 'description', 'bedrooms', 'bathrooms',
                  'capacity', 'square_footage', 'street', 'city', 'zip_code',
                  'cats_ok','dogs_ok', 'smoking_ok', 'availability_from', 'availability_to',
                  'image_1', 'image_2', 'image_3', 'image_4',
                  'image_5']





# class ListingForm(forms.Form):
#     title = forms.CharField(max_length=80)
#     location = forms.ChoiceField(choices=[(x, x) for x in ['SF Bay Area', 'Hawaii', 'Lake Tahoe']])
#     description = forms.CharField(widget=forms.Textarea)
#     bedrooms = forms.ChoiceField(choices=[(x, x) for x in range(0, 9)])
#     bathrooms = forms.ChoiceField(choices=[(x, x) for x in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7]])
#     capacity = forms.IntegerField(label='Sleeps')
#     square_footage = forms.IntegerField(label='Sq. Ft.')
#     street = forms.CharField(max_length=120)
#     city = forms.CharField(max_length=80)
#     zip_code = forms.IntegerField(label='Zip Code')
#     cats_ok = forms.BooleanField(required=False, label='Cats Ok')
#     dogs_ok = forms.BooleanField(required=False, label='Dogs Ok')
#     smoking_ok = forms.BooleanField(required=False, label='Smoking Ok')
#     availability_from = forms.DateField(initial=datetime.date.today, label='Available From')
#     availability_to = forms.DateField(initial=datetime.date.today() + datetime.timedelta(days=30), label='Available Until')
#     points_per_night = forms.IntegerField(label='Points/Night')
#     deposit = forms.IntegerField(label='Security Deposit')
#     image_1 = forms.ImageField(required=True)
#     image_2 = forms.ImageField(required=False)
#     image_3 = forms.ImageField(required=False)
#     image_4 = forms.ImageField(required=False)
#     image_5 = forms.ImageField(required=False)
#     required_css_class = 'required'
#     # CHOICES = [('select1', 'Cats OK'),
#     #            ('select2', 'Dogs OK')]
#     # pets = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())


#
# class ListingForm(forms.ModelForm):
#     title = forms.CharField(max_length=80)
#     location = forms.ChoiceField(choices=[(x, x) for x in ['SF Bay Area', 'Hawaii', 'Lake Tahoe']])
#     description = forms.CharField(widget=forms.Textarea)
#     bedrooms = forms.ChoiceField(choices=[(x, x) for x in range(0, 9)])
#     bathrooms = forms.ChoiceField(choices=[(x, x) for x in [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 5, 6, 7]])
#     capacity = forms.IntegerField(label='Sleeps')
#     square_footage = forms.IntegerField(label='Sq. Ft.')
#     street = forms.CharField(max_length=120)
#     city = forms.CharField(max_length=80)
#     zip_code = forms.IntegerField(label='Zip Code')
#     cats_ok = forms.BooleanField(required=False, label='Cats Ok')
#     dogs_ok = forms.BooleanField(required=False, label='Dogs Ok')
#     smoking_ok = forms.BooleanField(required=False, label='Smoking Ok')
#     availability_from = forms.DateField(initial=datetime.date.today, label='Available From')
#     availability_to = forms.DateField(initial=datetime.date.today() + datetime.timedelta(days=30), label='Available Until')
#     points_per_night = forms.IntegerField(label='Points/Night')
#     deposit = forms.IntegerField(label='Security Deposit')
#     image_1 = forms.ImageField(required=True)
#     image_2 = forms.ImageField(required=False)
#     image_3 = forms.ImageField(required=False)
#     image_4 = forms.ImageField(required=False)
#     image_5 = forms.ImageField(required=False)
#     required_css_class = 'required'
#     # CHOICES = [('select1', 'Cats OK'),
#     #            ('select2', 'Dogs OK')]
#     # pets = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
#
#     class Meta:
#         model = Listing
#         fields = []