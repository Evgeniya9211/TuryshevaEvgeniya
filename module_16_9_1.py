class AnyFigures:
    def __init__(self, figure_name=""):
        self.figure_name = figure_name

    def init_from_dict(self, figure_dict):
        if(figure_dict.get("figure") == "Rectangle"):
            self.x = figure_dict.get("x")
            self.y = figure_dict.get("y")
            self.width = figure_dict.get("width")
            self.height = figure_dict.get("height")
        elif(figure_dict.get("figure") == "Circle"):
            self.x = figure_dict.get("x")
            self.y = figure_dict.get("y")
            self.radius = figure_dict.get("radius")
        else:
            self.x = figure_dict.get("x")
            self.y = figure_dict.get("y")
            self.length = figure_dict.get("length")

    def prnt_attribute(self, figure_dict):
        if (figure_dict.get("figure") == "Rectangle"):
            print('{data[figure]}({data[x]}, {data[y]}, {data[width]}, {data[height]})'.format(data=figure_dict))
        elif (figure_dict.get("figure") == "Circle"):
            print('{data[figure]}({data[x]}, {data[y]}, {data[radius]})'.format(data=figure_dict))
        else:
            print('{data[figure]}({data[x]}, {data[y]}, {data[length]})'.format(data=figure_dict))


figures = [{"figure": "Rectangle", "x": 5, "y": 2, "width": 50, "height": 100},
           {"figure": "Circle", "x": 10, "y": 20, "radius": 7},
           {"figure": "Square", "x": 8, "y": 16, "length": 15}]

for figure in figures:
    figure_obj = AnyFigures()
    figure_obj.init_from_dict(figure)
    figure_obj.prnt_attribute(figure)

