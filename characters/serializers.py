from django.contrib.auth.models import User
from .models import Character, Journal, Entry
from rest_framework import serializers


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        created_by = serializers.ReadOnlyField(source='created_by.username')
        fields = ('created_by', 'first_name', 'last_name', 'class_type', 'max_hitpoints',
                'level', 'race', 'background', 'current_hitpoints', 'proficiency_bonus',
                'strength', 'dexterity', 'constitution', 'intelligence',
                'wisdom', 'charisma', 'strength_modifier', 'dexterity_modifier', 'constitution_modifier',
                'intelligence_modifier', 'wisdom_modifier', 'charisma_modifier',
                'armor_class', 'speed', 'backstory',)

class JournalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Journal
        created_by = serializers.ReadOnlyField(source='created_by.username')
        fields = ('created_by', 'created_at', 'character', )

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        created_by = serializers.ReadOnlyField(source='created_by.username')
        fields = ('created_by', 'journal', 'created_at', 'title', 'content', )

class UserSerializer(serializers.ModelSerializer):
    # characters = serializers.PrimaryKeyRelatedField(many=True, queryset=Character.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username', )
