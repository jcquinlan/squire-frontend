from django.contrib import admin
from characters.models import Character, Journal, Entry

# Register your models here.
@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name')

@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('character',)

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('journal', 'content')
