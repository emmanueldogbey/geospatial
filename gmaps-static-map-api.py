import googlemaps
import configparser

def main():
    api_key = get_apikey()
    map_img = get_mapimage(api_key)
    save_mapimage(map_img)

def get_apikey():
    config = configparser.ConfigParser()
    config.read("file.ini")
    api_key = config["API_KEY"]["api_key"]

    return api_key

def get_mapimage(api_key):
    gmaps = googlemaps.Client(key=api_key)
    size = (640,640)
    location = input("Where would you want to return a map for? ").strip()

    map_img = gmaps.static_map(size, center=location)

    return map_img

def save_mapimage(map_img):
    with open(f"accra_map.jpg", "wb") as file:
        for chunk in map_img:
            file.write(chunk) if chunk else None

if __name__ == "__main__":
    main()