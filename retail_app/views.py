from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Store
from .serializers import StoreSerializer, StoreDetailSerializer


class StoreList(APIView):
    def get(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)


class StoreDetail(APIView):

    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        store = self.get_object(pk)
        serializer = StoreDetailSerializer(store)
        return Response(serializer.data)