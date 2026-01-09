import os
import zipfile

labels_path = "predictions/test_results/labels"
zip_name = "submission.zip"

with zipfile.ZipFile(zip_name, "w") as zipf:
    for file in os.listdir(labels_path):
        if file.endswith(".txt"):
            zipf.write(
                os.path.join(labels_path, file),
                arcname=os.path.join("predictions", file)
            )

print("submission.zip created successfully")
