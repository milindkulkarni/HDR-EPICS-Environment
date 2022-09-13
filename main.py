from bokeh.plotting import figure, show 
# install bokeh using conda
from bokeh.models import LogColorMapper
from bokeh.palettes import Viridis6 as palette
from bokeh.sampledata.us_counties import data as counties
from bokeh.sampledata.us_states import data as states_c

import pandas as pd 

df = pd.read_csv(r'C:\Users\nicol\HDR-EPICS\Carson AvgTemp.csv')
print(df)

palette = tuple(reversed(palette))
color_mapper = LogColorMapper(palette=palette)
# Counties dictionary, list of all counties

counties = { 
    code: county for code, county in counties.items() if county['state'] == 'nd'
}

# Find long/lats from each county
county_xs = [county['lons'] for county in counties.values()]
county_ys = [county['lats'] for county in counties.values()]


county_names = [county['name'] for county in counties.values()]

data = dict(
    x = county_xs,
    y = county_ys,
    name=county_names,
)

TOOLS = "pan,wheel_zoom,reset,hover,save"

p = figure(
    title="North Dakota", tools=TOOLS,
    x_axis_location=None,y_axis_location = None,
    tooltips=[
        ("Name", "@name"),  ("Long, Lat)", "($x, $y)")
    ]
)

p.grid.grid_line_color = None
p.hover.point_policy = "follow_mouse"

p.patches("x","y",source=data,fill_color={"field": "rate", "transform":color_mapper},
fill_alpha=0.6, line_color="black", line_width=0.5)

show(p)