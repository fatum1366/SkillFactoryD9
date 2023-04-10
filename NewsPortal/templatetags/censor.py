from django import template

register = template.Library()

@register.filter()

def censor(text):

    if type(text) == str:

        censored_words = ["редиска", "валенок", "козёл", "козел"]

        for word in censored_words:
            text = text.replace(word, word[0]+'*' * (len(word)-1))

        return text
    else:
        print("TypeError")