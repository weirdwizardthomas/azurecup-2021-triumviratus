import os

if __name__ == '__main__':
    cwd = os.getcwd()
    directory_name = os.path.split(cwd)[-1]

    if directory_name != 'src':
        print('Wrong working directory. Expected directory: {}. Provided directory: {}.'.format('src', directory_name))
    else:
        root = os.path.join('..', '..')
        os.makedirs(os.path.join(root, 'backend', 'model'), exist_ok=True)
        os.makedirs(os.path.join(root, 'backend', 'keychain', 'kaggle'), exist_ok=True)
        os.makedirs(os.path.join(root, 'data', 'image-database'), exist_ok=True)
