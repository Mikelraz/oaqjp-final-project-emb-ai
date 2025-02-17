from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detection():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    output = (
        F"For the given statement, the system response is 'anger' : {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']} "
        f"and 'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )

    return output

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
