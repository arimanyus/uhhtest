from django.shortcuts import render, redirect, get_object_or_404
from .models import Site
from .forms import WebsiteForm
from .content_generator import generate_content



def index(request):
    return render(request, 'sites/index.html')


def list_sites(request):
    sites = Site.objects.filter(user=request.user)
    return render(request, 'sites/list.html', {'sites': sites})

def website_form_view(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST, request.FILES)
        if form.is_valid():
            website = form.save(commit=False)
            website.user = request.user

            # Generate content for the website
            industry = form.cleaned_data.get('industry')
            description = form.cleaned_data.get('description')

            about_us_content = generate_content('about_us', industry, description)
            home_content = generate_content('home', industry, description)
            contact_content = generate_content('contact', industry, description)

            # TODO: Use the generated content to populate the website

            website.save()
            return redirect('sites:website_detail', website_id=website.id)
    else:
        form = WebsiteForm()
    return render(request, 'sites/website_form.html', {'form': form})





# def website_form_view(request):
#     if request.method == 'POST':
#         form = WebsiteForm(request.POST, request.FILES)
#         if form.is_valid():
#             website = form.save(commit=False)
#             website.user = request.user
#             website.save()
#             return redirect('sites:website_detail', website_id=website.id)
#     else:
#         form = WebsiteForm()
#     return render(request, 'sites/website_form.html', {'form': form})


def website_detail(request, website_id):
    website = get_object_or_404(Site, id=website_id)
    return render(request, 'sites/website_detail.html', {'website': website})
