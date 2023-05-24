from django.http import Http404
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest, Movie, Reservation
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, filters
from .serializers import GuestSerializer, MovieSerializer, ReservationSerializer

from rest_framework.views import APIView
# Create your views here.


# 1 without rest and no model query function based views (FBV)

def no_rest_no_model(request):

    guests = [
        {
            'id': 1,
            "Name": "Omar",
            "mobile": 789456,
        },
        {
            'id': 2,
            'name': "yassin",
            'mobile': 74123,
        }
    ]

    return JsonResponse(guests, safe=False)


# 2 model data default djanog without rest

def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        "guests": list(data.values('name', 'mobile'))

    }

    return JsonResponse(response)


# List == GET
# Create == POST
# pk query == GET
# Update == PUT
# Delete destroy == DELETE


# 3 Function based views
# 3.1 GET POST
# بقلوله هنا انك بتهندل نوعين من الريكوست الى قايلك عليهم الى هما ال get و ال post
@api_view(['GET', 'POST'])
def FBV_List(request):

    # Get
    if request.method == 'GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)

     # POST
     # post -> params -> data -> url -> view - > post ->serializer -> guest serializer -> database
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():   # check if there are data or not
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# 3.2 GET PUT DELETE
@api_view(['GET', 'PUT', 'DELETE'])
def FBV_PK(request, pk):
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

     # Get
    if request.method == 'GET':

        serializer = GuestSerializer(guest)
        return Response(serializer.data)

     # PUT

    elif request.method == 'PUT':
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():   # check if there are data or not
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

   # DELETE
    elif request.method == 'DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CBV Class based views
# 4.1 List and Create == GET and POST
class CBV_List(APIView):
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.data,
            status=status.HTTP_400_BAD_REQUEST
        )

# 4.2 GET PUT DELETE cloass based views -- pk


class CBV_PK(APIView):
    def get_object(self, pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)

    def put(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
