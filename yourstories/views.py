from uuid import UUID
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import mail_admins, send_mail
from django.template.loader import render_to_string

from .models import Story

def home(request):
    return render(request, 'home.html', dict(num_stories=Story.objects.filter(published=True).count(), stories=Story.objects.filter(published=True).order_by('-submitted_at')[0:5]))

def index(request):
    return render(request, 'index.html', dict(stories=Story.objects.filter(published=True).order_by('-submitted_at')))

def post(request):
    return render(request, 'submit.html', dict(previous={}))

def post_handler(request):
    def error(msg):
        return render(request, 'submit.html', dict(error_message=msg, previous=request.POST))
    story_dict = {}
    try:
        story_dict['title'] = request.POST['title']
    except KeyError as e:
        return error('Please add a title')
    try:
        story_dict['content'] = request.POST['content']
    except KeyError as e:
        return error('Please add some content')
    try:
        story_dict['author'] = request.POST['author']
    except KeyError as e:
        story_dict['author'] = None
    try:
        story_dict['author_email'] = request.POST['author_email']
    except KeyError as e:
        return error('Please provide an email address. We will need it to verify your story.')

    story = Story(**story_dict)
    story.save()
    mail_admins(
        subject='New story submitted: {} by {}'.format(story.title, story.author or 'Anonymous'),
        message='A new story was submitted, please view it on the admin portal. Id: {}'.format(story.id)
    )
    send_mail(
        subject='Please confirm your email address for borisfucked.me story submission',
        message=render_to_string('email.html', dict(story=story)),
        from_email='noreply@borisfucked.me',
        recipient_list=[story.author_email]
    )
    return HttpResponseRedirect(reverse('yourstories:story', args=(story.id,)))

def story(request, id):
    return render(request, 'story.html', dict(story=get_object_or_404(Story, pk=id)))

def verify(request, id, code):
    story = get_object_or_404(Story, pk=id)
    if UUID(code) == story.email_verification_code:
        story.author_email_verified = True
        story.save()
        return HttpResponseRedirect(reverse('yourstories:story', args=(story.id,)))
    else:
        return render(request, 'error.html', dict(message='Sorry, confirmation failed. Story could be already confirmed.'))
