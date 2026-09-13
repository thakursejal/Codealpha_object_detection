# Codealpha_object_detection
🎯 AI Object Detection

«Detect. Analyze. Understand. 🤖»

An AI-powered Object Detection Web Application built using Python, YOLO, and Streamlit. The application detects objects in both images and videos, displaying bounding boxes, object labels, confidence scores, and detection summaries.

🚀 Live Demo

🔗 "Try the AI Object Detection App" (https://codealpha-object-detection.streamlit.app/)

✨ Features

- 📷 Detect objects in images
- 🎥 Detect objects in videos
- 🎯 Display bounding boxes
- 🏷️ Show object labels
- 📊 Display confidence scores
- 📈 Generate video detection summaries
- 🔢 Show detection counts
- ⬇️ Download detected videos
- 🌐 Simple and interactive web interface

🧠 How It Works

        Upload Image / Video
                ↓
           YOLO Model
                ↓
        Object Detection
                ↓
      Bounding Boxes + Labels
                ↓
         Confidence Scores
                ↓
         Detection Results

🛠️ Tech Stack

- 🐍 Python
- 🤖 YOLO (Ultralytics)
- 🎈 Streamlit
- 👁️ OpenCV
- 🖼️ Pillow
- 🎞️ FFmpeg

📷 Image Detection

Upload an image and the YOLO model identifies the objects present in it.

The application displays:

- Object name
- Bounding box
- Confidence score
- Detection details

🎥 Video Detection

Upload a video and the application processes it frame by frame using YOLO.

The result includes:

- Detected video
- Object labels
- Bounding boxes
- Confidence scores
- Frames processed
- Object types detected
- Average confidence
- Detection counts
- Download option

📊 Detection Summary

For video input, the application provides a summary such as:

👤 Person     — Average Confidence
🍾 Bottle     — Average Confidence
🪑 Chair      — Average Confidence
📺 TV         — Average Confidence
💻 Laptop     — Average Confidence

The summary also shows the number of detections for each object.

🎯 Applications

Object detection can be useful in areas such as:

- 🤖 Robotics
- 🚦 Traffic monitoring
- 🏭 Industrial inspection
- 📹 Video analytics
- 🛒 Retail analytics
- 🏙️ Smart city applications
- 🔐 Security systems

🚀 Future Enhancements

- 📹 Real-time webcam detection
- 🎯 Object tracking
- 📊 Advanced detection analytics
- 🧠 Custom-trained YOLO models
- 🔔 Object-based alerts
- 📈 Detection history

🎓 Learning Outcomes

Through this project, I gained hands-on experience with:

- Computer Vision
- Object Detection
- YOLO
- Python
- Streamlit
- Image & Video Processing
- Model Inference
- Web Application Deployment

📁 Project Structure

Codealpha_object_detection/
│
├── app.py
├── requirements.txt
└── README.md

👩‍💻 Author

Thakur Sejal
B.Tech — Artificial Intelligence & Machine Learning

⭐ Project

Developed as part of my AI Internship to gain practical experience in Computer Vision, Object Detection, Python, and AI application deployment.

---

⭐ If you found this project useful, consider giving the repository a star!

Built with 🐍 Python • 🤖 YOLO • 🎈 Streamlit
