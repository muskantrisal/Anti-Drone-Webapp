from flask import Flask,render_template,url_for,request
import pandas as pd 
import joblib
from werkzeug.utils import secure_filename
import shutil, os
from yolo_video import predictV
from aviTowebm import avi2webm
import time
# load the model from disk
#filename = 'nlp_model.pkl'
#clf = pickle.load(open(filename, 'rb'))
#cv=pickle.load(open('tranform.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	if request.method == 'POST':
		dir = 'static'
		for f in os.listdir(dir):
			if f != '5668.jpg':
				os.remove(os.path.join(dir, f))
		f = request.files['video_file']
		f.save(secure_filename(f.filename))
		f1 = [secure_filename(f.filename)]	
		for _ in f1:
			shutil.move(_, 'static')
		pa = 'static'+'/' + f1[0]
		args = {'input': pa, 'output': 'static/output.avi', 'yolo': 'yolo-coco', 'confidence': 0.5, 'threshold': 0.4}
		time.sleep(1)
		predictV(args)
		avi2webm('static/output.avi')
	return render_template('result.html')



if __name__ == '__main__':
	app.run(debug=True)