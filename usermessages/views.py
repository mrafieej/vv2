from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Message
from listing.models import Listing
from userprofiles.models import UserProfile
import datetime
from django.db.models import Q, F
from django.db.models import Max
from itertools import chain
from django.db.models import Value
from django.db.models.functions import Concat

class InboxView(generic.ListView):
    model = Message
    template_name = 'usermessages/inbox.html'
    messages = []

    def get_queryset(self):
        user_self = self.request.user.user_profile

        messages_sent = Message.objects.filter(Q(sender=user_self)).annotate(other=Max('receiver'))
        messages_received = Message.objects.filter(Q(receiver=user_self)).annotate(other=Max('sender'))
        messages_all = messages_sent | messages_received
        latest_message_set = messages_all.values('listing', 'other').annotate(latest=Max('message_date')).order_by()
        q_statement = Q()
        for msg in latest_message_set:
            q_statement |= (Q(listing__exact=msg['listing']) & Q(other__exact=msg['other']) & Q(message_date=msg['latest']))
        self.messages = messages_all.filter(q_statement).order_by('-message_date')
        return messages_all.filter(q_statement).order_by('-message_date')

    def get_context_data(self, **kwargs):
        context = super(InboxView, self).get_context_data(**kwargs)
        context['loggedin'] = self.request.user.is_authenticated()
        context['user_id_self'] = self.request.user.user_profile.pk.hex
        context['has_unread'] = self.messages.filter(is_read=False)
        return context


def message_detail(request, user_id_other, listing_id):
    user_self = request.user.user_profile
    user_other = get_object_or_404(UserProfile, pk=user_id_other)
    listing = get_object_or_404(Listing, pk=listing_id)
    if request.method == "POST":
        body = request.POST['body']
        message = Message(listing=listing,
                          sender=user_self,
                          receiver=user_other,
                          body=body,
                          message_date=datetime.datetime.now(),
                          is_read=False)
        message.save()

    messages = Message.objects.filter(Q(listing=listing, sender=user_self, receiver=user_other)
                                      | Q(listing=listing, sender=user_other, receiver=user_self)).order_by('-message_date')

    context = {
        'user_self': user_self,
        'user_other': user_other,
        'listing': listing,
        'messages': messages,
        'loggedin': request.user.is_authenticated()
    }
    return render(request, 'usermessages/message_detail.html', context)





