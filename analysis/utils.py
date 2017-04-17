import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

newspapers = pd.read_sql_table('newspapers', 'postgres:///frontpages')

def newspaper_for_slug(slug):
    return newspapers[newspapers.slug == slug].title.iloc[0]

def slug_for_newspaper(title):
    return newspapers[newspapers.title == title].slug.iloc[0]

def make_intensity_grid(paper, height, width, verbose=False):
    intensity_grid = np.zeros((height, width))

    for i, row in paper.iterrows():
        left = int(row.bbox_left)
        right = int(row.bbox_right)
        top = int(row.bbox_top)
        bottom = int(row.bbox_bottom)

        if np.count_nonzero(intensity_grid[bottom:top, left:right]) > 0:
            if verbose:
                print('Warning: overlapping bounding box with', bottom, top, left, right)
        intensity_grid[bottom:top, left:right] = row.avg_character_area
    
    return intensity_grid

def plot_intensity(intensity, title, scale=100):
    height, width = intensity.shape
    fig = plt.figure(figsize=(height/scale, width/scale))
    ax = plt.gca()

    cmap = plt.get_cmap('YlOrRd')
    cmap.set_under(color='white')

    fig.suptitle(title)
    plt.imshow(intensity, cmap=cmap, extent=[0, width, 0, height], origin='lower', vmin=0.1)
    plt.close()
    return fig

