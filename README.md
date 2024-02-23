# Fruit Pantry Assistant

Introducing the Fruit Pantry Assistant—an innovative application designed to enhance your culinary exploration. With the power of YOLOv8, our custom-trained model, at your fingertips, the contents of your pantry and fruit bowl take center stage.

Here's how it works: Upload an image, and our YOLOv8 model steps in to identify the diverse range of fruits at your disposal. To ensure precision, the detections can be refined, putting you in control of the process. Alternatively, bypass the editing phase and delve directly into a selection of nutritious recipes, thoughtfully curated based on your fruit inventory, courtesy of the Chap GPT API.

Embark on a journey that elevates your cooking experience. Uncover the potential within your ingredients and savor the rich flavors that your fruit bowl can offer. Make every meal a delightful adventure. 😋🤤

## Getting Started

To use the Fruit Pantry Assistant:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the Flask app using `python app.py`.

## Usage

1. Upload a photo of your pantry or fruit bowl.
2. Choose the number of meal ideas you want.
3. Review detected fruits and adjust if necessary.
4. Explore healthy meal ideas based on the detected fruits.

## Screenshots

![App Screenshot 1](screenshots/web_app.png)
![App Screenshot 2](screenshots/example_result.jpg)

## Contributing

We welcome contributions from the community to enhance the Fruit Pantry Assistant project. If you'd like to contribute, please follow these steps:

1. Fork the repository to your GitHub account.
2. Clone your forked repository to your local machine.
3. Create a new branch for your feature or bug fix.
4. Make your changes, commit them, and push to your forked repository.
5. Create a pull request from your branch to the main branch of the original repository.

## Issues

If you encounter any issues or have suggestions for improvements, please [open an issue](https://github.com/your-username/fruit-pantry-assistant/issues).

## Acknowledgments

- The YOLOv8 model and related code are based on [Ultralytics](https://github.com/ultralytics/yolov5).
- Recipe suggestions are obtained from Chat GPT API.