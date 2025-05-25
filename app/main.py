from flask import Flask, render_template, request
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    image_data = ""
    if request.method == "POST":
        if "textinput" in request.form and request.form["textinput"]:
            text = request.form["textinput"]
            result = text.upper()  # einfache Textverarbeitung
        elif "imageinput" in request.files and request.files["imageinput"]:
            image_file = request.files["imageinput"]
            img = Image.open(image_file.stream).convert("L")  # Graustufen
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            image_data = base64.b64encode(buf.getvalue()).decode("utf-8")
    return render_template("index.html", result=result, image_data=image_data)

if __name__ == "__main__":
    app.run(debug=True)
