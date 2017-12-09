# DR Fall 2017 Project

## Objective
Train a model that may inform a self-driving car when to 'Brake' given certain data inputs, and evaluate the model using ground truth data as well as human formulated logic for when to 'Brake' (e.g. if object detected is 'near' and velocity is not 'already decreasing at a fast rate' then 'Brake')

Data used for this project come from the [KITTI Vision Benchmark Suite](http://www.cvlibs.net/datasets/kitti/index.php) (positional, velocity, acceleration, etc.) and labeled object detection data from [KITTI MoSeg](http://webdocs.cs.ualberta.ca/~vis/kittimoseg/)

## Data
Data used for this project come from the [KITTI Vision Benchmark Suite](http://www.cvlibs.net/datasets/kitti/index.php) (positional, velocity, acceleration, etc.) and labeled object detection data from [KITTI MoSeg](http://webdocs.cs.ualberta.ca/~vis/kittimoseg/).  Downloaded datasets from these sources are found in the drive_data and box_data folders respectively.

A processed data set is found in the processed_data folder.

## Scripts
Data from the above sources is processed in ParseFeaturesAndLabels.ipynb

A basic LSTM is trained on the time series data in LSTM.ipynb

TODO: 
HMM
Stagger General ML
Revisit LSTM
GANS or  VAE to create new images for training



