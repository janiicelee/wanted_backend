import json
from .models      import *
from user.models  import User 
from django.http  import JsonResponse
from django.views import View 


class CategoryView(View):
    def get(self, request):
        try:
            categories = list(
                Category.objects.values('id','title'))
            return JsonResponse({'Category':categories}, status = 200)
        except:
            return JsonResponse({'message': 'ERROR'}, status = 400)

class CompanyView(View):
    def get(self, request):
        companies = list(Company.objects.all())
        company_list = [{
            'name' : company.name,
            'image' : company.image,
        }for company in companies]

        return JsonResponse({'data': company_list}, status = 200)

class JobPostsView(View):
    def get(self, request):
        jobposts = JobPosting.objects.prefetch_related('company','category','sub_category')
        like = JobUser.objects.all().filter(title_id = title_id)
        print(like)

        jobposts_list = list[{
            'company': jobposts.company.name,
            'image' : jobposts.company.image,
            'tag' : jobposts.company.tag,
            'category': jobposts.category.title,
            'sub_category':jobposts.category.sub_category,
            'details': jobposts.details,
                #'like': like.
        }] #syntax error

        return JsonResponse({'data': jobposts_list}, status = 200)
