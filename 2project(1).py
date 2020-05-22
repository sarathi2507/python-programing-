import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

parser =argparse.ArguementParser()
parser.add_arguement("--page_num_MAX", help="enter the number of pages to parse",type=int)
parser.add_arguement("--dbname", help="enter the name of db",type=str)
args = parser.parse_args()


oyo_url="https://www.oyorooms.com/hotels-in-bangalore//?page="
page_num_MAX = 3
scraped_info_list = []
connect.connect(args.dbname)

for page_num in range(1,page_num_MAX):
    url = oyo_url + str(page_num)
    print("GET Request for:" +url)
    req = requests.get(url)
    Content = req.Content

    soup = BeautifulSoup(Content,"html.parser")

    all_hotels = soup.find_all("div", {"class": "hotelcardListing"})

    for hotels in all_hotels:
        hotel_dict ={}
        hotel_dict["name"] = hotel.find("h3", {"class": "ListingHotelDescription__hotelName"}).text
        hotel_dict["address"] = hotel.find("span", {"itemprop": "streetAddress"}).text
        hotel_dict["price"] = hotel.find("span", {"class": "ListingPrice__finalPrice"}).text
        #try... except
        try:
            hotel_dict["rating"] = hotel.find("span", {"class": "HotelRating__ratingSummary"}).text
        except AttributeError:
            pass

        parent_amenities_element = hotel.find("div", {"class": "amenityWrapper"})

        amenities_list =[]
        for amenity in parent_amenities_element.find_all("div", {"class": "amenityWrapper__amenity"}):
            amenities_list.append(amentiy.find("span", {"class": "d-body-sm"}).text,strip())

        hotel_dict["amenities"] = ', '.join(amenities_list[:-1])

        scraped_info_list.append(hotel_dict)

        #print(hotel_name,hotel_address,hotel_price,hotel_rating,amenities_list)

dataFrame = pandas.DataFrame(scraped_info_list)
print("creating csv file...")
dataFrame.to_csv("oyo.csv")
connect.get_hotel_info(args.dbname)
