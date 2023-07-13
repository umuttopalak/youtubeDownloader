import languages.en as en
import languages.tr as tr

def get_translation(selected_language):
    if selected_language == "EN":
        return en.translations
    elif selected_language == "TR":
        return tr.translations
    else:
        return tr.translations 


def on_language_change(languagesMenu, label, btn1):
    selected_language = languagesMenu.get()

    if selected_language == "EN":
        translations = en.translations
    elif selected_language == "TR":
        translations = tr.translations
    else:
        translations = tr.translations 

    label.config(text=translations["label_text"])
    btn1.config(text=translations["button_text"])
    
    return translations