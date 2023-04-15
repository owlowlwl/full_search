def get_spn(toponym):
    toponym_coord = toponym["Point"]["pos"]
    longitude, lattitude = toponym_coord.split(" ")
    lower = toponym["boundedBy"]["Envelope"]["lowerCorner"].split()
    return [str(abs(float(longitude) - float(lower[0]))), str(abs(float(lattitude) - float(lower[1])))]
