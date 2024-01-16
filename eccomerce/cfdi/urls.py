from django.urls import path

from cfdi.views import CreateCfdiCollection, CfdiView


urlpatterns = [
	path('cfdiRequest/', CreateCfdiCollection.as_view()),
	path('cfdiList/', CfdiView.as_view())
]