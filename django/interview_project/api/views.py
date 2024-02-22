from django.http import JsonResponse
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import QueryHistory
from .serializers import QueryHistorySerializer
import socket, os
#from prometheus_client import Counter, generate_latest

#REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests', ['method', 'endpoint', 'status'])

# Root endpoint
@api_view(['GET'])
def root(request):
    kubernetes = os.getenv('KUBERNETES_SERVICE_HOST')
    if kubernetes:
        return JsonResponse({
        "version": "0.1.0",
        "date": int(timezone.now().timestamp()),
        "kubernetes": True
        })
    else:
        return JsonResponse({
        "version": "0.1.0",
        "date": int(timezone.now().timestamp()),
        "kubernetes": False
        })

# Health endpoint
@api_view(['GET'])
def health(request):
    return Response({"status": "healthy"})

# Metrics endpoint
@api_view(['GET'])
def metrics(request):
    # Increment the counter for each request to the metrics endpoint
    #REQUEST_COUNT.labels(method=request.method, endpoint=request.path, status=200).inc()

    # Return the Prometheus metrics
    #return HttpResponse(generate_latest())
    return Response("Metrics")


# Lookup endpoint
@api_view(['GET'])
def lookup(request):
    domain = request.GET.get('domain')
    try:
        ip_address = socket.gethostbyname(domain)
        # Log successful query and result
        QueryHistory.objects.create(domain=domain, ip_address=ip_address)
        return Response({"ip_address": ip_address})
    except socket.gaierror as e:
        return Response({"Error": "domain name does not exist"}, status=400)


# Validate endpoint
@api_view(['GET'])
def validate(request):
    ip_address = request.GET.get('ip_address')
    try:
        # Attempt to validate the IP address
        socket.inet_pton(socket.AF_INET, ip_address)
        return Response({"valid": True})
    except socket.error:
        return Response({"valid": False})


# History endpoint
@api_view(['GET'])
def history(request):
    # Retrieve latest 20 queries from the database
    query_history = QueryHistory.objects.all().order_by('-created_at')[:20]
    serializer = QueryHistorySerializer(query_history, many=True)
    return Response(serializer.data)

