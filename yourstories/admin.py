from django.contrib import admin

from .models import Story

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'author_email', 'author_email_verified', 'submitted_at', 'published')
    list_filter = ['submitted_at', 'author_email_verified']
    search_fields = ['title', 'content']
    readonly_fields = ['author_email_verified']
    fieldsets = [
        ('Display', {'fields': ['title', 'content', 'author', 'submitted_at']}),
        ('Admin', {'fields': ['author_email', 'author_email_verified', 'published']})
    ]
    actions = ['publish_stories', 'unpublish_stories']

    def publish_stories(self, req, q):
        q.update(published=True)
    publish_stories.short_description = 'Publish selected stories'

    def unpublish_stories(self, req, q):
        q.update(published=False)
    unpublish_stories.short_description = 'Unpublish selected stories'
