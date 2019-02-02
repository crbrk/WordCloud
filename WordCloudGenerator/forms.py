from django import forms
import os



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

def traverse_masks_static():
    mother_of_all_tuples = []
    just_read_the_file_names = os.scandir('static/masks')
    dirEntries = []
    for dirEntry in just_read_the_file_names:
        dirEntries.append(dirEntry)

    mask_file_names = []
    for file in dirEntries:
        mask_file_names.append(file.name)
    mask_file_names.sort()

    dropdown_values = []
    for file in mask_file_names:
        dropdown_values.append(file.split('.png')[0])

    for png, not_png in zip(mask_file_names, dropdown_values):
        mother_of_all_tuples.append((str(png), str(not_png)))

    mother_of_all_tuples = tuple(mother_of_all_tuples)
    return mother_of_all_tuples


traverse_masks_static()

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
    Mask = forms.ChoiceField(choices=traverse_masks_static(), widget=forms.Select(attrs={'class':'mask', 'style':'width:100%'}))
    Colormap = forms.ChoiceField(choices=colormaps_choices, widget=forms.Select(attrs={'class':'colormaps','style':'width:100%'}))

