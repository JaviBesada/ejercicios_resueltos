def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
        if c == "<" and not quote:
            tag = True
        elif c == ">" and not quote:  #Final del marcador
            tag = False
        elif c == '"' or c == "'" and tag:
            quote = not quote
        elif not tag:
            out = out + c
        else:
            pass

    return out




if __name__ == "__main__":

    print(remove_html_markup('<a href=">">foot</a>')) 
    print(remove_html_markup("<b>foot</b>"))
    print(remove_html_markup('"<b>foot</b>"'))
    print(remove_html_markup('<b>"foot"</b>'))
    print(remove_html_markup('<"b">foot</"b">'))