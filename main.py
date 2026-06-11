import init_django_orm  # noqa: F401
from db.models import Genre, Actor


def main():
    # 1. Create (Usando loops para evitar repetição)
    genres_to_create = ["Western", "Action", "Dramma"]
    for genre_name in genres_to_create:
        Genre.objects.create(name=genre_name)

    actors_to_create = [
        {"first_name": "George", "last_name": "Klooney"},
        {"first_name": "Kianu", "last_name": "Reaves"},
        {"first_name": "Scarlett", "last_name": "Keegan"},
        {"first_name": "Will", "last_name": "Smith"},
        {"first_name": "Jaden", "last_name": "Smith"},
        {"first_name": "Scarlett", "last_name": "Johansson"},
    ]
    for actor_data in actors_to_create:
        Actor.objects.create(**actor_data)

    # 2. Update
    Genre.objects.filter(name="Dramma").update(name="Drama")
    Actor.objects.filter(first_name="George", last_name="Klooney").update(last_name="Clooney")
    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(first_name="Keanu", last_name="Reeves")

    # 3. Delete
    Genre.objects.filter(name="Action").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    # 4. Return
    return Actor.objects.filter(last_name="Smith").order_by("first_name")
