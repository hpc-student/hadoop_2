from bokeh.io import show, output_file
from bokeh.plotting import figure
import pandas as pd

class data():
    def read(self):

        df=pd.read_csv('new_input', sep=',',header=None)
        df=df.sort_values(by=[7], ascending=False)
        df=df.head()

        X=df[0]

        Y=df[7]

        YY= Y.as_matrix(columns=None)
        XX=X.as_matrix(columns=None)
        fruits=[j for j in XX]
        counts=[int(i) for i in YY]
        p = figure(x_range=fruits, plot_height=350, title="Fruit Counts",toolbar_location=None, tools="")

        p.vbar(x=fruits, top=counts, width=0.9)

        p.xgrid.grid_line_color = None
        p.y_range.start = 0

        #show(p)
        return p
