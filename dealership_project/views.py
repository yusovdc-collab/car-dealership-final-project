import json
import re

from datetime import date

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST


# ==========================================
# DEALERSHIP DATA
# ==========================================

DEALERS = [
    {
        "id": 1,
        "full_name": "Best Cars Dealership",
        "short_name": "Best Cars",
        "address": "100 Example Avenue",
        "city": "New York",
        "state": "NY",
        "zip": "10001",
        "lat": 40.7506,
        "long": -73.9972
    },
    {
        "id": 2,
        "full_name": "Premium Auto Sales",
        "short_name": "Premium Auto",
        "address": "200 Example Boulevard",
        "city": "Los Angeles",
        "state": "CA",
        "zip": "90001",
        "lat": 34.0522,
        "long": -118.2437
    },
    {
        "id": 3,
        "full_name": "Sunshine Auto Group",
        "short_name": "Sunshine Auto",
        "address": "300 Example Street",
        "city": "Miami",
        "state": "FL",
        "zip": "33101",
        "lat": 25.7617,
        "long": -80.1918
    },
    {
        "id": 4,
        "full_name": "Kansas City Auto Sales",
        "short_name": "Kansas City Auto",
        "address": "400 Example Road",
        "city": "Kansas City",
        "state": "KS",
        "zip": "66101",
        "lat": 39.1141,
        "long": -94.6275
    }
]


# ==========================================
# CUSTOMER REVIEWS
# ==========================================

REVIEWS = [
    {
        "id": 1,
        "dealership": 1,
        "name": "John Smith",
        "review": "Great customer service!",
        "purchase": True,
        "purchase_date": "2026-05-10",
        "car_make": "Toyota",
        "car_model": "Camry",
        "car_year": 2022
    },
    {
        "id": 2,
        "dealership": 1,
        "name": "Sarah Johnson",
        "review": "Helpful staff and good prices.",
        "purchase": True,
        "purchase_date": "2026-06-15",
        "car_make": "Honda",
        "car_model": "Civic",
        "car_year": 2023
    },
    {
        "id": 3,
        "dealership": 1,
        "name": "Michael Davis",
        "review": "Excellent selection of vehicles.",
        "purchase": False,
        "purchase_date": None,
        "car_make": None,
        "car_model": None,
        "car_year": None
    }
]


# ==========================================
# CAR MAKES AND MODELS
# ==========================================

CAR_MAKES = [
    {
        "id": 1,
        "name": "Toyota",
        "models": [
            {"id": 1, "name": "Camry", "type": "Sedan"},
            {"id": 2, "name": "Corolla", "type": "Sedan"},
            {"id": 3, "name": "RAV4", "type": "SUV"}
        ]
    },
    {
        "id": 2,
        "name": "Honda",
        "models": [
            {"id": 4, "name": "Civic", "type": "Sedan"},
            {"id": 5, "name": "Accord", "type": "Sedan"},
            {"id": 6, "name": "CR-V", "type": "SUV"}
        ]
    },
    {
        "id": 3,
        "name": "BMW",
        "models": [
            {"id": 7, "name": "3 Series", "type": "Sedan"},
            {"id": 8, "name": "X4", "type": "SUV"},
            {"id": 9, "name": "X6", "type": "SUV"}
        ]
    },
    {
        "id": 4,
        "name": "Ford",
        "models": [
            {"id": 10, "name": "Mustang", "type": "Coupe"},
            {"id": 11, "name": "Explorer", "type": "SUV"},
            {"id": 12, "name": "F-150", "type": "Truck"}
        ]
    }
]


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def find_dealer(dealer_id):
    return next(
        (
            dealer for dealer in DEALERS
            if dealer["id"] == dealer_id
        ),
        None
    )


def dealer_review_list(dealer_id):
    return [
        review for review in REVIEWS
        if review["dealership"] == dealer_id
    ]


# ==========================================
# QUESTION 16 - HOMEPAGE
# ==========================================

@require_GET
def home(request):
    return render(
        request,
        "home.html",
        {
            "dealers": DEALERS
        }
    )


# ==========================================
# QUESTION 5 - USER LOGIN
# ==========================================

@require_POST
def login_user(request):
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse(
            {"error": "Invalid JSON"},
            status=400
        )

    username = data.get(
        "userName",
        data.get("username", "")
    )

    password = data.get("password", "")

    user = authenticate(
        request,
        username=username,
        password=password
    )

    if user is not None:
        login(request, user)

        return JsonResponse({
            "userName": user.username,
            "status": "Authenticated"
        })

    return JsonResponse(
        {
            "userName": "",
            "status": "Failed",
            "message": "Invalid username or password"
        },
        status=401
    )


# ==========================================
# QUESTION 6 - USER LOGOUT
# ==========================================

@require_GET
def logout_user(request):
    logout(request)

    return JsonResponse({
        "userName": ""
    })


# ==========================================
# QUESTION 8 - GET DEALER REVIEWS
# ==========================================

@require_GET
def get_dealer_reviews(request, dealer_id):
    return JsonResponse({
        "reviews": dealer_review_list(dealer_id)
    })


# ==========================================
# QUESTION 9 - GET ALL DEALERS
# ==========================================

@require_GET
def get_dealers(request):
    return JsonResponse({
        "dealers": DEALERS
    })


# ==========================================
# QUESTION 10 - GET DEALER BY ID
# ==========================================

