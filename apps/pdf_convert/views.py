from django.shortcuts import render
from apps.post.models import Post
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def show_posts(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'pdf_converter/info.html', context)



def pdf_report_create(request):
    posts = Post.objects.all()

    template_path = 'pdf_converter/pdfReport.html'

    context = {'posts': posts}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="pots_report.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
