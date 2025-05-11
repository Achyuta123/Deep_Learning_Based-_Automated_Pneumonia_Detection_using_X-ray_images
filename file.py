import os

def rename_files(root_folder):
    test_folder = os.path.join(root_folder, 'test')
    pneumonia_folder = os.path.join(test_folder, 'PNEUMONIA')
    normal_folder = os.path.join(test_folder, 'NORMAL')

    # Rename files in pneumonia folder
    for i, filename in enumerate(os.listdir(pneumonia_folder)):
        os.rename(os.path.join(pneumonia_folder, filename), os.path.join(pneumonia_folder, f'1_{i}.jpg'))
    
    # Rename files in normal folder
    for i, filename in enumerate(os.listdir(normal_folder)):
        os.rename(os.path.join(normal_folder, filename), os.path.join(normal_folder, f'0_{i}.jpg'))

root_folder = r"C:\Users\HP\Desktop\major project\dataset"
rename_files(root_folder)
