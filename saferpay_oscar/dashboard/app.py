from django.conf.urls import url
from django.contrib.admin.views.decorators import staff_member_required
from oscar.core.application import Application

from saferpay_oscar.dashboard import views


class SaferpayDashboardApplication(Application):
    name = None
    list_view = views.TransactionListView
    detail_view = views.TransactionDetailView

    def get_urls(self):
        urlpatterns = [
            url(r'^transactions/$', self.list_view.as_view(),
                name='saferpay_oscar-transactions-list'),
            url(r'^transactions/(?P<pk>\d+)/$', self.detail_view.as_view(),
                name='saferpay_oscar-transactions-detail'),
        ]
        return self.post_process_urls(urlpatterns)

    def get_url_decorator(self, url_name):
        return staff_member_required


application = SaferpayDashboardApplication()
