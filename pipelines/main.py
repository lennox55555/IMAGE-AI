import os
import shutil
from bing_image_downloader import downloader


def get_ssd_usage(path):
    total, used, free = shutil.disk_usage(path)
    return used / (2 ** 40)  # Convert to terabytes


def create_dataset(items):
    # Define the path to the external SSD
    dataset_dir = "/Volumes/PortableSSD/dataset"

    # Create a folder named 'dataset' on the SSD if it doesn't exist
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)

    image_count = 0
    while get_ssd_usage("/Volumes/PortableSSD") < 1.5:
        for item in items:
            # Create subfolders for each item on the SSD
            item_dir = os.path.join(dataset_dir, item)
            if not os.path.exists(item_dir):
                os.makedirs(item_dir)

            # Download images
            try:
                downloader.download(item, limit=100, output_dir=dataset_dir,
                                    adult_filter_off=True, force_replace=False,
                                    timeout=200, filter='.jpg')

                # Rename downloaded images
                downloaded_files = os.listdir(os.path.join(dataset_dir, item))
                jpg_files = [f for f in downloaded_files if f.lower().endswith('.jpg')]

                for i, file in enumerate(jpg_files):
                    old_path = os.path.join(dataset_dir, item, file)
                    new_name = f"Image{image_count + i + 1}.jpg"
                    new_path = os.path.join(dataset_dir, item, new_name)
                    os.rename(old_path, new_path)

                image_count += 100
                print(f"Downloaded 100 images for {item}. Total images: {image_count}")
            except Exception as e:
                print(f"Failed to download images for {item}: {e}")

            if get_ssd_usage("/Volumes/PortableSSD") >= 1.5:
                print("SSD capacity reached 1.5 TB. Stopping download.")
                return


if __name__ == "__main__":
    items = [
        "a nut (hardware)",
        "a bolt (hardware)",
        "a screw (hardware)",
        "a washer (hardware)",
        "a nail (hardware)",
        "a hinge (hardware)",
        "a bracket (hardware)",
        "a anchor (hardware)",
        "a rivets (hardware)",
        "a clamp (hardware)",
        "a grommet (hardware)",
        "a pin (hardware)",
        "a stud (hardware)",
        "a bushing (hardware)",
        "a spacer (hardware)",
        "a latche (hardware)",
        "a fastener (hardware)",
        "a spring (hardware)",
        "a lock (hardware)",
        "a hook (hardware)",
        "a clip (hardware)",
        "a coupling (hardware)",
        "a o-ring (hardware)",
        "a gasket (hardware)",
        "a seal (hardware)",
        "a bearing (hardware)",
        "a knob (hardware)",
        "a handle (hardware)",
        "a pulley (hardware)",
        "a chain (hardware)",
        "a cable (hardware)",
        "a fitting (hardware)",
        "a standoff (hardware)",
        "a tack (hardware)",
        "a tie-down (hardware)",
        "a eyelet (hardware)",
        "a plate (hardware)",
        "a strap (hardware)"
    ]
    create_dataset(items)