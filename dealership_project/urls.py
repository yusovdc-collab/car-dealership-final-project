from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from .views import (
    login_user,
    logout_user,
    get_dealers,
    get_dealer_reviews,
    get_dealer_by_id,
    get_dealers_by_state,
    get_all_car_makes,
    analyze_review,
    dealer_details,
    post_review,
)

urlpatterns = [

    # Django administration
    path(
        "admin/",
        admin.site.urls,
    ),

    # JSON authentication endpoints
    path(
        "login/",
        login_user,
        name="login",
    ),

    path(
        "logout/",
        logout_user,
        name="logout",
    ),

    # Browser login page
    path(
        "site-login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="site_login",
    ),

    # Browser logout
    path(
        "site-logout/",
        auth_views.LogoutView.as_view(),
        name="site_logout",
    ),

    # Get all dealerships
    path(
        "djangoapp/get_dealers",
        get_dealers,
        name="get_dealers",
    ),

    # Get dealership reviews
    path(
        "djangoapp/get_dealer_reviews/<int:dealer_id>",
        get_dealer_reviews,
        name="get_dealer_reviews",
    ),

    # Get dealership by ID
    path(
        "djangoapp/dealer/<int:dealer_id>",
        get_dealer_by_id,
        name="get_dealer_by_id",
    ),

    # Filter dealerships by state
    path(
        "djangoapp/get_dealers_by_state/<str:state>",
        get_dealers_by_state,
        name="get_dealers_by_state",
    ),

    # Car makes and models
    path(
        "djangoapp/get_cars",
        get_all_car_makes,
        name="get_all_car_makes",
    ),

    # Sentiment analysis
    path(
        "djangoapp/analyze_review",
        analyze_review,
        name="analyze_review",
    ),

    # Dealer details and reviews
    path(
        "review-dealer/<int:dealer_id>/",
        dealer_details,
        name="dealer_details",
    ),

    # Post review form
    path(
        "post-review/<int:dealer_id>/",
        post_review,
        name="post_review",
    ),
]
