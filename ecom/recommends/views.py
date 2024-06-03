from django.shortcuts import render
from .recommendation_engine import get_dataset, train_model, get_user_recommendations
from .models import Recommendation

def recommendation_list(request):
    user = request.user.userprofile
    data = get_dataset()
    model = train_model(data)
    recommendations = get_user_recommendations(user.user.id, model)

    # Clear existing recommendations for the user
    Recommendation.objects.filter(user=user).delete()

    # Store the new recommendations in the database
    for product in recommendations:
        Recommendation.objects.create(product=product, user=user)

    return render(request, 'recommendations/recommendation_list.html', {'recommendations': recommendations})