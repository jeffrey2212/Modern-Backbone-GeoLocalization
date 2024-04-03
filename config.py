# Configuration settings for your project

# Dataset paths
UNIVERSITY_1652_ROOT_DIR = '/path/to/university-1652/dataset'
UNIVERSITY_160K_ROOT_DIR = '/path/to/university-160k/dataset'

# Model Hyperparameters
LPN = 0
BATCH_SIZE = 16
BLOCK = 4
CLASSES = 701

LEARNING_RATE = 0.003

NUM_EPOCHS = 120

DROP_RATE = 0.3
FPS16 =  1
IMAGE_SIZE = 448

model = 'EVA'
name = 'EVA_1652_2023-07-13-08:38:00'

query = 'drone'
weight_decay = 0.001
weight_save_path = 'path/to/weights' 


# Other configurations
# For example, number of workers for DataLoader
NUM_WORKERS = 4