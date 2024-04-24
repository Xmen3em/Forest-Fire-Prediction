# Forest Fire Prediction Django App

![](Deerfire_high_res_edit.jpg)

This repository contains a Django app that aims to predict the burned area of forest fires in the northeast region of Portugal, using meteorological and other data. The app is based on the [forestfires dataset](https://www.kaggle.com/datasets/elikplim/forest-fires-data-set/data) available on Kaggle.

## Table of Contents
* [Dataset Overview](#dataset-overview)
* [Notebook Contents](#notebook-contents)
* [Requirements](#requirements)
* [Usage](#usage)
* [Screenshots](#screenshots)

## Dataset Overview
- The data is a CSV file.
- The data is acquired from the following link:
    - https://archive.ics.uci.edu/ml/datasets/forest+fires

## Notebook Contents
The Jupyter Notebook included in this repository covers the following steps:

1. **Data Preprocessing**: The dataset is preprocessed to handle missing values, encode categorical variables, and remove duplicate values.
2. **Exploratory Data Analysis (EDA)**: Various visualizations and statistical analyses are performed to gain insights into the distribution and relationships among different features in the dataset.
3. **Machine Learning (ML)**: Several machine learning algorithms such as linear regression and random forest regressor are implemented to predict the burned area of forest fires. The models are trained, evaluated, and compared using appropriate metrics.
4. **Deep Neural Network (DNN)**: A deep neural network model is constructed using TensorFlow/Keras to predict the burned area of forest fires. The model architecture, training process, and evaluation results are presented.

## [Requirements](Django%20App/requirements.txt)
To run this app, you need the following dependencies installed:
* Django
* pandas
* numpy
* matplotlib
* seaborn
* scikit-learn
* TensorFlow/Keras

## Usage
1. Clone this repository to your local machine.
2. Install the required dependencies.
3. Run the Django app using the appropriate [command](Django%20App/Flow.txt).

## Screenshots
Here are some screenshots of the Forest Fire Prediction Django app:

![Screenshot 1](imgs/Screenshot%20from%202024-04-24%2007-09-29.png)
![Screenshot 2](imgs/Screenshot%20from%202024-04-24%2007-09-46.png)
![Screenshot 3](imgs/Screenshot%20from%202024-04-24%2007-10-09.png)
