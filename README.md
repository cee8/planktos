# Planktos: Phytoplankton Image Recognition


<div align="center">
  <img src="https://github.com/cee8/some-chris-images/blob/main/IMG_9070.jpg" width="250" height="300" style="margin: 10px;"/>
  <img src="https://github.com/cee8/some-chris-images/blob/main/Aphin.png" width="250" height="300" style="margin: 10px;"/>
  <img src="https://github.com/cee8/some-chris-images/blob/main/IMG_8911.jpg" width="250" height="300" style="margin: 10px;"/>
  <img src="https://github.com/cee8/some-chris-images/blob/main/IMG_9086.jpg" width="250" height="300" style="margin: 10px;"/>
</div>

<br/>


Planktos is an innovative image recognition model tailored for classifying various species of phytoplankton. Built using cutting-edge machine learning algorithms, this tool enables researchers and environmentalists to automate and accelerate the identification process, enhancing studies in marine biology and ecology.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Training the Model](#training-the-model)
  - [Predicting with the Model](#predicting-with-the-model)
  - [Data Preprocessing](#data-preprocessing)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **Customizable Model Training**: Fine-tune the model parameters based on your specific dataset requirements.
- **Efficient Prediction**: Utilize the trained model to classify new images quickly and accurately.
- **Flexible Data Preprocessing**: Ready your dataset for training with a robust preprocessing script tailored for phytoplankton image data.

## Installation

Clone the repository and install the necessary dependencies:

```bash
git clone https://github.com/cee8/planktos.git
cd planktos
pip install -r requirements.txt
```

## Usage

### Training the Model

Start the training process with the following command, which will also handle model serialization and label saving:

```bash
python3 metaflow/phytoplankton_flow.py run
```

### Predicting with the Model
To predict phytoplankton classes from new images:
```bash
python3 src/predict_image.py
```



### Data Preprocessing
Prepare your dataset by running the preprocessing script:

```bash
python3 src/data_loader.py
```


## Contributing
We welcome contributions to Planktos! For more information on how to help, please refer to the contributing guidelines.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
Feel free to raise any issues or suggestions on the GitHub page. Alternatively, you can contact me directly at cee8@github.com.
