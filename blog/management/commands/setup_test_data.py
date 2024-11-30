import random

from django.db import transaction
from django.core.management.base import BaseCommand

from blog.models import Post
from blog.factories import PostsFactory

NUM_POSTS = 100


class Command(BaseCommand):
    help = 'Generate some test data'
    
    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting old data ...\n')
        models = [Post]
        # for m in models:
        #     m.objects.all().delete()
            
        self.stdout.write('Generating new data...\n')   
        # create customers
        # CustomerFactory.create_batch(NUM_CUSTOMERS)
        PostsFactory.create_batch(NUM_POSTS)
        self.stdout.write('Data created successfuly\n')        
    