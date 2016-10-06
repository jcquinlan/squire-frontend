from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

CLASS_CHOICES = (
    (u'1', u'Barbarian'),
    (u'2', u'Bard'),
    (u'3', u'Cleric'),
    (u'4', u'Druid'),
    (u'5', u'Fighter'),
    (u'6', u'Mage'),
    (u'7', u'Monk'),
    (u'8', u'Paladin'),
    (u'9', u'Ranger'),
    (u'10', u'Sorceror'),
    (u'11', u'Rogue'),
    (u'12', u'Warlock'),
)

RACE_CHOICES = (
    (u'1', u'Dragonborn'),
    (u'2', u'Dwarf'),
    (u'3', u'Elf'),
    (u'4', u'Gnome'),
    (u'5', u'Half-Elf'),
    (u'6', u'Half-Orc'),
    (u'7', u'Halfling'),
    (u'8', u'Human'),
    (u'9', u'Tiefling'),
    (u'10', u'Genasi'),
    (u'11', u'Goliath'),
)

class Character(models.Model):
    created_by = models.ForeignKey(User)
    alive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    title = models.CharField(max_length=20, null=True, blank=True)
    class_type = models.CharField(max_length=1, choices=CLASS_CHOICES)
    level = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(20),])
    race = models.CharField(max_length=30, choices=RACE_CHOICES)
    background = models.CharField(max_length=30)
    max_hitpoints = models.IntegerField()
    current_hitpoints = models.IntegerField()
    proficiency_bonus = models.IntegerField(default=2)
    strength = models.PositiveIntegerField(default=10)
    strength_modifier = models.IntegerField(default=0);
    dexterity = models.PositiveIntegerField(default=10)
    dexterity_modifier = models.IntegerField(default=0);
    constitution = models.PositiveIntegerField(default=10)
    constitution_modifier = models.IntegerField(default=0);
    intelligence = models.PositiveIntegerField(default=10)
    intelligence_modifier = models.IntegerField(default=0);
    wisdom = models.PositiveIntegerField(default=10)
    wisdom_modifier = models.IntegerField(default=0);
    charisma = models.PositiveIntegerField(default=10)
    charisma_modifier = models.IntegerField(default=0);
    armor_class = models.IntegerField()
    speed = models.IntegerField(default=30)
    backstory = models.TextField(null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        import math
        self.strength_modifier = math.trunc((self.strength - 10) / 2)
        self.dexterity_modifier = math.trunc((self.dexterity - 10) / 2)
        self.constitution_modifier = math.trunc((self.constitution - 10) / 2)
        self.intelligence_modifier = math.trunc((self.intelligence - 10) / 2)
        self.wisdom_modifier = math.trunc((self.wisdom - 10) / 2)
        self.charisma_modifier = math.trunc((self.charisma - 10) / 2)
        self.proficiency_bonus = math.ceil((self.level / 4) + 1)
        super(Character, self).save(*args, **kwargs)

class Journal(models.Model):
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    character = models.OneToOneField(Character)

    def num_of_entries(self):
        return Entry.objects.filter(journal=self).count()

    def author(self):
        return '%s %s' % (self.character.first_name, self.character.last_name)

    def __str__(self):
        return '%s %s\'s Journal' % (self.character.first_name, self.character.last_name)

class Entry(models.Model):
    created_by = models.ForeignKey(User)
    journal = models.ForeignKey(Journal)
    title = models.CharField(max_length=30, null=True, blank=True)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def author(self):
        return self.journal.author()
