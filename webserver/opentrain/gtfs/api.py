from tastypie.resources import ModelResource
from tastypie import fields
import models

class AgencyResource(ModelResource):
    class Meta:
        queryset = models.Agency.objects.all()
        resource_name = 'agencies'

class RouteResource(ModelResource):
    agency = fields.ForeignKey(AgencyResource, 'agency',full=True)
    class Meta:
        queryset = models.Route.objects.all()
        resource_name = 'routes'

class ServiceResource(ModelResource):
    class Meta:
        queryset = models.Service.objects.all()
        resource_name = 'services'
        
class TripResource(ModelResource):
    route = fields.ForeignKey(RouteResource,'route',full=True)
    service = fields.ForeignKey(ServiceResource,'service',full=True)
    class Meta:
        queryset = models.Trip.objects.all()
        resource_name = 'trips'
        
        
class StopTimeResource(ModelResource):
    class Meta:
        queryset = models.StopTime.objects.all()
        resource_name = 'stop-times'
        
class StopResource(ModelResource):
    class Meta:
        queryset = models.Stop.objects.all()
        resource_name = 'stops'
        
class ShapeResource(ModelResource):
    class Meta:
        queryset = models.Shape.objects.all()
        resource_name = 'shapes'
        
def register_all(tp):
    tp.register(AgencyResource())
    tp.register(RouteResource())
    tp.register(TripResource())
    tp.register(ServiceResource())
    tp.register(StopTimeResource())
    tp.register(StopResource())
    tp.register(ShapeResource())
    
    