# dataset.py

import os
import pandas as pd
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms


class SkinLesionDataset(Dataset):
    def __init__(self, csv_path, transform=None):
        self.data = pd.read_csv(csv_path)
        self.transform = transform
        self.label_map = {"benign": 0, "malignant": 1}

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        row = self.data.iloc[idx]
        image_path = row["image_path"]
        label = self.label_map[row["label"]]
        image = Image.open(image_path).convert("RGB")

        if self.transform:
            image = self.transform(image)

        return image, label
