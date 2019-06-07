CS 180E, May 2019. Final Exam by Jim Zieleman

# Define class
class Airport
    
    # Airport constants
    IATA_LEN = 3
    LAT_EXTREME = 90.0
    LON_EXTREME = 180.0
    
    # Construct our airport
    def __init__(self, code = None, latitude = 0, longitude = 0)
        if code != None and len(code) == Airport.IATA_LEN
            self.code = code
        else
            self.code = None
        
        if abs(latitude)  Airport.LAT_EXTREME
            self.latitude = latitude
        else
            self.latitude = 0
        
        if abs(longitude)  Airport.LON_EXTREME
            self.longitude = longitude
        else
            self.longitude = 0
    
    # See if current Airport is equivalent to another
    def __eq__(self, other)
        if other == None
            return False
        # Find our latitude longitude distances
        lat_diff = round(self.latitude - other.latitude,7)
        long_diff = round(self.longitude - other.longitude,7)
        
        if self.code == other.code and lat_diff == 0 and long_diff == 0
            return True
        return False
    
    def __str__(self)
        return %s @ (%.1f, %.1f) % (self.code, self.latitude, self.longitude)

# Create a list of Airports
def test6_airports()
    airports = [
                Airport('CLT', 35.2, -80.9),
                Airport('IAD', 38.9, -77.4),
                Airport('AUH', 24.4, 54.6),
                Airport('SCY', -0.9, -89.6),
                Airport('ICN', 37.4, 126.4),
                Airport('ZRH', 47.4, 8.5)
                ]
    return airports

# Create a list of Airports from a file
def read_from_file(str)
    infile = open(str)
    airport_strings = infile.readlines()
    infile.close()
    
    airport_list = []
    
    for airport in airport_strings
        airport_data = airport.split()
        airport_list.append(Airport(airport_data[0], float(airport_data[1]), float(airport_data[2])))
        
    return airport_list

# See how many Airports are in each quadrant
def quadrant_count(airports)
    # [NE, NW, SW, SE]
    # [PP, PN, NN, NP]
    count = [0,0,0,0]
    
    if airports == None
        return count
    
    # Count the airports in each quadrant
    for airport in airports
        if airport != None
            # NE Quadrant
            if airport.latitude  0 and airport.longitude  0
                count[0] += 1
            # NW Quadrant    
            elif airport.latitude  0 and airport.longitude  0
                count[1] += 1
            # SW Quadrant
            elif airport.latitude  0 and airport.longitude  0
                count[2] += 1
            # SE Quadrant
            else
                count[3] += 1
          
    return count

# Run if main (Testing code)
if __name__ == __main__
    a1 = Airport('hia',123.0000003, 124.00000001)
    a2 = Airport('hia',123.0000009, 124.00000002)
    print(a1 == a2)
    
    airports = test6_airports()
    print(quadrant_count(airports))
