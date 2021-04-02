
def set_styles_fig(fig):
    fig.patch.set_facecolor(background_color())
    return fig
    
def set_styles_ax(ax):
    ax.set_facecolor(background_color())
    ax.spines['bottom'].set_color(axis_color())
    ax.spines['left'].set_color(axis_color())
    ax.xaxis.label.set_color(axis_color())
    ax.tick_params(axis='x', colors=axis_color())
    ax.yaxis.label.set_color(axis_color())
    ax.tick_params(axis='y', colors=axis_color())
    return ax

def background_color(background_color='xkcd:black'):
    return background_color

def axis_color(axis_color='xkcd:light blue'):
    return axis_color

def label_color(label_color='xkcd:white'):
    return label_color

def signature_color(signature_color='xkcd:light blue'):
    return signature_color

def annotation_color(annotation_color='xkcd:light gray'):
    return annotation_color