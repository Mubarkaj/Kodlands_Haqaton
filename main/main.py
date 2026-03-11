from flask import Flask, render_template, request
import os
import subprocess
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/project", methods=['POST','GET'])
def project():
    if request.method=="POST":
        if not 'image' in request.files:
            return 'No file part'

        image_file = request.files['image']
        if image_file.filename=='':
            return 'No selected file'

        # Ensure the upload directory exists so saving won't raise FileNotFoundError
        os.makedirs("uploads", exist_ok=True)


        filename=image_file.filename

        image_file.save(os.path.join("uploads", filename))
        response = subprocess.run(f"python detector.py -i {os.path.join('uploads',filename)} -o {os.path.join('static','outputs',filename)}",shell=True,capture_output=True,text=True)
        print(response)



        # in main.py, change outputs folder to static/outputs
        os.makedirs("static/outputs", exist_ok=True)


        # and pass just the filename to template
        return render_template("project.html", filename=filename, count=int(response.stdout.strip()))   
    return render_template("project.html", filename='')
    

@app.route("/about")
def about():
        return render_template("about.html")
if __name__=="__main__":
    app.run(debug=True)