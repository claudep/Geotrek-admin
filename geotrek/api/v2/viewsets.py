from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import viewsets, renderers
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from django.conf import settings

from geotrek.api.v2 import pagination as api_pagination, filters as api_filters
from geotrek.api.v2.serializers import override_serializer


class GeotrekViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend,
                       api_filters.GeotrekQueryParamsFilter,
                       api_filters.GeotrekPublishedFilter)
    pagination_class = api_pagination.StandardResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly, ] if settings.API_IS_PUBLIC else [IsAuthenticated, ]
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    renderer_classes = [renderers.JSONRenderer]

    def get_serializer_context(self):
        return {
            'request': self.request,
            'kwargs': self.kwargs
        }


class GeotrekGeometricViewset(GeotrekViewSet):
    filter_backends = GeotrekViewSet.filter_backends + \
        (api_filters.GeotrekQueryParamsDimensionFilter,
            api_filters.GeotrekInBBoxFilter,
            api_filters.GeotrekDistanceToPointFilter)
    distance_filter_field = 'geometry'
    distance_filter_convert_meters = True
    renderer_classes = viewsets.ReadOnlyModelViewSet.renderer_classes

    def get_serializer_class(self):
        base_serializer_class = super(GeotrekGeometricViewset, self).get_serializer_class()
        format_output = self.request.query_params.get('format', 'json')
        return override_serializer(format_output, base_serializer_class)
