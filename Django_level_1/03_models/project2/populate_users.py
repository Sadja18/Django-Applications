import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project2.settings")

import django
django.setup()

from app2.models import User
from faker import Faker

fake_generator = Faker()

def populate(N=10):
    for entry in range(N):
        fake_name = fake_generator.name().split()
        fake_fname = fake_name[0]
        fake_lname = fake_name[1]
        fake_email = fake_generator.email()

        user = User.objects.get_or_create(fname = fake_fname,
                                          lname = fake_lname,
                                          email = fake_email)

if __name__ == "__main__":
    print("Populating....")
    populate(40)
    print("Completed")
