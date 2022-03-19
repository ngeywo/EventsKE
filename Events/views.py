from django.shortcuts import render, redirect, get_object_or_404
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import Venueform, Eventform
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView
)


# Create your views here.
class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = ['name', 'event_date', 'venue', 'manager', 'attendees', 'description']

    def form_valid(self, form):
        form.instance.manager = self.request.user
        return super().form_valid(form)

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.manager:
            return True
        return False


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.manager:
            return True
        return False



def EventDetail(request,pk):
    event=  Event.objects.get(pk=pk)
    return render(request, 'Events/event_detail.html', {'event': event})



# def homee(request):
#     events = Event.objects.all()
#
#     return render(request, 'Events/homee.html', {'events': events})


class PostListView(ListView):
    model = Event
    paginate_by = 5
    template_name = 'Events/homee.html'
    ordering = '-date_posted'
    context_object_name = 'events'




class UserPostListView(ListView):
    model = Event
    template_name = 'Events/user_event.html'
    context_object_name = 'events'
    paginate_by = 5

    def get_query_set(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Event.objects.filter(manager=user).order_by('-date_posted')


def add_event(request):
    submitted = False
    if request.method == 'POST':
        form = Eventform(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add_event?submitted=True')

    else:
        form = Eventform
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'Events/add_event.html', {'form': form, 'submitted': submitted})


def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = Venueform(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list venues')
    return render(request, 'Events/update_venue.html', {
        'venue': venue,
        'form': form,
    })


def search_venue(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venue = Venue.objects.filter(name__contains=searched)
        return render(request, 'Events/search_venue.html', {
            'searched': searched,
            'venue': venue
        })

    else:
        return render(request, 'Events/search_venue.html', {

        })


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'Events/show_venue.html', {
        'venue': venue
    })


def list_venues(request):
    venue_list = Venue.objects.all()

    return render(request, 'Events/venue.html', {
        'venue_list': venue_list
    })


def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = Venueform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')

    else:
        form = Venueform
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'Events/add_venue.html', {'form': form, 'submitted': submitted})


def all_events(request):
    now = datetime.now()
    current_year = now.year
    event_list = Event.objects.all()
    return render(request, 'Events/event_list.html', {
        'event_list': event_list,
        'current_year': current_year,
    })


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = 'john'
    month = month.title()

    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    now = datetime.now()
    current_year = now.year

    time = now.strftime('%I:%M')

    # create calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    return render(request,
                  'Events/home.html', {
                      'fname': name,
                      'year': year,
                      'month': month,
                      'month_number': month_number,
                      'cal': cal,
                      'current_year': current_year,
                      'time': time,

                  })
