import matplotlib.pyplot as plt



def show_graph(opt, lon, lat, depth, volcano):
    if opt == 0:
        graph(volcano,lon, lat, "Long_lat", "Longitud", "Latitud", 1, 2)
    elif opt == 1:
        graph(volcano,lon, depth, "Long_prof", "Longitud", "Profundidad (Km)", 1, 3)
    else:
        graph(volcano,lat, depth, "Lat_prof", "Latitud", "Profundidad (Km)", 2, 3)

def graph(volcano, x, y, title, labelx, labely, indx, indy):
    plt.ion()
    colors = {0:'b', 1:'g', 2:'c', 3:'m', 4:'y'}
    fig, ax = plt.subplots()
    fig.canvas.manager.set_window_title(title)
    ax.plot(x, y, 'r.', markersize=1)
    plt.xlabel(labelx)
    plt.ylabel(labely)
    for idx, value in enumerate(volcano):
        ax.plot(value[indx], value[indy], f'{colors[idx]}^', markersize=8, markerfacecolor=f'{colors[idx]}', label=value[0])
    
    if indy == 3:
        ax.axis([(min(x)-0.01), (max(x)+0.01), min(y)-3, max(y)+3])
    else:
        ax.axis([(min(x)-0.01), (max(x)+0.01), min(y)-0.01, max(y)+0.01])

    show_legend(ax, volcano)

def show_legend(ax, volcano):
    if len(volcano) > 0:
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1,
                         box.width, box.height * 0.9])
        legend = ax.legend(loc='upper right', bbox_to_anchor=(0.5, -0.15), ncol=5 , fancybox=True, framealpha=0.5)
    plt.show()