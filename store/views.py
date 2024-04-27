from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from store.serializers import ProductMaterialsSerializer


class CalculateTotalCost(APIView):
    def post(self, request):
        serializer = ProductMaterialsSerializer(data=request.data)
        if serializer.is_valid():
            product_materials = serializer.validated_data.get('product_materials', [])
            warehouse_totals = {}
            for material in product_materials:
                warehouse_id = material.get('warehouse_id')
                price = material.get('price')
                qty = material.get('qty')
                total_cost = price * qty
                if warehouse_id in warehouse_totals:
                    warehouse_totals[warehouse_id] += total_cost
                else:
                    warehouse_totals[warehouse_id] = total_cost
            return Response(warehouse_totals, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
