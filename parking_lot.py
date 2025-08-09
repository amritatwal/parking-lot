import itertools

class Level:
    """
    Represents a single level within a parking lot.
    """
    def __init__(self, number):
        # Nice-to-have: add a flag to easily keep track of whether a level is full or not 
        # self.isFull = False
        self.level = number
         
class Spot:
    """
    Represents a single parking spot within a level.
    """
    new_id = itertools.count(1)
    def __init__(self, spotType):
        self.id = next(self.new_id)
        self.type = spotType
        self.isEmpty = True
        self.vehicleId = None

class ParkingMap:
    """
    Represents a single parking lot map. 
    """
    def __init__(self):
        self.map = {}

    def add_level(self, levelNumber):
        """
        Adds a new level to the parking map.
        """
        self.map[levelNumber] = []

    def add_spot(self, levelNumber, spotType):
        """
        Adds a new spot to a level.
        """
        if levelNumber not in self.map:
            print("This level does not exist.")
            return 
        
        new_spot = Spot(spotType)
        self.map[levelNumber].append(new_spot)

    def show_map(self):
        """
        Prints current state of parking map.
        """
        for level, spots in self.map.items():
            print("Level: ", level)
            if (not spots):
                print('No spots')
            for spot in spots:
                print("Spot: ", spot.__dict__)

class Vehicle:
    """
    Represents a vehicle.
    """
    new_id = itertools.count(1)
    def __init__(self, vehicleType):
        self.id = next(self.new_id)
        self.type = vehicleType.upper()

class ParkingLot:
    """
    Represents a parking lot.
    """
    def __init__(self, parking_lot_map):
        self.parking_lot = parking_lot_map
        # Nice-to-have: add a flag to easily keep track of whether a lot is full or not 
        # self.isFull = False 

    def add_vehicle_to_spot(self, level, spot, vehicle):
        """
        Add vehicle to a given spot 
        """
        spot.vehicleId = vehicle.id 
        spot.isEmpty = False
        print(f"Parked vehicle {vehicle.id} in level: {level}, spot: {spot.id}")
 
    def park_vehicle(self, vehicle):
        """
        Find a spot for given vehicle, add vehicle to spot if one found 
        """   
        if (not self.parking_lot.map):
            return 
        # Nice-to-have: using flag, check if parking lot is full before proceeding
        # if self.isFull: 
        #     print('Sorry, the car park is full.')
        #     return
        
        for level, spots in self.parking_lot.map.items():
            # Nice-to-have: using flag, check if level is full before looking through spots
            # if level.isFull: 
            #     continue
            
            for spot in spots:
                if spot.isEmpty == False:
                    continue
                elif spot.type != "CAR" and vehicle.type == "CAR":
                    continue
                else:
                    self.add_vehicle_to_spot(level, spot, vehicle)
                    return
                
        print(f"Couldn't find a spot for vehicle {vehicle.id} of type {vehicle.type}.")
  
    def unpark_vehicle(self, vehicle):
        """
        Unpark a vehicle from spot 
        """ 
        for spots in self.parking_lot.map.values():
            for spot in spots:
                if spot.vehicleId == vehicle.id:
                    self.remove_vehicle(spot, vehicle)
                    return 

        print("Couldn't find this vehicle in our parking lot.")

    def find_vehicle(self, vehicle):
        """
        Finds a vehicle in the parking lot
        """
        for level, spots in self.parking_lot.map.items():
            for spot in spots:
                if spot.vehicleId == vehicle.id:
                    print(f"Vehicle {vehicle.id} is in level: {level}, spot: {spot.id}")
                    return
        
        print("Couldn't find this vehicle in our parking lot.")

    def remove_vehicle(self, spot, vehicle):
        """
        Removes vehicle from given spot 
        """
        spot.vehicleId = None
        spot.isEmpty = True
        print(f"Un-parked {vehicle.id} from {spot}")
    
    def display_parking_lot(self):
        """
        Prints current state of parking lot
        """
        self.parking_lot.show_map()

# Example - initialise a parking lot map 
parking_lot_map = ParkingMap()
parking_lot_map.add_level(1)
parking_lot_map.add_spot(1, "CAR")
parking_lot_map.add_spot(1, "CAR")

parking_lot_map.add_level(2)
parking_lot_map.add_spot(2, "MOTORCYCLE")
parking_lot_map.add_level(3)
parking_lot_map.show_map()

# Example - initialise the parking lot, parking and un-parking vehicles
parking_lot = ParkingLot(parking_lot_map)

# Park, unpark successfully
my_vehicle = Vehicle("CAR")
parking_lot.park_vehicle(my_vehicle)
parking_lot.find_vehicle(my_vehicle)

# Park, unpark successfully
my_motorcycle = Vehicle("MOTORCYCLE")
parking_lot.park_vehicle(my_motorcycle)
parking_lot.find_vehicle(my_motorcycle)

# Park unsuccessfully (no more car spots)
my_other_vehicle = Vehicle("CAR")
parking_lot.park_vehicle(my_other_vehicle)
