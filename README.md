# STEG
A simple implementation of Least significant bit based text encoding inside a image (steganography).


## Requirements

After cloning the repository, to install the requirements : 
```py
pip install requirements.txt
```
The only requirements are
```
numpy==1.20.1
Pillow==8.1.0
```

## Usage
import the `steg.py` and call the following functions


For encoding
```py
encode(image, message)
```

For decoding
```py
decode(image, msgLen)
```

For documentation, view the source code.
