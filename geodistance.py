# geodistance.py
import math


def geoDistance(loc1, loc2):

    R = 6373.0
    # radius of the Earth
    lat1 = math.radians(loc1[1])
    lon1 = math.radians(loc1[0])
    lat2 = math.radians(loc2[1])
    lon2 = math.radians(loc2[0])

    dlon = lon2 - lon1
    #change in coordinates
    dlat = lat2 - lat1

    a = math.sin(
        dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    # Haversine formula
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return distance
