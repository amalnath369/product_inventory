from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from .models import Product
from .serializers import ProductSerializer



def home(request):
    return render(request, "index.html")



class ProductListCreateAPIView(APIView):

    def get(self, request):
        products =  Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({'status': 'success', 'data': serializer.data}, 
                        status=status.HTTP_200_OK)
    

    def post(self,request):
        data = request.data
        serialiser = ProductSerializer(data=data)
        if serialiser.is_valid():
            serialiser.save()
            return Response({'status': 'success', 'message': 'product created successfully'}, 
                            status=status.HTTP_201_CREATED)
        else:
            return Response({'status': 'failed', 'message': 'product creation failed','error':serialiser.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)

        
class ProductDetailAPIView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)
    
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response({'status': 'success','data': serializer.data}, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success','data': serializer.data,'message': 'Product updated successfully'},
                             status=status.HTTP_200_OK)
        
        return Response({
            'status': 'error',
            'errors': serializer.errors,
            'message': 'Validation failed'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'data': serializer.data,
                'message': 'Product updated successfully'
            }, status=status.HTTP_200_OK)
        
        return Response({
            'status': 'error',
            'errors': serializer.errors,
            'message': 'Validation failed'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        
        return Response({
            'status': 'success',
            'message': 'Product deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)