# Python3.7.1
# Bokeh Visual Example

import pandas as pd
import numpy as np

from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel


# Set up figures
fig = figure(background_fill_color='yellow',
             background_fill_alpha=0.5,
             border_fill_color='blue',
             border_fill_alpha=0.25,
             plot_height=300,
             plot_width=500,
             h_symmetry=True,
             x_axis_label='X Label',
             x_axis_type='datetime',
             x_axis_location='above',
             x_range=('2018-1-1', '2018-6-30'),
             y_axis_label='Y Label',
             y_axis_type='linear',
             y_axis_location='left',
             y_range=(0, 100),
             title='Example',
             title_location='right',
             toolbar_location='below',
             tools='save')


# Where the visualization will be rendered.
output_file('output_file_test.html',
            title='Bokeh Figure')
output_notebook()  # Render inline in Jupyter Notebook.


# Remove the gridlines from the figure object.
fig.grid.grid_line_color = None

# See what it looks like.
show(fig)
