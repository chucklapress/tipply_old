from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView,View,CreateView,ListView
from django.http import HttpResponse
from app.models import EmployeeListing, Employee, WorkSkill
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse



# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'

class LoginView(View):
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/form')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)

        return render(request, "index.html")

def user_create_view(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index_view'))
        else:
            return render(request, "user_create_view.html", {"form": form})
    form = UserCreationForm()
    return render(request, "user_create_view.html", {"form": form})



class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class EmployeeListingCreateView(CreateView):
    model = EmployeeListing
    fields = ['applicant_name','applicant_email','applicant_phone','position_applying_for','post_resume_or_cover']
    success_url = '/'


class ApplicantListView(ListView):
    model = EmployeeListing


class EmployeeListView(ListView):
    model = WorkSkill


class EmployeeWorkSkillCreateView(CreateView):
    model = WorkSkill
    fields = ['employee_number','employee_name','appearence','customer_skills','team_work','adhere_company_policies','accepts_coaching','self_starting']
    success_url = '/'


class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['employee_name','dob','address','telephone_number','federal_and_state_filling_status','department','start_date','recieved_employee_handbook','personel_notes']
    success_url = '/'
