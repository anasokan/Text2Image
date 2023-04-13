from flask import Flask, render_template, request
import openai
import json

with open('config.json') as f:
    config = json.load(f)
openai.api_key = config["openai_api_key"]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_image", methods=["POST"])
def generate_image():
    prompt = request.form["prompt"]
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response["data"][0]["url"]
    return render_template("image.html", image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
