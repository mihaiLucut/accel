from django.http import JsonResponse
from .models import Lead
from .serializers import LeadSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def my_requester(request):
    print(f'Request Method: {request.method}')
    print(f'Request Path: {request.path}')
    print(f'Request User: {request.user}')
    print(f'Request GET params: {request.GET}')
    print(f'Request POST data: {request.POST}')

@api_view(['GET', 'POST'])
def lead_list(request, format=None):
    my_requester(request)
    if request.method == 'GET':
        # get all the leads
        leads = Lead.objects.all()
        # serialize them
        serializer = LeadSerializer(leads, many=True)
        # return as json
        return Response(serializer.data)

    if request.method == 'POST':
        print("hello3")
        serializer = LeadSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def lead_detail(request, id, format=None):
    try:
        lead = Lead.objects.get(pk=id)
    except Lead.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = LeadSerializer(lead)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = LeadSerializer(lead, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        lead.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
