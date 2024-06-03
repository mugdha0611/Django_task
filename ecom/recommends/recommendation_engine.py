from surprise import Reader, Dataset, SVD
from django.contrib.auth.models import User
from products.models import Product
import pandas as pd

def get_dataset():
    # Retrieve all users
    users = User.objects.all()

    data = []
    for user in users:
        # Get the products that the user has "viewed" or "interacted with"
        viewed_products = Product.objects.order_by('?')[:10]  

        for product in viewed_products:
            data.append((user.id, product.id, 5))  

    df = pd.DataFrame(data, columns=['user_id', 'item_id', 'rating'])
    reader = Reader(rating_scale=(1, 5))

    # Create the dataset
    data = Dataset.load_from_df(df, reader)
    return data

def train_model(data):
    #  SVD algorithm for collaborative filtering
    algo = SVD()

   
    model = algo.fit(data.build_full_trainset())
    return model

def get_user_recommendations(user_id, model, n=10):
    user = User.objects.get(id=user_id)
    existing_recommendations = user.recommendation_set.values_list('product__id', flat=True)

    all_products = Product.objects.exclude(id__in=list(existing_recommendations)).values_list('id', flat=True)

    predictions = [(user_id, product_id) for product_id in all_products]

    predictions = model.test(predictions)

    predictions = sorted(predictions, key=lambda x: x.est, reverse=True)

    top_recommendations = [prediction.iid for prediction in predictions[:n]]

    recommended_products = Product.objects.filter(id__in=top_recommendations)
    return recommended_products