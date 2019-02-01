from django import forms




colormaps_choices = (
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
    ('png', 'png'),
    ('jpeg', 'jpeg'),

)

masks = (
            ('nomask.png', 'NO MASK'),
            ('heartbeat.png', 'heartbeat'),
            ('play.png', 'play'),
            ('comment.png', 'comment'),
            ('bicycle.png', 'bicycle'),
            ('area-chart.png', 'area chart'),
            ('bar-chart.png', 'bar chart'),
            ('pie-chart.png', 'pie chart'),
            ('question.png', 'question'),
            ('amazon.png', 'amazon'),
            ('python.png', 'python'),
            ('youtube-square.png', 'you-tube'),
            ('address-book.png', 'address-book'),
            ('address-book-o.png', 'address-book-o'),
            ('address-card.png', 'address-card'),
            ('address-card-o.png', 'address-card-o'),
            ('adjust.png', 'adjust'),
            ('adn.png', 'adn'),
            ('align-center.png', 'align-center'),
            ('align-justify.png', 'align-justify'),
            ('align-left.png', 'align-left'),
            ('align-right.png', 'align-right'),
            ('ambulance.png', 'ambulance'),
            ('android.png', 'android'),
            ('american-sign-language-interpreting.png',     'american-sign-language-interpreting'),
('500px.png', '500px'),


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




class makeit(forms.Form):
    Words = forms.CharField(widget=forms.Textarea(attrs={'class':'jcf-textarea'}), required=True)
    Height = forms.IntegerField(required=False, min_value=1, label="Height")
    Width = forms.IntegerField(required=False, min_value=1)
    Max_words = forms.IntegerField(required=False, min_value=1)
    Max_font_size = forms.IntegerField(required=False, min_value=1)
    Repeat_words = forms.BooleanField(required=False, initial=True)
    Background_color = forms.CharField(widget=ColorWidget(attrs={'class': "jscolor {hash:true}"}))
    Format = forms.ChoiceField(choices=image_format_choices, widget=forms.Select(attrs={'style':'width:100%'}))
    Font_type = forms.ChoiceField(choices=fonts, widget=forms.Select(attrs={'style':'width:100%'}))
    Mask = forms.ChoiceField(choices=masks, widget=forms.Select(attrs={'class':'mask', 'style':'width:100%'}))
    Colormap = forms.ChoiceField(choices=colormaps_choices, widget=forms.Select(attrs={'style':'width:100%'}))

