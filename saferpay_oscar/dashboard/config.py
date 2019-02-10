from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SaferpayDashboardConfig(AppConfig):
    label = 'saferpay_oscar'
    name = 'saferpay_oscar.dashboard'
    verbose_name = _('Saferpay dashboard')
