import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django
django.setup()

import random
from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker

fake = Faker()
topics = ['Search', 'Social', 'Food', 'Games', 'Shopping']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(n=5):

    for entry in range(n):
        topic = add_topic()

        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        #Create new webpage entry
        webpage = Webpage.objects.get_or_create(topic=topic, url=fake_url, name=fake_name)[0]

        #Create fake access record
        access_record = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]

if __name__=="__main__":
    print("populating")

    populate(15)

    print("process completed")
