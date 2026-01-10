import os
import zipfile

# Source of your new labels
labels_path = '/kaggle/working/predictions/test_results/labels'
zip_name = 'submission.zip'

with zipfile.ZipFile(zip_name, 'w') as zipf:
    for file in os.listdir(labels_path):
        if file.endswith('.txt'):
            # This nests the files inside a folder named 'predictions' inside the zip
            zipf.write(os.path.join(labels_path, file),
                       arcname=os.path.join('predictions', file))

print("Final submission.zip created successfully!")
