from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Artical
from .ArticalSerializer import ArticalSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

from rest_framework import generics
from rest_framework import mixins

from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.

'''
MODEL VIEW SET Example
'''
class ArticalModelViewSet(viewsets.ModelViewSet):
    serializer_class = ArticalSerializer
    queryset = Artical.objects.all()



'''
GENERIC VIEW SET Example
'''
class ArticalGenericViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticalSerializer
    queryset = Artical.objects.all()



'''
VIEW SET & ROUTERS EXAMPLE
'''
class ArticalViewSet(viewsets.ViewSet):
    def list(self, request):
        articals = Artical.objects.all()
        #convert articals data to serializer
        serializer = ArticalSerializer(articals, many = True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ArticalSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk = None):
        querySet = Artical.objects.all()
        artical = get_object_or_404(querySet, pk = pk)
        serializer = ArticalSerializer(artical)
        return Response(serializer.data)

    def update(self, request, pk=None):
        artical = Artical.objects.get(pk = pk)
        serializer = ArticalSerializer(artical, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        artical = Artical.objects.get(pk = pk)
        artical.delete()
        return JsonResponse({'message':'Successfully deleted the information.'})




'''
GENERIC API VIEW Example
'''
class ArticalGenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = ArticalSerializer
    queryset = Artical.objects.all()

    lookup_field = 'id'

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]

    permission_classes = [IsAuthenticated]

    def get(self, request, id = None):
        print('ID :')
        print( id)
        if id:
            return self.retrieve(request)
        else:
            print('No ID')
            return self.list(request)

    def post(self, request, id = None):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)
    
    def delete(self, request, id=None):
        return self.destroy(request, id)





'''
CLASS BASED API VIEW Example
'''
class ArticalAPIView(APIView):

    def get(self, request):
        articals = Artical.objects.all()
        #convert articals data to serializer
        serializer = ArticalSerializer(articals, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ArticalSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class ArticalDetailsAPIView(APIView):

    def get_object(self, id):
        try:
            return Artical.objects.get(id=id)
        except Artical.DoesNotExist:
            return JsonResponse({'message':'No data found'})
            
    def get(self, request, id):
        artical = self.get_object(id)
        serializer = ArticalSerializer(artical)
        return Response(serializer.data)

    def put(self, request, id):
        artical = self.get_object(id)
        serializer = ArticalSerializer(artical, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        artical = self.get_object(id)
        artical.delete()
        return JsonResponse({'message':'Successfully deleted the information.'})




'''
API VIEW Example
'''
@api_view(['GET', 'POST'])
def artical(request):
    if request.method == 'GET':
        articals = Artical.objects.all()
        #convert articals data to serializer
        serializer = ArticalSerializer(articals, many = True)
        return Response(serializer.data)
        
    elif request.method == 'POST':
        serializer = ArticalSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    else:
        return JsonResponse({'message': 'Invalid Request!'})



@api_view(['GET', 'PUT', 'DELETE'])
def artical_details(request, id):
    try:
        artical = Artical.objects.get(id=id)
    except Artical.DoesNotExist:
        return JsonResponse({'message':'No data found'})
        
    if request.method == 'GET':
        serializer = ArticalSerializer(artical)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticalSerializer(artical, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artical.delete()
        return JsonResponse({'message':'Successfully deleted the information.'})
    
    else:
        return JsonResponse({'message': 'Invalid Request!'})



'''
FUNCTION BASED API VIEW Example
'''
# @csrf_exempt
# def artical(request):
#     if request.method == 'GET':
#         articals = Artical.objects.all()
#         #convert articals data to serializer
#         serializer = ArticalSerializer(articals, many = True)
#         return JsonResponse(serializer.data, safe = False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticalSerializer(data = data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status = 201)
#         return JsonResponse(serializer.errors, status = 400)

#     else:
#         return JsonResponse({'message': 'Invalid Request!'})



# @csrf_exempt
# def artical_details(request, id):
#     try:
#         artical = Artical.objects.get(id=id)
#     except Artical.DoesNotExist:
#         return JsonResponse({'message':'No data found'})
        
#     if request.method == 'GET':
#         serializer = ArticalSerializer(artical)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticalSerializer(artical, data = data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status = 400)

#     elif request.method == 'DELETE':
#         artical.delete()
#         return JsonResponse({'message':'Successfully deleted the information.'})
    
#     else:
#         return JsonResponse({'message': 'Invalid Request!'})



