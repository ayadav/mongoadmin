from django.conf.urls.defaults import *
from django.views.generic import RedirectView, TemplateView
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = patterns('mongoadmin',
    url(r'^$', RedirectView.as_view(url='/mongo/connect/')),
    url(r'^mongo/connect/$', login_required(views.ConnectView.as_view())),
    url(r'^mongo/(?P<connection_name>[^/]+)/$',  login_required(views.ConnectionView.as_view())),
    url(r'^mongo/(?P<connection_name>[^/]+)/(?P<database_name>[^/]+)/$',  login_required(views.DatabaseView.as_view())),
    url(r'^mongo/(?P<connection_name>[^/]+)/(?P<database_name>[^/]+)/(?P<collection_name>[^/]+)/$',  login_required(views.CollectionView.as_view())),
    url(r'^mongo/(?P<connection_name>[^/]+)/(?P<database_name>[^/]+)/(?P<collection_name>[^/]+)/add/$',  login_required(views.CreateDocumentView.as_view())),
    url(r'^mongo/(?P<connection_name>[^/]+)/(?P<database_name>[^/]+)/(?P<collection_name>[^/]+)/(?P<pk>[a-z\d]+)/$',  login_required(views.UpdateDocumentView.as_view())),
    url(r'^mongo/(?P<connection_name>[^/]+)/(?P<database_name>[^/]+)/(?P<collection_name>[^/]+)/(?P<pk>[a-z\d]+)/delete/$',  login_required(views.DeleteDocumentView.as_view())),
)
