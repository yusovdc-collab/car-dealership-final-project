from django.contrib import admin
from django.urls import path

from .views import (
    home,
    login_user,
    logout_user,
    get_dealer_reviews,
    get_dealers,
    get_dealer_by_id,
    get_dealers_by_state,
    get_all_car_makes,
    analyze_review,
    analyze_review_path,
    dealer_details,
    post_review,
    site_login
)


urlpatterns = [

    # ======================================
    # HOMEPAGE
    # ======================================

    path(
        "",
        home,
        name="home"
    ),

    # ======================================
    # DJANGO ADMIN
    # ======================================

    path(
        "admin/",
        admin.site.urls
    ),

    # ======================================
    # QUESTION 5 - LOGIN
    # ======================================

    path(
        "djangoapp/login",
        login_user,
        name="login_user"
    ),

    path(
        "djangoapp/login/",
        login_user
    ),

    # ======================================
    # QUESTION 6 - LOGOUT
    # ======================================

    path(
        "djangoapp/logout",
        logout_user,
        name="logout_user"
    ),

    path(
        "djangoapp/logout/",
        logout_user
    ),

    # ======================================
    # QUESTION 8 - DEALER REVIEWS
    # ======================================

    path(
        "fetchReviews/dealer/<int:dealer_id>",
        get_dealer_reviews,
        name="fetch_reviews"
    ),

    path(
        "fetchReviews/dealer/<int:dealer_id>/",
        get_dealer_reviews
    ),

    path(
        "djangoapp/get_dealer_reviews/<int:dealer_id>",
        get_dealer_reviews
    ),

    # ======================================
    # QUESTION 9 - ALL DEALERS
    # ======================================

    path(
        "fetchDealers",
        get_dealers,
        name="fetch_dealers"
    ),

    path(
        "fetchDealers/",
        get_dealers
    ),

    path(
        "djangoapp/get_dealers",
        get_dealers
    ),

    # ======================================
    # QUESTION 10 - DEALER BY ID
    # ======================================

    path(
        "fetchDealer/<int:dealer_id>",
        get_dealer_by_id,
        name="fetch_dealer"
    ),

    path(
        "fetchDealer/<int:dealer_id>/",
        get_dealer_by_id
    ),

    path(
        "djangoapp/dealer/<int:dealer_id>",
        get_dealer_by_id
    ),

    # ======================================
    # QUESTION 11 - DEALERS BY STATE
    # ======================================

    path(
        "fetchDealers/<str:state>",
        get_dealers_by_state,
        name="fetch_dealers_by_state"
    ),

    path(
        "fetchDealers/<str:state>/",
        get_dealers_by_state
    ),

    path(
        "djangoapp/get_dealers_by_state/<str:state>",
        get_dealers_by_state
    ),

    # ======================================
    # QUESTION 14 - CAR MAKES AND MODELS
    # ======================================

    path(
        "djangoapp/get_cars",
        get_all_car_makes,
        name="get_all_car_makes"
    ),

    path(
        "djangoapp/get_cars/",
        get_all_car_makes
    ),

    # ======================================
    # QUESTION 15 - SENTIMENT ANALYSIS
    # ======================================

    path(
        "analyze/<str:review_text>",
        analyze_review_path,
        name="analyze_review_path"
    ),

    path(
        "analyze/<str:review_text>/",
        analyze_review_path
    ),

    path(
        "djangoapp/analyze_review",
        analyze_review,
        name="analyze_review"
    ),

    path(
        "djangoapp/analyze_review/",
        analyze_review
    ),

    # ======================================
    # QUESTION 19 - DEALER DETAILS
    # ======================================

    path(
        "review-dealer/<int:dealer_id>/",
        dealer_details,
        name="dealer_details"
    ),

    # ======================================
    # QUESTION 20 - POST REVIEW
    # ======================================

    path(
        "post-review/<int:dealer_id>/",
        post_review,
        name="post_review"
    ),

    # ======================================
    # SITE LOGIN
    # ======================================

    path(
        "site-login/",
        site_login,
        name="site_login"
    )

]
