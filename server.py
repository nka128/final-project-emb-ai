''' Executing this function initiates the application of EmotionDetection
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detect():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function.
    '''
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    result = f"For the given statement, the system response is \
    'anger': {response['anger']}, \
    'disgust': {response['anger']}, \
    'fear': {response['fear']}, \
    'joy': {response['joy']}, \
    and 'sadness': {response['sadness']}. \
    The dominant emotion is {response['dominant_emotion']}."

    return result

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
