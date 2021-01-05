from django.urls import path
from sender.views import handle_send

app_name = 'sender'

urlpatterns = {
    path('', handle_send, name='handle_send')
}