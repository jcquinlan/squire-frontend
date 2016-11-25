from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from choices import RACE_CHOICES, CLASS_CHOICES

class Character(models.Model):
    created_by = models.ForeignKey(User)
    alive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    title = models.CharField(max_length=20, null=True, blank=True)
    class_type = models.CharField(max_length=1, choices=CLASS_CHOICES)
    experience = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(355000),])
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

    def return_level(self, experience):
        if experience >= 355000:
            return 20
        elif experience >= 305000:
            return 19
        elif experience >= 265000:
            return 18
        elif experience >= 225000:
            return 17
        elif experience >= 195000:
            return 16
        elif experience >= 165000:
            return 15
        elif experience >= 140000:
            return 14
        elif experience >= 120000:
            return 13
        elif experience >= 100000:
            return 12
        elif experience >= 85000:
            return 11
        elif experience >= 64000:
            return 10
        elif experience >= 48000:
            return 9
        elif experience >= 34000:
            return 8
        elif experience >= 23000:
            return 7
        elif experience >= 14000:
            return 6
        elif experience >= 6500:
            return 5
        elif experience >= 2700:
            return 4
        elif experience >= 900:
            return 3
        elif experience >= 300:
            return 2
        else:
            return 1

    def save(self, *args, **kwargs):
        import math
        self.strength_modifier = math.trunc((self.strength - 10) / 2)
        self.dexterity_modifier = math.trunc((self.dexterity - 10) / 2)
        self.constitution_modifier = math.trunc((self.constitution - 10) / 2)
        self.intelligence_modifier = math.trunc((self.intelligence - 10) / 2)
        self.wisdom_modifier = math.trunc((self.wisdom - 10) / 2)
        self.charisma_modifier = math.trunc((self.charisma - 10) / 2)
        self.proficiency_bonus = math.ceil((self.level / 4) + 1)
        self.level = self.return_level(self.experience)
        super(Character, self).save(*args, **kwargs)

class Journal(models.Model):
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30, unique=True)
    character = models.ForeignKey(Character)

    def num_of_entries(self):
        return Entry.objects.filter(journal=self).count()

    def author(self):
        return '%s %s' % (self.character.first_name, self.character.last_name)

    def __str__(self):
        return '%s %s\'s Journal' % (self.character.first_name, self.character.last_name)

class Entry(models.Model):
    created_by = models.ForeignKey(User)
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_by

    def author(self):
        return self.journal.author()
