from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from youtubeadl.apps.downloader.views import DownloadFormView


admin.site.site_header = 'YouTube ADL Admin'
admin.site.site_title = 'YouTube ADL Admin'


urlpatterns = [
    url(r'^$', DownloadFormView.as_view(), name='home'),
    url(r'^downloader/', include('youtubeadl.apps.downloader.urls')),

    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
    # Serve media files during development.
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
