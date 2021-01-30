colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black']

vrtx = ['1', '2', '3', '4']

neighbors = {}
neighbors['1'] = ['2', '3']
neighbors['2'] = ['1', '3', '4']
neighbors['3'] = ['1', '2', '4']
neighbors['4'] = ['2', '3']

colors_of_vrtx = {}

def promising(vrtx, color):
    for neighbor in neighbors.get(vrtx): 
        color_of_neighbor = colors_of_vrtx.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True

def get_color_for_vrtx(vrtx):
    for color in colors:
        if promising(vrtx, color):
            return color

def main():
    for vrt in vrtx:
        colors_of_vrtx[vrt] = get_color_for_vrtx(vrt)

    print (colors_of_vrtx)


main()