# IMAGE-AI 🤖

IMAGE-AI is a powerful AI system that integrates various machine learning models to perform advanced image analysis tasks such as image classification, object detection, and image segmentation. It can handle prompts like "What animal is this?", "How many animals are there in the picture?", and "What is the average RGB color of the animal?"

## Features

- **Image Classification**: Identifies and classifies objects or animals in an image.
- **Object Detection**: Detects and counts the number of objects (e.g., animals) in an image.
- **Image Segmentation**: Segments the image to isolate specific parts for further analysis.


                       +-------------------------+
                       |      Input Question     |
                       +-----------+-------------+
                                   |
                                   v
                      +------------+-------------+
                      |          NLP Model        |
                      +------------+--------------+
                                   |
                +------------------+------------------+
                |                  |                  |
                v                  v                  v
      +---------+------+  +--------+---------+  +-----+---------+
      | Classification |  | Object Detection |  | Segmentation  |
      |      Model     |  |      Model       |  |     Model     |
      +---------+------+  +--------+---------+  +-----+---------+
                |                  |                  |
                v                  v                  v
     +----------+----------+ +-----+-----+  +---------+---------+
     | Classify the Animal  | | Count the |  | Segment the Animal |
     |                      | |  Animals  |  | Calculate Average  |
     |                      | |            |  |    RGB Color      |
     +----------------------+ +-----------+  +--------------------+
"""
