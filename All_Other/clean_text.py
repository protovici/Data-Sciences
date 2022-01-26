import re
import string

def clean_text(x):

    '''Make text lowercase, remove text in square brackets,remove links,remove punctuation
    and remove words containing numbers.'''
    
    text = x.lower()
    text = re.sub('\[.*?\]', '', x)
    text = re.sub('https?://\S+|www\.\S+', '', x)
    text = re.sub('<.*?>+', '', x)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', x)
    text = re.sub('\n', '', x)
    text = re.sub('\w*\d\w*', '', x)
    return x