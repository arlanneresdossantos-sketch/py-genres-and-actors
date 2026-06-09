# main.py
from db.models import Genre, Actor


def main() -> str:
    Genre.objects.create(name="Western")
    Genre.objects.create(name="Ação")
    Genre.objects.create(name="Drama")

    Actor.objects.create(first_name="George", last_name="Klooney")
    Actor.objects.create(first_name="Kianu", last_name="Reaves")
    Actor.objects.create(first_name="Scarlett", last_name="Keegan")
    Actor.objects.create(first_name="Will", last_name="Smith")
    Actor.objects.create(first_name="Jaden", last_name="Smith")
    Actor.objects.create(first_name="Scarlett", last_name="Johansson")

    Genre.objects.filter(name="Drama").update(name="Drama")
    Actor.objects.filter(first_name="George",
                         last_name="Klooney").update(last_name="Clooney")

    Actor.objects.filter(first_name="Kianu", last_name="Reaves").update(
        first_name="Keanu",
        last_name="Reeves"
    )

    Genre.objects.filter(name="Ação").delete()
    Actor.objects.filter(first_name="Scarlett").delete()

    return Actor.objects.filter(
        last_name="Smith").order_by("first_name").values_list(
        "first_name", "last_name")
