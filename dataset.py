from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
from PIL import Image
import os

class University1652Dataset(Dataset):
    def __init__(self, root_dir, split='train', transform=None):
        """
        Args:
            root_dir (string): Directory with all the images.
            split (string): One of 'train', 'test', or 'val' to denote the dataset split.
            transform (callable, optional): Optional transform to be applied on a sample.
        """
        self.root_dir = root_dir
        self.split = split
        self.transform = transform
        self.images, self.labels = self._load_dataset()

    def _load_dataset(self):
        # Implement logic to load images and labels based on split
        # This might involve reading directory structures, parsing labels, etc.
        # Return lists/arrays of image paths and labels
        return images, labels

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir, self.images[idx])
        image = Image.open(img_name)
        label = self.labels[idx]

        if self.transform:
            image = self.transform(image)

        return image, label
