def keywords_to_list(text_file):
    text_file = open(text_file, 'r')
    keywords = sorted(text_file.read().split(','), key=str.lower)
    return keywords

