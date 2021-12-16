from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# search_query = input('Enter search query')
# numberOfImages  = int(input('Number of Images'))

from google_images_download import google_images_download

@app.route('/', methods=['POST'])
def main():
    
    search_query=request.json['search']
    numberOfImages=request.json['number']
    
    response = google_images_download.googleimagesdownload()
    
    # def downloadimages(query):
        
    arguments = {"keywords": search_query,
                "format": "jpg",
                "limit":numberOfImages,
                "print_urls":True,
                "size": "medium",
                "aspect_ratio":"panoramic"}
    # try:
    response.download(arguments)
    return jsonify({'msg': 'Successful'})

        # # Handling File NotFound Error	
        # except FileNotFoundError:
        #     arguments = {"keywords": query,
        #                 "format": "jpg",
        #                 "limit":4,
        #                 "print_urls":True,
        #                 "size": "medium"}
                        
        #     # Providing arguments for the searched query
        #     try:
        #         # Downloading the photos based
        #         # on the given arguments
        #         response.download(arguments)
        #         return 200
        #     except:
        #         pass
        #         return 500

            
    # Driver Code

    # downloadimages(search_query)
    # print()

if __name__ == '__main__':
    app.run(debug=False)
