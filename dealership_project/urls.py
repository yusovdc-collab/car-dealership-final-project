from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path(
        "admin/",
        admin.site.urls
    ),

    # Homepage
    path(
        "",
        views.home,
        name="home"
    ),

    # Website authentication
    path(
        "site-login/",
        views.site_login,
        name="site_login"
    ),

    path(
        "site-logout/",
        views.site_logout,
        name="site_logout"
    ),

    # Authentication API
    path(
        "login/",
        views.login_user,
        name="login_user"
    ),

    path(
        "logout/",
        views.logout_user,
        name="logout_user"
    ),

    # Dealership API
    path(
        "get_dealers/",
        views.get_dealers,
        name="get_dealers"
    ),

    path(
        "get_dealers/<int:dealer_id>/",
        views.get_dealer_by_id,
        name="get_dealer_by_id"
    ),

    path(
        "get_dealers/state/<str:state>/",
        views.get_dealers_by_state,
        name="get_dealers_by_state"
    ),

    path(
        "get_dealer_reviews/<int:dealer_id>/",
        views.get_dealer_reviews,
        name="get_dealer_reviews"
    ),

    # Car makes
    path(
        "get_cars/",
        views.get_all_car_makes,
        name="get_all_car_makes"
    ),

    path(
        "get_car_makes/",
        views.get_all_car_makes,
        name="get_car_makes"
    ),

    # Sentiment analysis
    path(
        "analyze_review/",
        views.analyze_review,
        name="analyze_review"
    ),

    path(
        "analyze_review/<path:review_text>/",
        views.analyze_review_path,
        name="analyze_review_path"
    ),

    # Dealership details
    path(
        "dealer/<int:dealer_id>/",
        views.dealer_details,
        name="dealer_details"
    ),

    # Post review
    path(
        "dealer/<int:dealer_id>/review/",
        views.post_review,
        name="post_review"
    ),

    # Legacy routes
    path(
        "dealer_details/<int:dealer_id>/",
        views.dealer_details,
        name="dealer_details_legacy"
    ),

    path(
        "post_review/<int:dealer_id>/",
        views.post_review,
        name="post_review_legacy"
    ),
]