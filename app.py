from flask import Flask, render_template, request
from ultralytics import YOLO
from PIL import Image
import os

from api_call import get_recipe_suggestions
from fruit_counts_file import get_fruit_counts
from create_request import construct_recipe_request
from process_image import create_bounding_box
from my_dict import class_dict

app = Flask(__name__, static_folder="static")

# Load a model
model = YOLO('best_large.pt')
global image_path
global annotated_image_path

image_path = "temp_image.jpg"
annotated_image_path = "static/annotated_image.jpg"
try:
    os.remove(image_path)
    os.remove(annotated_image_path)
except:
    pass
def use_model(image_file, image_path):
    image = Image.open(image_file)
    image.save(image_path)
    results = model.predict(image_path, conf=0.5)
    result = results[0]
    fruit_counts = get_fruit_counts(result, class_dict)
    return result, fruit_counts


@app.route("/", methods=["GET", "POST"])
def index():
    global uploaded_file
    global result
    global fruit_counts
    
    uploaded_file = None  
    fruit_counts = {}
    num_recipe_options =2
    test_bool = True
    
    if request.method == "POST":
        if "file" in request.files:
            uploaded_file = request.files["file"]
            num_recipe_options = int(request.form.get("num_recipe_options"))
            print("num_recipe_options1")
            print(num_recipe_options)
            result, fruit_counts = use_model(uploaded_file, image_path)
        
        if "next_button" in request.form:
            if uploaded_file:
                annotated_image_path = "static/annotated_image.jpg"
                create_bounding_box(image_path, annotated_image_path, result, class_dict)
                print("hello")
                print("num_recipe_options2")
                print(num_recipe_options)
                return render_template("index.html",
                                       fruit_counts=fruit_counts, class_dict= class_dict,
                                       num_recipe_options=num_recipe_options)
        print(test_bool)
        if "update_button" in request.form:
            new_fruit_counts = {}
            num_recipe_options = int(request.form.get("num_recipe_options"))
            for fruit_id, fruit_name in class_dict.items():
                count = request.form.get(f"fruit_counts[{fruit_name}]")
                if count is not None and int(count) > 0:
                    new_fruit_counts[fruit_name] = int(count)
            if new_fruit_counts != fruit_counts:
                test_bool = False
            fruit_counts.update(new_fruit_counts)

            fruit_counts.update(new_fruit_counts)
            print(test_bool)

            print("num_recipe_options3")
            print(num_recipe_options)
        print("num_recipe_options4")
        print(num_recipe_options)
        print(test_bool)
        user_message = construct_recipe_request(fruit_counts, num_recipe_options)
        print(user_message)

  
        recipe_suggestions = get_recipe_suggestions(user_message)
        print(recipe_suggestions)

        
        annotated_image_path = "static/annotated_image.jpg"
        create_bounding_box(image_path, annotated_image_path, result, class_dict)


        if test_bool==False:
            return render_template("index.html",
                               recipe_suggestions=recipe_suggestions)
            
        else:
            return render_template("index.html",
                               recipe_suggestions=recipe_suggestions,
                               annotated_image_path=annotated_image_path)
            
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
