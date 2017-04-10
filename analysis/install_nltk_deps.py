import nltk
import ssl

# http://stackoverflow.com/questions/41348621/ssl-error-downloading-nltk-data
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('punkt')
nltk.download('brown')
