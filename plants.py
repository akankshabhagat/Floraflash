

import requests
from flask import Flask, render_template, jsonify

key = "Your_TREFLE_TOKEN_HERE"
r = requests.get('https://trefle.io/api/v1/species?filter%5Bflower_color%5D=red&token=' + key)
flower_data = r.json()['data']

current_index = 0

plants = Flask(__name__)

@plants.route('/')
def index():
    global current_index
    heading = flower_data[current_index]['common_name']
    flower = flower_data[current_index]['image_url']
    return render_template('index.html', heading=heading, image_url=flower)

@plants.route('/next')
def next():
    global current_index, flower_data
    current_index = (current_index + 1) % len(flower_data)
    flower = flower_data[current_index]['image_url']
    common_name = flower_data[current_index]['common_name']
    return jsonify({'image_url': flower, 'common_name': common_name})

if __name__ == '__main__':
    plants.run(debug=True)




# import requests
# import json
# from flask import Flask, render_template

# key="NNx5gCUuS5viaKORm4xQ_3geyk4J8xE4n0DtKDXPJME"
# r = requests.get('https://trefle.io/api/v1/species?filter%5Bflower_color%5D=red&token='+key)
# # if r.status_code == 200:
#     # Decode the response content from bytes to string



# # response_data = r.content.decode('utf-8')
# # #     # Convert the string to a Python dictionary
# # data_dict = json.loads(response_data)
# #     print(json.dumps(data_dict, indent=4))

# flowername=r.json()['data'][7]['common_name']
# flower=r.json()['data'][7]['image_url']
  
# # print(json.dumps(flower,indent=4))
# plants = Flask(__name__)

# @plants.route('/')
# def index():
#     heading=flowername
    
#    # Replace this with the URL of your image
#     return render_template('index.html',heading=heading,image_url=flower)

# if __name__ == '__main__':
#     plants.run(debug=True)
