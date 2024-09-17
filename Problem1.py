def display_itineraries(itineraries):
    for index, itinerary in enumerate(itineraries, start=1):
        traveler, destinations = itinerary[0], itinerary[1:]
        print(f"Itinerary {index}: {traveler} - From {destinations[0]} to {destinations[1]}")



def main():
    itineraries = ([("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")])
    display_itineraries(itineraries)

if __name__ == "__main__":
    main()