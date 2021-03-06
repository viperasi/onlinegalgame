#-*- coding:utf-8 -*-
from django import template
from onlinegalgame.story.models import UserStory

register = template.Library()

def getstory(value, type):
    try:
        UserStory.objects.filter(author=value).order_by('sort')[:1][0]
    except:
        if type == 'storyid' :
            return 0
    else:
        story = UserStory.objects.filter(author=value).order_by('sort')[:1][0]
        if type == 'title':
            return story.title
        if type == 'date':
            return story.cdate
        if type == 'summary':
            return story.summary
        if type == 'storyid':
            return story.id
    
register.filter('getstory', getstory)
