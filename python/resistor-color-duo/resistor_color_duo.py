# band colors encoding
band_colors = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}

def value(colors):
    # check if the colors array have atleast 2 colors
    if len(colors) < 2:
        raise ValueError(f"Input colors array must have length equal to 2.")

    resistor_value = 10 * band_colors[colors[0]] + band_colors[colors[1]]
    return resistor_value
