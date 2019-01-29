import os
from PIL import Image
import numpy as np
from django.conf import settings
from wordcloud import WordCloud


base_dir = settings.BASE_DIR


def resolve_font_path(tmp_font):
    FONT_PATH = os.path.join(str(base_dir) + "/static/fonts/" + str(tmp_font))
    return FONT_PATH


def resolve_mask(tmp_mask_selection):
    if tmp_mask_selection == 'None':
        mask2 = None
    else:
        MASK_PATH = os.path.join(str(base_dir) + "/static/masks/" + str(tmp_mask_selection))
        mask = Image.open(MASK_PATH)
        mask2 = Image.new("RGB", mask.size, (255, 255, 255))
        mask2.paste(mask, mask)
        mask2 = np.array(mask2)
    return mask2


def what_to_do_with_font_size(tmp_max_font_size,
                              tmp_mask_selection,
                              tmp_figsize_h,
                              hardcoded_dpi=100):

    check_sent_font = False if tmp_max_font_size is None else True
    check_mask2 = False if resolve_mask(tmp_mask_selection) is None else True
    checker = [check_sent_font, check_mask2]

    if checker == [False, True]:
        return resolve_mask(tmp_mask_selection).shape[0]
    elif checker == [False, False]:
        return tmp_figsize_h * hardcoded_dpi
    elif checker == [True, True]:
        return tmp_max_font_size
    elif checker == [True, False]:
        return tmp_max_font_size


def draw_a_word_cloud_with_args_from_form(tmp_figsize_w,
                                          tmp_figsize_h,
                                          tmp_mask_selection,
                                          tmp_max_words,
                                          tmp_max_font_size,
                                          tmp_user_color,
                                          tmp_repeat_words,
                                          tmp_colormap,
                                          tmp_user_input,
                                          tmp_font,
                                          hardcoded_dpi=100):

    wc = WordCloud(height=tmp_figsize_h * hardcoded_dpi if resolve_mask(tmp_mask_selection) is None else None,
                   width=tmp_figsize_w * hardcoded_dpi if resolve_mask(tmp_mask_selection) is None else None,
                   scale=1,
                   max_words=tmp_max_words,
                   max_font_size=what_to_do_with_font_size(tmp_max_font_size,
                                                           tmp_mask_selection,
                                                           tmp_figsize_h,),
                   font_path=resolve_font_path(tmp_font),
                   background_color=tmp_user_color,
                   repeat=tmp_repeat_words,
                   mask=resolve_mask(tmp_mask_selection),
                   colormap=tmp_colormap
                   ).generate(tmp_user_input)

    print(wc)
    return {"wc": wc}
