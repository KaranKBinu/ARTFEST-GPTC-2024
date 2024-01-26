from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("contest_details", views.contest_details, name="contest_details"),
    path("contests", views.contests, name="contests"),
    path("select-categories", views.select_categories, name="select_categories"),
    path("login/", views.user_login, name="user_login"),
    path("user_logout/", views.user_logout, name="user_logout"),
    path("contact/", views.contact_form, name="contact_form"),
    # path('upload_and_process_excel',views.upload_and_process_excel,name='upload_and_process_excel'),
]
