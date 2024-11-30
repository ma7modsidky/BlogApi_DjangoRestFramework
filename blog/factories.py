import factory
from factory.django import DjangoModelFactory
from faker import Faker

from . models import Post, Category


fake = Faker()

class PostsFactory(DjangoModelFactory):
    class Meta:
        model = Post
    title = factory.LazyAttribute(lambda _: fake.sentence(nb_words=6)) 
    brief = factory.LazyAttribute(lambda _: fake.text(max_nb_chars=200)) 
    body = factory.LazyAttribute(lambda _: fake.text(max_nb_chars=1000)) 
    # image = factory.django.ImageField(color='blue') 
    slug = factory.LazyAttribute(lambda _: fake.slug()) 
    published = factory.LazyAttribute(lambda _: fake.date_time_this_year())
    updated = factory.LazyAttribute(lambda _: fake.date_time_this_year())
    status = factory.LazyAttribute(lambda _: 'published')