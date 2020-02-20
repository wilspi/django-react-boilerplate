from django.urls import path, re_path
from myapplication import views

urlpatterns = [
    # frontend
    path("", views.index, name="index"),
    # apis
    path("api/v1/test", views.test_api),
    # re_path(
    #     "api/v1/myapplication/(?P<name>[a-zA-Z][a-zA-Z0-9\_]?)/(?P<version>\d+\.\d+)$",
    #     views.my_view,
    # ),
]

# # https://stackoverflow.com/a/21805592
# urlpatterns += patterns(
#     #'django.contrib.staticfiles.views',
#     url(r'^(?:index.html)?$', 'serve', kwargs={'path': 'index.html'}),
#     #url(r'^(?P<path>(?:js|css|img)/.*)$', 'serve'),
# )
