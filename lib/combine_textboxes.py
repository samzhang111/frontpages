from collections import Counter

from bs4 import BeautifulSoup
import pandas as pd

def most_common(array):
    return max(Counter(array).items(), key=lambda x: x[1])[0]

def parse_bbox(bbox):
    return [float(x) for x in bbox.split(',')]

def extract_textboxes(soup):
    texts = []
    for textbox in soup('textbox'):
        text = ''.join([x.text for x in textbox('text')])
        fonts = [(x.get('font'), x.get('size')) for x in textbox('text') if x.get('font')]

        if not text or not fonts:
            continue

        fontset = most_common(fonts)
        texts.append((text, fontset[0], float(fontset[1]), *parse_bbox(textbox.get('bbox'))))
        
    df = pd.DataFrame(texts, columns=['text', 'fontface', 'fontsize', 'bbox_left', 'bbox_bottom', 'bbox_right', 'bbox_top'])
    return df

if __name__ == '__main__': 
    import sys

    with open(sys.argv[1]) as f:
        soup = BeautifulSoup(f.read(), 'lxml')
        df = text_from_textboxes(soup)
    
    print('Extracted {} text boxes.'.format(df.shape[0]))
    print('First five:')
    print(df.head())
