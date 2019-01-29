from django import forms
from django.conf import settings
from palettable.colorbrewer.diverging import *

diverging_maps_with_color_number = (
    #diverging
    ("BrBG", "BrBG"),
    ("PRGn", "PRGn"),
    ("PiYG", "PiYG"),
    ("PuOr", "PuOr"),
    ("RdBu", "RdBu"),
    ("RdGy", "RdGy"),
    ("RdYlBu", "RdYlBu"),
    ("RdYlGn", "RdYlGn"),
    ("Spectral", "Spectral"),
    ("coolwarm", "coolwarm"),
    ("bwr", "bwr"),
    ("seismic", "seismic"),
    #cyclic
    ("twilight", "twilight"),
    ("twilight_shifted", "twilight_shifted"),
    ("hsv", "hsv"),
    # uniform seq
    ("viridis", "viridis"),
    ("plasma", "plasma"),
    ("inferno", "inferno"),
    ("magma", "magma"),
    ("cividis", "cividis"),
    # seq
    ('Greys', 'Greys'),
    ("Purples", "Purples"),
    ("Blues", "Blues"),
    ("Greens", "Greens"),
    ("Oranges", "Oranges"),
    ("Reds", "Reds"),
    ("YlOrBr", "YlOrBr"),
    ("YlOrRd", "YlOrRd"),
    ("OrRd", "OrRd"),
    ("PuRd", "PuRd"),
    ("RdPu", "RdPu"),
    ("BuPu", "BuPu"),
    ("GnBu", "GnBu"),
    ("PuBu", "PuBu"),
    ("YlGnBu", "YlGnBu"),
    ("PuBuGn", "PuBuGn"),
    ("BuGn", "BuGn"),
    ("YlGn", "YlGn"),
    # seq 2
    ("binary", "binary"),
    ("gist_yarg", "gist_yarg"),
    ("gist_gray", "gist_gray"),
    ("gray", "gray"),
    ("bone", "bone"),
    ("pink", "pink"),
    ("spring", "spring"),
    ("summer", "summer"),
    ("autumn", "autumn"),
    ("winter", "winter"),
    ("cool", "cool"),
    ("Wistia", "Wistia"),
    ("hot", "hot"),
    ("afmhot", "afmhot"),
    ("gist_heat", "gist_heat"),
    ("copper", "copper"),

)


image_format_choices = (
    ('jpeg', 'jpeg'),
    ('png', 'png'),

)

masks = (
            ('None', 'DONT USE MASK'),
            ('heartbeat.png', 'serce'),
            ('play.png', 'play'),
            ('comment.png', 'comment'),
            ('bicycle.png', 'bicycle'),
            ('area-chart.png', 'area chart'),
            ('bar-chart.png', 'bar chart'),
            ('pie-chart.png', 'pie chart'),
            ('question.png', 'question'),
            ('amazon.png', 'amazon'),
            ('python.png', 'python')
)


fonts = (
    ('cmb10.ttf', 'cmb10 - np'),
    ('BPreplay.otf', 'BPreplay - np'),
    ('AlexBrush-Regular.ttf', 'AlexBrush-Regular - np'),
    ('AmaticBold.ttf', 'AmaticBold'),
    ('AmaticSC-Regular.ttf', 'AmaticSC-Regular'),
    ('DejaVuSans.ttf', 'DejaVuSans'),
    ('DejaVuSansMono.ttf', 'DejaVuSansMono'),
    ('DINCondensed-Bold.ttf', 'DINCondensed-Bold - np'),
    ('DroidSansMono.ttf', 'DroidSansMono'),
)

class ColorWidget(forms.TextInput):

    class Media:
        js = ('../static/jscolor.js',)


w = ColorWidget()

#fill validations for fields

class makeit(forms.Form):
    txt = forms.CharField(widget=forms.Textarea(attrs={'style':'resize:none;'}))
    background_color = forms.CharField(widget=ColorWidget(attrs={'class':"jscolor {hash:true}"}))
    figsize_height = forms.IntegerField(required=True)
    figsize_width = forms.IntegerField(required=True)
    image_format = forms.ChoiceField(choices=image_format_choices)
    max_words = forms.IntegerField(required=True)
    repeat_words = forms.BooleanField(required=False)
    max_font_size = forms.IntegerField(required=False)
    font = forms.ChoiceField(choices=fonts)
    mask = forms.ChoiceField(choices=masks, required=False)
    colormap = forms.ChoiceField(choices=diverging_maps_with_color_number)

