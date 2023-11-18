from django.urls import path

from .views import EventsListCreateView, ProgramListView, UserListView

urlpatterns = [
    path(r'events/', EventsListCreateView.as_view()),
    path(r'program_list', ProgramListView.as_view()),
    path(r'users_list', UserListView.as_view()),
]