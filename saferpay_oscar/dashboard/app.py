from django.conf.urls import url
from oscar.core.loading import get_class
from oscar.core.application import DashboardApplication


class SaferpayDashboardApplication(DashboardApplication):
    name = None
    default_permissions = ['is_staff', ]

    list_view = get_class('saferpay_oscar.dashboard.views', 'TransactionListView')  #views.TransactionListView
    detail_view = get_class('saferpay_oscar.dashboard.views', 'TransactionDetailView')  #views.TransactionDetailView

    def get_urls(self):
        urls = [
            url(r'^transactions/$', self.list_view.as_view(),
                name='saferpay_oscar-transactions-list'),
            url(r'^transactions/(?P<pk>\w+)/$', self.detail_view.as_view(),
                name='saferpay_oscar-transactions-detail'),
        ]
        return self.post_process_urls(urls)


application = SaferpayDashboardApplication()