@require_GET
def get_dealer_by_id(request, dealer_id):
    dealer = find_dealer(dealer_id)

    if dealer is None:
        return JsonResponse(
            {"error": "Dealer not found"},
            status=404
        )

    return JsonResponse({
        "dealer": dealer
    })


# ==========================================
# QUESTION 11 - GET DEALERS BY STATE
# ==========================================

@require_GET
def get_dealers_by_state(request, state):
    state = state.strip().upper()

    matching_dealers = [
        dealer for dealer in DEALERS
        if dealer["state"].upper() == state
    ]

    return JsonResponse({
        "dealers": matching_dealers
    })


# ==========================================
# QUESTION 14 - GET CAR MAKES
# ==========================================

@require_GET
def get_all_car_makes(request):
    return JsonResponse({
        "car_makes": CAR_MAKES
    })


# ==========================================
# QUESTION 15 - SENTIMENT ANALYSIS
# ==========================================

POSITIVE_WORDS = {
    "fantastic",
    "excellent",
    "great",
    "amazing",
    "good",
    "wonderful",
    "helpful",
    "best",
    "friendly",
    "outstanding"
}

NEGATIVE_WORDS = {
    "bad",
    "terrible",
    "poor",
    "awful",
    "horrible",
    "worst",
    "disappointing",
    "rude",
    "unhelpful"
}


def calculate_sentiment(review_text):
    words = re.findall(
        r"\b\w+\b",
        review_text.lower()
    )

    positive_count = sum(
        word in POSITIVE_WORDS
        for word in words
    )

    negative_count = sum(
        word in NEGATIVE_WORDS
        for word in words
    )

    if positive_count > negative_count:
        return "positive"

    if negative_count > positive_count:
        return "negative"

    return "neutral"


@require_GET
def analyze_review(request):
    review_text = request.GET.get(
        "text", ""
    ).strip()

    if not review_text:
        return JsonResponse(
            {"error": "Review text is required"},
            status=400
        )

    return JsonResponse({
        "text": review_text,
        "sentiment": calculate_sentiment(review_text)
    })


@require_GET
def analyze_review_path(request, review_text):
    review_text = review_text.strip()

    if not review_text:
        return JsonResponse(
            {"error": "Review text is required"},
            status=400
        )

    return JsonResponse({
        "text": review_text,
        "sentiment": calculate_sentiment(review_text)
    })


# ==========================================
# QUESTION 19 - DEALER DETAILS
# ==========================================

@require_GET
def dealer_details(request, dealer_id):
    dealer = find_dealer(dealer_id)

    if dealer is None:
        return JsonResponse(
            {"error": "Dealer not found"},
            status=404
        )

    reviews = dealer_review_list(dealer_id)

    context = {
        "dealer": dealer,
        "dealer_id": dealer_id,
        "dealer_name": dealer["full_name"],
        "dealer_city": dealer["city"],
        "dealer_state": dealer["state"],
        "dealer_location": (
            f'{dealer["city"]}, {dealer["state"]}'
        ),
        "reviews": reviews,
        "review_count": len(reviews)
    }

    return render(
        request,
        "dealer_details.html",
        context
    )


# ==========================================
# QUESTION 20 - POST REVIEW
# ==========================================

@login_required(login_url="/site-login/")
def post_review(request, dealer_id):
    dealer = find_dealer(dealer_id)

    if dealer is None:
        return JsonResponse(
            {"error": "Dealer not found"},
            status=404
        )

    error = None

    if request.method == "POST":
        review_text = request.POST.get(
            "review", ""
        ).strip()

        purchase = request.POST.get(
            "purchase", "no"
        ).lower() in ("yes", "true", "on", "1")

        car_make = request.POST.get(
            "car_make", ""
        ).strip()

        car_model = request.POST.get(
            "car_model", ""
        ).strip()

        car_year_text = request.POST.get(
            "car_year", ""
        ).strip()

        purchase_date_text = request.POST.get(
            "purchase_date", ""
        ).strip()

        car_year = None
        purchase_date = None

        if not review_text:
            error = "Please enter a review."

        elif purchase and (
            not car_make or not car_model
        ):
            error = (
                "Please select a car make and model."
            )

        elif purchase:
            if car_year_text:
                try:
                    car_year = int(car_year_text)

                    if not 1886 <= car_year <= date.today().year + 1:
                        error = "Please enter a valid car year."

                except ValueError:
                    error = "Please enter a valid car year."

            if purchase_date_text:
                try:
                    purchase_date = date.fromisoformat(
                        purchase_date_text
                    ).isoformat()

                except ValueError:
                    error = "Please enter a valid purchase date."

        if error is None:
            new_review = {
                "id": max(
                    [r["id"] for r in REVIEWS],
                    default=0
                ) + 1,
                "dealership": dealer_id,
                "name": request.user.username,
                "review": review_text,
                "purchase": purchase,
                "purchase_date": (
                    purchase_date if purchase else None
                ),
                "car_make": (
                    car_make if purchase else None
                ),
                "car_model": (
                    car_model if purchase else None
                ),
                "car_year": (
                    car_year if purchase else None
                )
            }

            REVIEWS.append(new_review)

            return redirect(
                "dealer_details",
                dealer_id=dealer_id
            )

    context = {
        "dealer": dealer,
        "car_makes": CAR_MAKES,
        "error": error
    }

    return render(
        request,
        "post_review.html",
        context
    )


# ==========================================
# SITE LOGIN
# ==========================================

def site_login(request):
    return redirect("home")
