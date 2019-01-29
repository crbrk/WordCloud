import base64
import urllib
import io
from django.shortcuts import render
from django.views import View
from .forms import makeit
from .generator import draw_a_word_cloud_with_args_from_form


class WordCloudGenerator(View):
    template_name = 'index.html'
    form_class = makeit
    form_initials = {'figsize_height': 5,
                     'figsize_width': 5,
                     'txt': "some were born to win some worn born to lose",
                     'max_words': 100,
                     'repeat_words': True
                     }

    def get(self, request):
        form = self.form_class(initial=self.form_initials)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            figsize_w = form.cleaned_data.get('figsize_width')
            figsize_h = form.cleaned_data.get('figsize_height')
            mask_selection = form.cleaned_data.get('mask')
            max_words = form.cleaned_data.get('max_words')
            max_font_size = form.cleaned_data.get('max_font_size')
            user_color = form.cleaned_data.get('background_color')
            repeat_words = form.cleaned_data.get("repeat_words")
            colormap = form.cleaned_data.get('colormap')
            user_input = form.cleaned_data.get('txt')
            font = form.cleaned_data.get('font')
            image_format = form.cleaned_data.get('image_format')

            wcg = draw_a_word_cloud_with_args_from_form(figsize_w,
                                                        figsize_h,
                                                        mask_selection,
                                                        max_words,
                                                        max_font_size,
                                                        user_color,
                                                        repeat_words,
                                                        colormap,
                                                        user_input,
                                                        font)
            wc = wcg['wc']

            image = wc.to_image()
            buf = io.BytesIO()
            image.save(buf, format=image_format)

            buf.seek(0)
            string = base64.b64encode(buf.read())
            first_half_of_uri = 'data:image/' + image_format + ';base64,'
            uri = first_half_of_uri + urllib.parse.quote(string)

            args = {'form': form, 'imageraster': uri}
            return render(request, self.template_name, args)
