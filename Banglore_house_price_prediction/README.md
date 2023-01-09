# Banglore House Predictions:

This is one of the guided projects. The main aim of this project is to find the price for a home in Banglore given its Location, BHK size, Total square feet area and number of bathrooms. Following are the steps undertaken:

1. **Preprocessing the data**: Data cleaning, outlier detection, dimensionality reduction.
2. **Model building**: After the preprocessing and splitting the data in train test split it is time to search the Best Model this is done by gridSearchCV in this project, this approach isn't just used to find the best model but also is used for hyper parameter tuning i.e. finding the best parameter.
3. **Prediction and accuracy measurement**: As the model was selected using gridsearchcv it gives good score also the predictions were mostly correct.
4. **Deployment using Flask server**: Here is where I deployed the model on to a website using Python Flask server. Using postman I tested the model on various of its methods such as prediction methods and the method for displaying locations. With the help of html, css and java the model was deployed well on a website. Here is the snapshot of the webpage.

***📢This page is responsive only when my server is on. I don't know how to fix it if anyone can knows how to please feel free to help.***

![Screenshot (159)](https://user-images.githubusercontent.com/85283030/211310983-758fedf4-29f2-4840-9d14-661994b147b1.png)
