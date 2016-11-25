from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route, detail_route
from django.contrib.auth.models import User
from .models import Character, Journal, Entry
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view, permission_classes
from .permissions import IsOwner
from .serializers import CharacterSerializer, JournalSerializer, EntrySerializer, UserSerializer


@api_view(['POST'])
@permission_classes([permissions.AllowAny,])
def create_auth(request):
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        User.objects.create_user(
            email = serialized.data['email'],
            username = serialized.data['username'],
            password = serialized.data['password']
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    permission_classes = (IsOwner,)

    def get_queryset(self):
        user = self.request.user
        return Character.objects.filter(created_by=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    permission_classes = (IsOwner,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @list_route(methods=['get'])
    def character(self, request):
        character_id = request.GET.get('character_id', '')
        journals = Journal.objects.filter(character=character_id)

        serializer = self.get_serializer(journals, many=True)
        return Response(serializer.data)



class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    permission_classes = (IsOwner,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def save(self):
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

    @list_route(methods=['get'])
    def journal(self, request):
        journal_id = request.GET.get('journal_id', '')
        entries = Entry.objects.filter(journal=journal_id)

        serializer = self.get_serializer(entries, many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)
