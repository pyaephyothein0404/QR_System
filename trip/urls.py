from django.urls import path
from . import views

urlpatterns = [
    
    path('documents/', views.documents_list, name='documents'),
    path('documents/upload/', views.upload_document, name='upload_document'),
    path('documents/delete/<int:pk>/', views.delete_document, name='delete_document'),
    path('documents/<int:pk>/', views.document_detail, name='document_detail'),
    path('documents/qr/<int:pk>/', views.qr_code, name='qr_code'),
    path('detail-plan/', views.detail_plan, name='detail_plan'),
    path('receipt/qr/<int:pk>/', views.receipt_qr_code, name='receipt_qr_code'),
    path('', views.home, name='home'),
    path('qr/home/', views.home_qr_code, name='home_qr_code'),
    path('receipt/', views.receipts, name='receipts'),
    path('receipt/<int:pk>/', views.receipt_detail, name='receipt_detail'),
    path('receipt/upload/', views.upload_receipt, name='upload_receipt'),
    path('receipt/delete/<int:pk>/', views.delete_receipt, name='delete_receipt'),
]

