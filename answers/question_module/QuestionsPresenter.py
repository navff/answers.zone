from django.http import HttpResponse


class QuestionsPresenter:
    def index(request, name="жопулечка"):
        output = "<h2>User</h2><h3>name: {0}</h3>".format(name)
        return HttpResponse(output)

    def one_item(request, name):
        output = "<h2>Подробка</h2><h3>name: {0}</h3>".format(name)
        return HttpResponse(output)
