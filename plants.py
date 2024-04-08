

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




