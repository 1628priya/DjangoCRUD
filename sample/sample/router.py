from newapp.viewsets import InstitueViewset
from rest_framework import routers


router=routers.DefaultRouter()
router.register('institutes',InstitueViewset)

