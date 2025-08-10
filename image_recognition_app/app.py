from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from utils.preprocess import prepare_image
import os
import uuid

app = Flask(__name__)
model=load_model("model/mnist_model.h5")
upload_folder = 'static/uploads'
os.makedirs(upload_folder, exist_ok=True)

@app.route('/',methods=['GET', 'POST'])
def index():
    prediction = None
    img_path = None

    if request.method == 'POST':
        file= request.files['file']
        if file:
            img_filename = f"{uuid.uuid4().hex}.png"
            img_path = os.path.join(upload_folder, img_filename)
            file.save(img_path)

            img_array = prepare_image(img_path)
            pred=model.predict(img_array)
            prediction=str(pred.argmax())
    
    return render_template('index.html', prediction=prediction, img_path=img_path)


if __name__ == '__main__':
    app.run(debug=True)

