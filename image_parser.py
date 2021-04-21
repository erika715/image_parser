import requests
import urllib
import shutil

def image_pars(search_querry, num_of_images):

    search_querry_encoded = urllib.parse.quote(search_querry)
    image_search_url = "https://google-search3.p.rapidapi.com/api/v1/images/q={}&num={}".format(search_querry_encoded, num_of_images)

    headers = {
        "x-rapidapi-key": "e6684327e4msh73dd35dd09c4df8p1fd427jsnaaee2fcfab3b",
        "x-rapidapi-host": "google-search3.p.rapidapi.com"
    }

    response = requests.request("GET", image_search_url, headers=headers)

    image_links = []

    if response.status_code == 200:
        
        json = response.json()
        image_results = json["image_results"]

        for result in image_results:
            image_link = result["image"]["src"]
            
            image_links.append(image_link)
            
    else:
        print("Bad search request")

    unique_image_links = set(image_links)

    if len(unique_image_links) > 0:
        for link in enumerate(unique_image_links):
            filename = search_querry + str(link[0]) + ".jpg"
            
            image_url = link[1]
            
            image_response = requests.get(image_url, stream = True)
            
            if image_response.status_code == 200:
                image_response.raw.decode_content = True
                
                with open(filename,'wb') as f:
                    shutil.copyfileobj(image_response.raw, f)
            
                print("Image sucessfully Downloaded: ",filename)
            
            else:
                print("Image Couldn\'t be retreived")
            
    else:
        print("Not found any image")
        
image_pars("человек в медицинском халате", 1000)        
        
        
