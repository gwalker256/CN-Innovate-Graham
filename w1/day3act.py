print ("hello")

# countries = {"United Kingdom":"London", "France": "Paris", "Germany": "Berlin", "Spain": "Madrid","Italy": "Rome"}
# countries.setdefault("Ireland", "Dublin")
# countries.setdefault("Portugal", "Lisbon")

# print(countries)

# countries["United Kingdom"] = "English"

# print(countries)

fav_songs = [
    {"artist" : "", "song_name" : "","genre" : "", "release_year" : ""},
    {"artist" : "", "song_name" : "","genre" : "", "release_year" : ""},
    {"artist" : "", "song_name" : "","genre" : "", "release_year" : ""},
    {"artist" : "", "song_name" : "","genre" : "", "release_year" : ""}
]

fav_songs[0]["artist"]="Radiohead"

print (fav_songs)

fav_songs[0]["artist"]="Blur"

print (fav_songs)

fav_songs.pop(0)

print (fav_songs)

fav_songs.append({"artist" : "", "song_name" : "","genre" : "", "release_year" : ""})

print (fav_songs)

# print(complex_dict["one"]["name"])

# complex_dict = {
#     "one" : {
#     "name": "Will",
#     "age": 31,
#     "instructor": True
# }, "two" : {
#     "name": "Jay",
#     "age": "30",
#     "instructor": True
# }}

# print(complex_dict["one"]["name"])

# countries = {
#     "UK" : {
#     "name": "United Kingdom",
#     "capital": "London"
    
#     }, "FR" : {
#         "name": "France",
#         "capital": "Paris"
#     }, "UK" : {
#         "name": "United Kingdom",
#         "capital": "London"
#     }, "GE" : {
#         "name": "Germany",
#         "capital": "Berlin"
#     }, "SP" : {
#         "name": "Spain",
#         "capital": "Madrid"
#         }, "IT" : {
#         "name": "Italy",
#         "capital": "Rome"
# }
# }