import os

def check_class_distribution(data_path):
    class_counts = {}
    classes = [d for d in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, d))]
    for cls in classes:
        cls_path = os.path.join(data_path, cls)
        count = len([name for name in os.listdir(cls_path) if os.path.isfile(os.path.join(cls_path, name))])
        class_counts[cls] = count
        print(f"{cls}: {count}")

    return class_counts

# Usage
data_path = 'data/training/phyto_skye/phyto'
class_counts = check_class_distribution(data_path)
