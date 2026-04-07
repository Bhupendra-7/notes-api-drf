from rest_framework.authentication import TokenAuthentication
from .serializers import NoteSerializer, UserSignupSerializer
from .models import Note
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication




# List Notes (GET all notes):
class NoteList(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        priority = request.query_params.get('priority', None) #key and value returns , if no val then None
        if request.user.is_authenticated:
            # Authenticated user, filter by priority if provided, else all their notes
            if priority:
                notes = Note.objects.filter(priority=priority, owner=request.user)
            else:
                notes = Note.objects.filter(owner=request.user)
        else:
            # Unauthenticated user, return all notes (no filtering)
            notes = Note.objects.all()

        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)



# CREATING A NNOTE
class NoteCreate(APIView):
    # authentication_classes = [TokenAuthentication, JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = NoteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(owner = request.user)  #setting owner here
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



#Retrieve/GET a Single NNote by ID:
class NoteDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        # Check ownership
        if note.owner != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = NoteSerializer(note)
        return Response(serializer.data)
    

#Update a Note 
class NoteUpdate(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        if note.owner != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        # try:
        #     note = Note.objects.get(pk=pk)
        # except Note.DoesNotExist:
        #     return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = NoteSerializer(note)
        return Response(serializer.data)


    def put(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        if note.owner != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        # try:
        #     note = Note.objects.get(pk=pk)
        # except Note.DoesNotExist:
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = NoteSerializer(note, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class NoteDelete(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        if request.user == note.owner or request.user.is_staff:
            serializer = NoteSerializer(note)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
    
    
    def delete(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        if request.user == note.owner or request.user.is_staff:
            note.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
        # try:
        #     note = Note.objects.get(pk=pk)
        #     note.delete()
        #     return Response(status=status.HTTP_204_NO_CONTENT)
        # except Note.DoesNotExist:
        #     return Response(status=status.HTTP_404_NOT_FOUND)


class SignupView(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Logs out the current user by deleting their token.
        # DRF's TokenAuthentication adds `auth_token` to the user object when the user is authenticated.
        # After this, the user's token becomes invalid and cannot be used in future requests.
        request.user.auth_token.delete()
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

