# Text2Image

Text2Image is a simple web application that uses OpenAI's CLIP model to generate images based on text input.

##Setup

To use this application, follow these steps:

1. Clone the repository:

git clone https://github.com/anasokan/Text2Image

2. Install the required packages:

pip install -r requirements.txt

3. Update the config.json file in the root directory of the project with your OpenAI API key:

{
  "openai_api_key": "your_openai_api_key"
}

4. Start the Flask server:

python app.py

5. Go to http://localhost:5000 in your web browser to use the application.


##Usage
1. Enter a text prompt in the input field and click "Generate Image".
2. Wait for the image to load.
3. Click "Generate Another Image" to generate a new image based on a new prompt.


##Contributing
If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: git checkout -b my-new-feature
3. Make your changes and commit them: git commit -am 'Add some feature'
4. Push to the branch: git push origin my-new-feature
5. Submit a pull request.

##License
This project is licensed under the MIT License
