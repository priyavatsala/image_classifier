#  AI Image Classifier (MobileNetV2)

A ready-to-use image classification system powered by TensorFlow/Keras and pre-trained MobileNetV2 model.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## Features
- Instant classification of 1000+ object categories
- No training required - uses pre-trained ImageNet weights
- Lightweight and fast predictions (<1 second on CPU)
- Clean terminal output with confidence scores
- Built-in error handling for missing files

##  Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/image-classifier.git
cd image-classifier
pip install -r requirements.txt
=== Image Classification Starting ===
Loading image: dog.jpg
Loading MobileNetV2 model...
Classifying image...

=== Classification Results ===
1. golden_retriever: 92.45%
2. Labrador_retriever: 6.12%
3. German_shepherd: 0.87%
