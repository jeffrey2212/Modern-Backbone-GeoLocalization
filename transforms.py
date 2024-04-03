from torchvision import transforms

# Define the transformations for the dataset
transform = transforms.Compose([
    transforms.Resize((448, 448)),  # Resize images as mentioned in the paper
    transforms.RandomHorizontalFlip(),  # Data augmentation
    transforms.RandomRotation(15),  # Rotate images to a certain degree
    transforms.ToTensor(),  # Convert images to PyTorch tensors
    transforms.Normalize(mean=[0.485, 0.456, 0.406],  # Normalize images
                         std=[0.229, 0.224, 0.225])
])
