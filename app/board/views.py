from django.contrib.auth import logout
from django.http import HttpRequest, HttpResponseRedirect
from django.views.generic import FormView, RedirectView

from .forms import SubmitForm
from .models import Submission


def get_client_ip(request: HttpRequest) -> str:
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class Index(FormView):
    template_name = 'board/index.html'
    form_class = SubmitForm
    success_url = '/'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['entries'] = Submission.objects.filter(state__exact=Submission.State.ACCEPTED).order_by('time')
        return context

    def form_valid(self, form) -> HttpResponseRedirect:
        print(form.cleaned_data)
        submission: Submission = form.save(commit=False)
        submission.ip = get_client_ip(self.request)

        submission.save()
        return super().form_valid(form)


class LogoutView(RedirectView):
    permanent = False
    pattern_name = 'index'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super().get_redirect_url(*args, **kwargs)
