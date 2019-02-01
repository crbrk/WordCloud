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
    form_initials = {
                     'Words': "Enter\nwords\nnow",
                     }

    def get(self, request):
        form = self.form_class(initial=self.form_initials)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            figsize_w = form.cleaned_data.get('Width')
            figsize_h = form.cleaned_data.get('Height')
            mask_selection = form.cleaned_data.get('Mask')
            max_words = form.cleaned_data.get('Max_words')
            max_font_size = form.cleaned_data.get('Max_font_size')
            user_color = form.cleaned_data.get('Background_color')
            repeat_words = form.cleaned_data.get("Repeat_words")
            colormap = form.cleaned_data.get('Colormap')
            user_input = form.cleaned_data.get('Words')
            font = form.cleaned_data.get('Font_type')
            image_format = form.cleaned_data.get('Format')

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

            args = {'form': form, 'imageraster': uri,}
            return render(request, self.template_name, args)

