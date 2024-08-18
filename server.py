from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    format_emotions = emotion_detector(text_to_analyze)
    if format_emotions['max_emotion'] is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is 'anger': {format_emotions['anger']}, "
        f"'disgust': {format_emotions['disgust']}, 'fear' : {format_emotions['fear']}, "
        f"'joy': {format_emotions['joy']} and 'sadness': {format_emotions['sadness']}. "
        f"The Dominant emotion is {format_emotions['max_emotion']}."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=5000)