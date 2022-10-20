from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from noteapp.models import Note
from .serialisers import NoteSerializer


@api_view(['GET'])
def getData(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many = True)
    return Response(serializer.data)


@api_view(['POST'])
def addNote(request):
    serializer = NoteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return response(serializer.data)