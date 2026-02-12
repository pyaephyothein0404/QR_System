from django.shortcuts import render, redirect, get_object_or_404
from .models import Document
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
import qrcode
from io import BytesIO
from .models import Receipt
from django.db import IntegrityError


def home(request):
    return render(request, 'home.html')


def is_superuser(user):
    return user.is_superuser

@login_required
def documents_list(request):
    documents = Document.objects.all()
    return render(request, 'trip/documents.html', {'documents': documents})

@login_required
@user_passes_test(is_superuser)
def upload_document(request):
    if request.method == 'POST':
        number = request.POST['number']
        qr_number = request.POST['qr_number']
        description = request.POST['description']
        file = request.FILES['file']
        Document.objects.create(number=number, qr_number=qr_number, description=description, file=file)
        return redirect('documents')
    return render(request, 'trip/upload_document.html')

@login_required
@user_passes_test(is_superuser)
def delete_document(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    doc.delete()
    return redirect('documents')

@login_required
def document_detail(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    return render(request, 'trip/document_detail.html', {'doc': doc})

def home(request):
    return render(request, 'home.html')

def qr_code(request, pk):
    doc = get_object_or_404(Document, pk=pk)
    url = request.build_absolute_uri(f'/documents/{doc.pk}/')
    img = qrcode.make(url)
    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()
    return HttpResponse(image_stream, content_type="image/png")


@login_required
def detail_plan(request):
    return render(request, 'trip/detail_plan.html')



@login_required
def home_qr_code(request):
    # Generate a QR code for the home page URL
    url = request.build_absolute_uri('/')  # This will be your home page URL
    img = qrcode.make(url)
    response = HttpResponse(content_type="image/png")
    img.save(response, "PNG")
    return response

@login_required
def receipts(request):
    receipts = Receipt.objects.all()
    return render(request, 'trip/receipts.html', {'receipts': receipts})

@login_required
def receipt_detail(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    return render(request, 'trip/receipt_detail.html', {'receipt': receipt})



@login_required
def upload_receipt(request):
    error = None
    if request.method == 'POST':
        number = request.POST.get('number')
        qr_number = request.POST.get('qr_number')
        description = request.POST.get('description')
        file = request.FILES.get('file')
        if number and qr_number and file:
            try:
                Receipt.objects.create(
                    number=number,
                    qr_number=qr_number,
                    description=description,
                    file=file
                )
                return redirect('receipts')
            except IntegrityError:
                error = "QR Number already exists. Please use a unique QR Number."
    return render(request, 'trip/upload_receipt.html', {'error': error})

@login_required
def receipt_qr_code(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    url = request.build_absolute_uri(f'/receipt/{receipt.pk}/')
    img = qrcode.make(url)
    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()
    return HttpResponse(image_stream, content_type="image/png")

@login_required
def delete_receipt(request, pk):
    receipt = get_object_or_404(Receipt, pk=pk)
    receipt.delete()
    return redirect('receipts')