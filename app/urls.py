from django.urls import path, include
from .views import add_show,delete_data,update_data,getcookie,setcookie,delcookie

urlpatterns = [
    path('',add_show,name="addandshow"),
    path('delete/<int:id>/',delete_data,name="delete"),
    path('<int:id>',update_data,name="update"),
    path('set/',setcookie,name="setcookie"),
    path('get/',getcookie,name="getcookie"),
    path('delete/',delcookie,name="delcookie"),
    path('api/', include('app.api.urls'))
]