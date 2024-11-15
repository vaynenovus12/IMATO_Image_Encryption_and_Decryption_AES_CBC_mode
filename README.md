<h1 align="center">
  <br>
  <a href="#"><img src="https://github.com/user-attachments/assets/2cac09ea-9581-4ebb-befb-52cd9231528b" alt="IMATO" width="200"></a>
  <br>
  IMATO
  <br>
</h1>

<h4 align="center">IMATO is an image encryption and decryption application that leverages AES encryption in CBC mode. The app is developed with Python and <a href="https://docs.python.org/3/library/tkinter.html" target="_blank">Tkinter</a>, providing a graphical user interface to encrypt and decrypt images securely.</h4>

<p align="center">
  <a href="https://pypi.org/project/pip/">
    <img src="https://img.shields.io/pypi/v/pip.svg"
         alt="PyPI">
  </a>
  <a href="https://pypi.org/project/pip/">
    <img src="https://img.shields.io/pypi/pyversions/pip"
         alt="PyPI - Python Version">
  </a>
  <a href="https://pip.pypa.io/en/latest">
    <img src="https://readthedocs.org/projects/pip/badge/?version=latest"
         alt="Documentation">
  </a>
  <a href="https://pypi.org/project/pycryptodome/">
    <img src="https://badge.fury.io/py/pycryptodome.svg"
         alt="pycryptodome 3.21.0">
  </a>
  <a href="https://pypi.org/project/pillow/"><img
                alt="Newest PyPI version"
                src="https://img.shields.io/pypi/v/pillow.svg"></a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>

![IMATO_1](https://github.com/user-attachments/assets/131401ac-65c8-49b3-83ff-842f2ea69aa9)

## Key Features

* AES-CBC Encryption: Encrypts images using the AES algorithm in CBC mode with a user-defined key
* Secure Storage: Generates an encrypted image that can only be decrypted with the correct key
* User Interface: Built with Tkinter for an intuitive GUI  
* Splash Screen: Displays a loading animation and information about the app's development team
* Full-Screen Support: Runs in full screen with high-resolution images

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/vaynenovus12/IMATO_Image_Encryption_and_Decryption_AES_CBC_mode.git

# Go into the repository
$ cd cd IMATO_Image_Encryption_and_Decryption_AES_CBC_mode

# Install the required dependencies
$ pip install -r requirements.txt

# Run the application
$ python main.py
```

> **Note**
> Ensure that your Python environment is correctly set up with the required dependencies. This application has been tested with Python 3.11 and above. If you encounter issues, verify that all libraries in requirements.txt are installed and that your Python version is compatible

Encrypt:
1) Enter a 16-character key in the input field.
2) Select an image to encrypt by clicking the Encrypt button.
3) Encrypted image will be saved as encrypted_img.PNG.
4) Decrypt:

Decrypt:
1) Enter the correct key in the input field.
2) Select the encrypted image by clicking the Decrypt button.
3) Decrypted image will be saved as decrypted_img.PNG.


## Credits

This software uses the following open source packages:

- [Python Imaging Libray (Pillow)](https://pypi.org/project/pillow/)
- [PyCryptodome](https://pypi.org/project/pycryptodome/)

## License

BSD 2-Clause license

---

> GitHub [@vaynenovus12](https://github.com/vaynenovus12) &nbsp;&middot;&nbsp;
> Twitter [@vaynenovus12](https://twitter.com/vaynenovus12)
