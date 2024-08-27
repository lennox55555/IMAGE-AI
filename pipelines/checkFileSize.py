import os
import pathlib

def analyze_dataset(dataset_dir):
    total_photos = 0
    total_size = 0
    class_counts = {}

    # Walk through all subdirectories
    for root, dirs, files in os.walk(dataset_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                file_path = os.path.join(root, file)
                total_photos += 1
                total_size += os.path.getsize(file_path)

                # Count photos per class
                class_name = os.path.basename(root)
                class_counts[class_name] = class_counts.get(class_name, 0) + 1

    # Convert total size to appropriate unit
    size_gb = total_size / (1024 * 1024 * 1024)  # Convert to GB

    # Print results
    print(f"Total number of photos: {total_photos}")
    print(f"Total size of dataset: {size_gb:.2f} GB")
    print("\nBreakdown by class:")
    for class_name, count in sorted(class_counts.items()):
        print(f"{class_name}: {count} photos")

if __name__ == "__main__":
    dataset_dir = "/Volumes/PortableSSD/dataset"  # Adjust this path if necessary
    analyze_dataset(dataset_dir)