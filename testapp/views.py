from django.http import HttpResponse, HttpRequest

# Create your views here.
def greetings(request: HttpRequest) -> HttpResponse:
    return HttpResponse("HELLO FROM MY  APP!!!!")


def user_greeting(request, user):
    return HttpResponse(f"HELLO {user}")
