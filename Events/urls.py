from django.urls import path
from . import views
from .views import PostListView
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    EventUpdateView,
    EventDeleteView
)

urlpatterns = [
    # path('', views.home, name='home'),
    path('', PostListView.as_view(), name= 'homee'),
    # path('accounts/'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('Events/',views.all_events,name = 'Event list'),
    path('add_venue/', views.add_venue,name='Add venue'),
    path('add_event/', views.add_event,name='Add Event'),
    path('list_venues/', views.list_venues, name='list venues'),
    path('show_venue/<venue_id>/', views.show_venue,name='show venue'),
    path('search_venue/', views.search_venue, name='search venues'),
    path('update_venue/<venue_id>/', views.update_venue, name='update venue'),
    path('user/<str:username>/', views.UserPostListView.as_view(), name='user-events'),
    path('event/<int:pk>/', views.EventDetail, name='Event_detail'),
    path('event/<int:pk>/update/', EventUpdateView.as_view(), name='event-update'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event-delete'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
