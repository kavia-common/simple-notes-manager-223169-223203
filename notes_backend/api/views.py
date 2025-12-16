from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Note
from .serializers import NoteSerializer

# PUBLIC_INTERFACE
@api_view(['GET'])
def health(request):
    """Health check endpoint.
    Returns 200 OK with a JSON payload indicating service is healthy.
    """
    return Response({"status": "ok"}, status=status.HTTP_200_OK)


class NoteListCreateView(generics.ListCreateAPIView):
    """List all notes or create a new note."""
    queryset = Note.objects.all().order_by('-updated_at')
    serializer_class = NoteSerializer


class NoteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update (PUT/PATCH), or delete a single note by ID."""
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
