from django.views import generic
from saferpay.models import SaferpayTransaction


class TransactionListView(generic.ListView):
    model = SaferpayTransaction
    template_name = 'saferpay_oscar/dashboard/transaction_list.html'
    context_object_name = 'transactions'


class TransactionDetailView(generic.DetailView):
    model = SaferpayTransaction
    template_name = 'saferpay_oscar/dashboard/transaction_detail.html'
    context_object_name = 'transaction'
