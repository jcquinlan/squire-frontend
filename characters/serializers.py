from django.contrib.auth.models import User
from .models import Character, Journal, Entry
from rest_framework import serializers
from choices import RACE_CHOICES, CLASS_CHOICES


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        created_by = serializers.ReadOnlyField(source='created_by.username')
        class_type = serializers.ChoiceField(choices=CLASS_CHOICES)
        race = serializers.ChoiceField(choices=RACE_CHOICES)
        fields = ('id', 'created_by', 'first_name', 'last_name', 'class_type', 'race', 'max_hitpoints', 'experience',
                'level', 'background', 'current_hitpoints', 'proficiency_bonus',
                'strength', 'dexterity', 'constitution', 'intelligence',
                'wisdom', 'charisma', 'strength_modifier', 'dexterity_modifier', 'constitution_modifier',
                'intelligence_modifier', 'wisdom_modifier', 'charisma_modifier',
                'armor_class', 'speed', 'backstory',)

class JournalSerializer(serializers.HyperlinkedModelSerializer):
    num_of_entries = serializers.SerializerMethodField()

    def get_num_of_entries(self, obj):
        return obj.num_of_entries()

    class Meta:
        model = Journal
        created_by = serializers.ReadOnlyField(source='created_by.username')
        fields = ('id', 'name', 'created_by', 'created_at', 'character', 'num_of_entries')

class EntrySerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField('get_entry_author')

    def get_entry_author(self, obj):
        return obj.author()

    class Meta:
        model = Entry
        created_by = serializers.ReadOnlyField(source='created_by.username')
        fields = ('id', 'created_by', 'journal', 'created_at', 'author', 'content', )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email',)
        write_only_fields = ('password',)

    def create(self, validated_data):

        user = User.objects.create(
            username = validated_data['username'],
            # email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
