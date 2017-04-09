from collections import Counter

from bs4 import BeautifulSoup
import pandas as pd

def most_common(array):
    return max(Counter(array).items(), key=lambda x: x[1])[0]

def parse_bbox(bbox):
    return [float(x) for x in bbox.split(',')]

def calculate_area(bbox_left, bbox_bottom, bbox_right, bbox_top):
    return (bbox_right - bbox_left) * (bbox_top - bbox_bottom)

def extract_textboxes(soup):
    texts = []
    for page_soup in soup('page'):
        page = page_soup.get('id')
        _, _, page_width, page_height = parse_bbox(page_soup.get('bbox'))
        page_area = page_width * page_height

        for textbox in page_soup('textbox'):
            text = ''.join([x.text for x in textbox('text')])
            fonts = [(x.get('font'), x.get('size')) for x in textbox('text') if x.get('font')]

            if not text or not fonts:
                continue

            text_areas = []
            num_chars = 0
            for text_obj in textbox('text'):
                if not text_obj.get('bbox'):
                    continue
                text_areas.append(calculate_area(*parse_bbox(text_obj.get('bbox'))))
                num_chars += 1

            avg_char_area = sum(text_areas) / (num_chars or 1)

            fontset = most_common(fonts)
            bbox_left, bbox_bottom, bbox_right, bbox_top = parse_bbox(textbox.get('bbox'))
            bbox_area = calculate_area(bbox_left, bbox_bottom, bbox_right, bbox_top)

            percent_of_page = bbox_area / page_area

            texts.append((
                text, fontset[0], float(fontset[1]),
                bbox_left, bbox_bottom, bbox_right,
                bbox_top, bbox_area,
                avg_char_area, percent_of_page,
                page, page_width, page_height, page_area
            ))

    df = pd.DataFrame(texts, columns=[
        'text', 'fontface', 'fontsize', 
        'bbox_left', 'bbox_bottom', 'bbox_right', 
        'bbox_top', 'bbox_area', 
        'avg_character_area', 'percent_of_page',
        'page', 'page_width', 'page_height', 'page_area',
        ])
    return df

if __name__ == '__main__': 
    import sys

    with open(sys.argv[1]) as f:
        soup = BeautifulSoup(f.read(), 'lxml')
        df = extract_textboxes(soup)
    
    print('Extracted {} text boxes.'.format(df.shape[0]))
    print('First five:')
    print(df.head())
