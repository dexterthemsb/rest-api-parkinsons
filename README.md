# 💢 REST API for Parkinson's Diagnosis

A simple Flask API for predicting whether a person could be a Parkinson's patient or not based on some basic drawings of random shapes that he / she has drawn.

Deployed at: https://rest-api-parkinsons.onrender.com/

## 🚀 Installation

Just clone the repository and run the following command in a virtual environment:

```bash
pip install -r requirements.txt
```

## 📣 Usage

There are two end points:

1. ```GET @ '/'``` - which returns the following:

```python
{
  "msg": "Server is running."
}
```

2. ```POST @ '/predict'``` - It consists of a body with type as ```form-data``` with a key ```file``` and a success response with the prediction (healthy or parkinson are the two labels).

```python
{
    "label": "parkinson",
    "tensor": "tensor([4.9958e-04, 9.9950e-01])"
}
```

## ✌️ Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Always looking ahead for suggestions to improve. Cheers!

## 📜 License

[MIT](https://choosealicense.com/licenses/mit/)

## 🔨 Project Status

Up and running. Always adding new features.
