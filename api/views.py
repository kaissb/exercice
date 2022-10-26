from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from noteapp.models import Note
from .serializers import NoteSerializer
from .serializers import RegisterSerializer






@api_view(['GET'])
def apiOverview(request):
    api_urls = {'Login':'userlogin/',
                'Register':'userregister/',
                'Userdata':'userdata/',
                'logout':'userlogout/',
                'List':'listenote/',
                'Detail':'detailnote/<str:pk>',
                'create':'addnote/',
                'update':'updatenote/<str:pk>',
                'delete':'deletenote/<str:pk>',

    }
    return Response(api_urls)



#User auth , register
@api_view(['POST'])
def userlogin(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return Response({
        'user_info':{
            'id':user.id,
            'username':user.username,
        },
        'token':token
    })

@api_view(['POST'])
def userregister(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    _, token = AuthToken.objects.create(user)
    return Response({
        'user_info':{
            'id':user.id,
            'username':user.username,
        },
        'token':token
    })

@api_view(['GET'])
def userdata(request):
    user = request.user
    if user.is_authenticated:
        return Response({
            'user infos:':{
                'id':user.id,
                'username':user.username
            },
        })
    return Response({'error': 'user not authenticated'},status=400)

# Note list, add , update , delete
@api_view(['GET'])
def NoteList(request):
    user=request.user
    if user.is_authenticated:
        notes = Note.objects.filter(user=user.id)
        serializer = NoteSerializer(notes, many = True)
        return Response(serializer.data)
    return Response({'error':'user not authenticated'}, status=400)

@api_view(['GET'])
def NoteDetail(request,pk):
    user=request.user
    if user.is_authenticated:
        notes = Note.objects.get(id=pk)
        serializer = NoteSerializer(notes, many = False)
        return Response(serializer.data)
    return Response({'error':'user not authenticated'}, status=400)


@api_view(['POST'])
def addNote(request):
    user=request.user
    if user.is_authenticated:
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    return Response({'error':'user not authenticated'}, status=400)


@api_view(['POST'])
def updateNote(request,pk):
    user=request.user
    if user.is_authenticated:
        note = Note.objects.get(id=pk)
        serializer = NoteSerializer(instance=note, data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    return Response({'error':'user not authenticated'}, status=400)

@api_view(['DELETE'])
def deleteNote(request,pk):
    user=request.user
    if user.is_authenticated:
        note = Note.objects.get(id=pk)
        note.delete()
        return Response("Delete successful")
    return Response({'error':'user not authenticated'}, status=400)