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
    # uniform seq
    ("viridis", "viridis"),
    ("plasma", "plasma"),
    ("inferno", "inferno"),
    ("magma", "magma"),
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
            ('smile-o.png', 'smile-o'),
            ('js.png', 'js'),
            ('django.png', 'django'),
            ("exclamation-circle.png", "exclamation-circle"),
            ("handshake-o.png", "handshake-o"),
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
            ('anchor.png', 'anchor'),
            ('angellist.png', 'angellist'),
            ('angle-double-down.png', 'angle-double-down'),
            ('angle-double-left.png', 'angle-double-left'),
            ('angle-double-right.png', 'angle-double-right'),
            ('angle-double-up.png', 'angle-double-up'),
            ('angle-down.png', 'angle-down'),
            ('angle-left.png', 'angle-left'),
            ('angle-right.png', 'angle-right'),
            ('angle-up.png', 'angle-up'),
            ('apple.png', 'apple'),
            ('archive.png', 'archive'),
            ('arrow-circle-down.png', 'arrow-circle-down'),
            ('arrow-circle-left.png', 'arrow-circle-left'),
            ('arrow-circle-o-down.png', 'arrow-circle-o-down'),

)


fonts = (
    ('AmaticBold.ttf', 'AmaticBold'),
    ('AmaticSC-Regular.ttf', 'AmaticSC-Regular'),
    ('DejaVuSans.ttf', 'DejaVuSans'),
    ('DejaVuSansCondensed-Bold.ttf', 'DejaVuSansCondensed-Bold'),
    ('DroidSansMono.ttf', 'DroidSansMono'),
    ('Heuristica-Regular.otf', "Heuristica-Regular"),
    ('Heuristica-Bold.otf', 'Heuristica-Bold'),
    ('KaushanScript-Regular.otf', 'KaushanScript-Regular'),
    ('LinBiolinum_R.otf', 'LinBiolinum_R'),
    ('LinBiolinum_RB.otf', 'LinBiolinum_RB'),
    ('PlayfairDisplay-Regular.otf', 'PlayfairDisplay-Regular'),
    ('PlayfairDisplay-Italic.otf', 'PlayfairDisplay-Italic'),
    ('PlayfairDisplay-Bold.otf', 'PlayfairDisplay-Bold'),
    ('PlayfairDisplay-Black.otf', 'PlayfairDisplay-Black')

)

class ColorWidget(forms.TextInput):

    class Media:
        js = ('../static/jscolor.js',)




class makeit(forms.Form):
    Words = forms.CharField(widget=forms.Textarea(attrs={'class':'jcf-textarea', 'style':'resize:none', 'rows':4, 'cols':15}), required=True)
    Height = forms.IntegerField(required=False, min_value=1, label="Height")
    Width = forms.IntegerField(required=False, min_value=1)
    Max_words = forms.IntegerField(required=False, min_value=1)
    Max_font_size = forms.IntegerField(required=False, min_value=1)
    Repeat_words = forms.BooleanField(required=False, initial=True)
    Background_color = forms.CharField(widget=ColorWidget(attrs={'class': "jscolor {hash:true}"}))
    Format = forms.ChoiceField(choices=image_format_choices, widget=forms.Select(attrs={'style':'width:100%'}))
    Font_type = forms.ChoiceField(choices=fonts, widget=forms.Select(attrs={'class':'fonts','style':'width:100%'}))
    Mask = forms.ChoiceField(choices=masks, widget=forms.Select(attrs={'class':'mask', 'style':'width:100%'}))
    Colormap = forms.ChoiceField(choices=colormaps_choices, widget=forms.Select(attrs={'class':'colormaps','style':'width:100%'}))

