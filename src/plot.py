from motion_detector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")


plot=figure(x_axis_type='datetime',height=200, width=1000,title="Motion Graph")
plot.ygrid[0].ticker.desired_num_ticks=1

# add hover timestamp info 
hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
plot.add_tools(hover)

cds=ColumnDataSource(df)

quad=plot.quad(left="Start",right="End",bottom=0,top=1,color="green",source=cds)

# specify output template
output_file("Graph.html")
# export obtained dataframe to csv
df.to_csv("../timestamps.csv")

# open plot using default browser
show(plot)
