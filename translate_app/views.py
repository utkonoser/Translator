from .models import TranslateModel
from django.views.generic import CreateView,ListView,DetailView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import TranslateForm
from translate import Translator
# Create your views here.

class HomeView(CreateView):
    model = TranslateModel
    fields = "__all__"
    success_url = reverse_lazy('translate_app:history')

    def post(self, request):
        if request.POST:
            form = TranslateForm(request.POST)
            if form.is_valid():
                from_lang = form.cleaned_data['language_to_translate']
                to_lang = form.cleaned_data['language_to_be_translated']
                text = form.cleaned_data['text_to_translate']
                trans = Translator(from_lang=from_lang,to_lang=to_lang)
                new_text = text
                i,translation = 500,''
                while new_text:              
                    translation += trans.translate(new_text[:i])
                    new_text = new_text[500:]
                TranslateModel.objects.create(
                    language_to_translate = from_lang,
                    language_to_be_translated = to_lang,
                    text_to_translate = text,
                    translated_text = translation
                )
                pk = max(TranslateModel.objects.all().values_list('id',flat=True))
                return redirect('translate_app:detail',pk=pk)

    


class TranslateListView(ListView):
    model = TranslateModel
    context_object_name = 'translated_list'


class TranslateDetailView(DetailView):
    model = TranslateModel
