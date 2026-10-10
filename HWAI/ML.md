# Machine Learning Basics

This guide introduces the main ideas of machine learning for a beginner. It focuses on what the concepts mean, how the major algorithms work, and how a complete machine-learning project is organized.

## 1. What Is Machine Learning?

Machine learning is a way of creating programs that learn patterns from data.

In traditional programming, a programmer writes rules:

```text
Data + Human-written rules -> Answer
```

In machine learning, an algorithm learns the rules from examples:

```text
Training data + Correct answers -> Trained model
Trained model + New data       -> Prediction
```

For example, suppose we want to predict a phone's price using three features:

```text
hardware score, system score, AI score -> price
```

Instead of manually deciding how much each score affects the price, a machine-learning algorithm learns those relationships from phones whose prices are already known.

## 2. Important Vocabulary

### Sample

One item or observation in a dataset.

```text
Phone 1: hardware=86, system=99, AI=20, price=3595
```

This entire record is one sample.

### Feature

An input value used to make a prediction.

In the phone example, the features are:

```text
hardware score, system score, AI score
```

Features are commonly written as a vector:

```text
x = [86, 99, 20]
```

### Label or Target

The correct answer that the model should learn to predict.

```text
y = 3595
```

For classification, the label could be a category such as:

```text
0 = healthy
1 = cold
2 = pneumonia
```

### Model

A mathematical function that converts features into a prediction:

```text
features -> model -> prediction
```

### Parameters

Values learned by the model during training. Examples include the weights and bias in linear regression.

### Hyperparameters

Settings chosen before training, rather than learned from data. Examples include:

- Learning rate
- Number of training epochs
- Number of neighbors in KNN
- Maximum depth of a decision tree
- Number of clusters in K-means

## 3. The Main Types of Machine Learning

### 3.1 Supervised Learning

Supervised learning uses training samples that include correct answers.

```text
features + label
```

It has two major tasks.

#### Regression

Regression predicts a number.

Examples:

- Predicting a phone's price
- Predicting tomorrow's temperature
- Predicting delivery time

Common algorithms:

- Linear regression
- Decision-tree regression
- Random forest regression
- Neural networks

#### Classification

Classification predicts a category.

Examples:

- Spam or not spam
- Healthy, cold, or pneumonia
- Cat, dog, or bird

Common algorithms:

- Logistic regression
- K-nearest neighbors
- Decision trees
- Support vector machines
- Naive Bayes
- Neural networks

### 3.2 Unsupervised Learning

Unsupervised learning uses data without correct labels. The algorithm tries to discover structure in the data.

Common tasks include:

- Clustering similar samples
- Reducing the number of dimensions
- Detecting unusual samples

Common algorithms:

- K-means clustering
- Hierarchical clustering
- DBSCAN
- Principal component analysis (PCA)

### 3.3 Reinforcement Learning

An agent interacts with an environment and learns through rewards and penalties.

```text
state -> action -> reward -> improved behavior
```

Examples include:

- Game-playing agents
- Robot control
- Resource scheduling

## 4. The Machine-Learning Workflow

A typical project follows these steps:

```text
1. Define the problem
2. Collect data
3. Clean and prepare the data
4. Split the data
5. Choose a model
6. Train the model
7. Evaluate the model
8. Tune the model
9. Test the final model
10. Deploy and monitor it
```

### Step 1: Define the problem

Decide:

- What should be predicted?
- Is it regression, classification, or clustering?
- What measurement determines success?

### Step 2: Collect data

The data should represent the situations the model will encounter after deployment.

### Step 3: Prepare the data

Preparation can include:

- Removing or correcting invalid records
- Handling missing values
- Converting categories into numbers
- Normalizing feature scales
- Removing duplicated samples

### Step 4: Split the data

Data is commonly divided into three parts:

- **Training set:** used to learn model parameters
- **Validation set:** used to choose hyperparameters
- **Test set:** used once at the end to estimate real performance

A common split is:

```text
70% training, 15% validation, 15% testing
```

The exact percentages depend on the amount of available data.

## 5. Training a Model

Training normally repeats the following process:

```text
1. Make predictions
2. Calculate the error
3. Calculate how each parameter affected the error
4. Update the parameters
5. Repeat
```

### Loss Function

A loss function measures how wrong the model is. Training tries to make the loss smaller.

#### Mean Squared Error

Mean squared error is commonly used for regression:

```text
MSE = average((prediction - true value)^2)
```

Large errors are penalized strongly because the difference is squared.

#### Binary Cross-Entropy

Binary cross-entropy is commonly used for two-class classification. It penalizes predicted probabilities that disagree with the correct label.

### Gradient Descent

Gradient descent updates parameters in the direction that reduces the loss:

```text
new parameter = old parameter - learning rate * gradient
```

The gradient tells us how the loss changes when a parameter changes.

### Learning Rate

The learning rate controls the size of each update.

- Too small: training can be very slow.
- Too large: training can jump around or fail to converge.
- Suitable value: the loss decreases steadily.

### Epoch and Batch

- **Epoch:** one complete pass through the training dataset
- **Batch:** a group of samples processed before updating the parameters
- **Batch size:** the number of samples in one batch

If the batch size is 1, the model updates after every sample. This is called stochastic gradient descent, or SGD.

## 6. Common Algorithms

## 6.1 Linear Regression

Linear regression predicts a continuous number using a weighted sum:

```text
prediction = bias + w1*x1 + w2*x2 + ... + wn*xn
```

For phone prices:

```text
price = bias
      + w1 * hardware_score
      + w2 * system_score
      + w3 * AI_score
```

The model learns the weights and bias that minimize prediction error.

Linear regression is useful when the relationship is approximately linear and easy interpretation is important.

## 6.2 Logistic Regression

Despite its name, logistic regression is mainly a classification algorithm.

First, it calculates a weighted sum:

```text
z = bias + w1*x1 + w2*x2 + ... + wn*xn
```

Then it uses the sigmoid function to convert `z` into a value between 0 and 1:

```text
sigmoid(z) = 1 / (1 + exp(-z))
```

The result can be interpreted as a probability. For example:

```text
probability > 0.5  -> class 1
probability <= 0.5 -> class 0
```

## 6.3 K-Nearest Neighbors (KNN)

KNN predicts a sample using nearby known samples.

For classification:

1. Calculate the distance from the new sample to every training sample.
2. Select the `K` closest samples.
3. Count their labels.
4. Return the most common label.

Example with `K = 3`:

```text
Nearest labels: [0, 0, 1]
Prediction: 0
```

KNN is simple, but prediction can be slow because it compares a new sample with many stored samples.

Feature normalization is important because a large-scale feature can dominate the distance.

## 6.4 Decision Tree

A decision tree repeatedly asks questions about features.

```text
Is temperature <= 37.5?
├── Yes: Is coughing <= 1?
│   ├── Yes: healthy
│   └── No:  cold
└── No: pneumonia
```

Each internal node contains:

- A feature
- A threshold
- A left child
- A right child

A leaf node contains the final prediction.

Decision trees are easy to understand, but a very deep tree can memorize the training data.

## 6.5 Random Forest

A random forest trains many decision trees using different subsets of data and features.

For classification, the trees vote. For regression, their predictions are averaged.

Random forests are generally more stable and less likely to overfit than a single decision tree.

## 6.6 K-Means Clustering

K-means separates unlabeled samples into `K` groups.

The procedure is:

1. Choose `K` initial centers.
2. Assign each sample to its closest center.
3. Recalculate each center using the mean of its assigned samples.
4. Repeat until the centers stop changing or the iteration limit is reached.

K-means is used for tasks such as grouping customers or generating YOLO anchor-box dimensions.

The number `K` must be selected before running the algorithm.

## 6.7 Support Vector Machine (SVM)

An SVM tries to find a boundary that separates classes with the largest possible margin.

It often works well on small or medium-sized datasets with clear class boundaries. Kernels allow it to model nonlinear boundaries.

## 6.8 Naive Bayes

Naive Bayes uses probability to select the most likely class. It assumes that features are independent after the class is known.

That assumption is often not completely true, but the method can still work well, especially for text classification.

## 6.9 Neural Networks

A neural network contains layers of weighted calculations.

A simple two-layer network can be written as:

```text
hidden = input * W1
prediction = hidden * W2
```

Real neural networks commonly add:

- Biases
- Activation functions such as ReLU
- Many hidden layers
- Normalization and regularization

### Forward Propagation

Forward propagation calculates a prediction from the input:

```text
input -> hidden layers -> output
```

### Backpropagation

Backpropagation works backward from the loss to calculate how much every weight contributed to the error.

```text
loss -> output layer -> hidden layers -> earlier layers
```

The optimizer then updates the weights using those gradients.

Deep learning refers to neural networks with multiple layers. It is widely used for images, text, speech, and other complex data.

## 7. Classification Evaluation

For binary classification, predictions can be divided into four groups:

| Name | Meaning |
|---|---|
| True Positive (TP) | Predicted positive and actually positive |
| False Positive (FP) | Predicted positive but actually negative |
| False Negative (FN) | Predicted negative but actually positive |
| True Negative (TN) | Predicted negative and actually negative |

For multiclass classification, calculate these values separately for each class by treating that class as positive and all other classes as negative.

### Accuracy

```text
accuracy = correct predictions / all predictions
```

Accuracy can be misleading when one class is much more common than another.

### Precision

Precision asks:

> Of everything predicted as this class, how much was correct?

```text
precision = TP / (TP + FP)
```

### Recall

Recall asks:

> Of everything truly belonging to this class, how much did the model find?

```text
recall = TP / (TP + FN)
```

### F1 Score

F1 combines precision and recall:

```text
F1 = 2 * precision * recall / (precision + recall)
```

It is useful when both false positives and false negatives matter.

### Confusion Matrix

A confusion matrix shows actual labels as rows and predicted labels as columns:

```text
                 Predicted
               0    1    2
Actual 0       10    2    1
Actual 1        3    8    0
Actual 2        0    1    9
```

For class `0`:

- TP is the cell at actual 0, predicted 0.
- FP is the rest of predicted column 0.
- FN is the rest of actual row 0.

## 8. Regression Evaluation

### Mean Absolute Error (MAE)

```text
MAE = average(abs(prediction - true value))
```

MAE is easy to interpret because it uses the same unit as the target.

### Mean Squared Error (MSE)

```text
MSE = average((prediction - true value)^2)
```

MSE penalizes large mistakes more strongly.

### Root Mean Squared Error (RMSE)

```text
RMSE = sqrt(MSE)
```

RMSE has the same unit as the target.

### R-squared

R-squared measures how much of the target's variation is explained by the model. A value closer to 1 is generally better, although interpretation depends on the problem.

## 9. Overfitting and Underfitting

### Underfitting

The model is too simple to learn the important patterns.

```text
Training performance: poor
Validation performance: poor
```

Possible solutions:

- Use a more capable model.
- Add useful features.
- Train longer if optimization has not converged.

### Overfitting

The model memorizes training details and does not generalize well.

```text
Training performance: excellent
Validation performance: poor
```

Possible solutions:

- Collect more training data.
- Simplify the model.
- Use regularization.
- Stop training earlier.
- Use data augmentation.

### Generalization

Generalization is the ability to perform well on new data that was not used during training. This is the real objective of machine learning.

## 10. Data Preprocessing

### Normalization

Normalization puts features on similar scales. One common method converts values into the range `[0, 1]`:

```text
normalized = (value - minimum) / (maximum - minimum)
```

### Standardization

Standardization centers values around zero:

```text
standardized = (value - mean) / standard_deviation
```

Scaling is especially important for algorithms based on distances or gradients, such as KNN, K-means, SVM, and neural networks.

### One-Hot Encoding

One-hot encoding represents categories using binary columns.

```text
red   -> [1, 0, 0]
green -> [0, 1, 0]
blue  -> [0, 0, 1]
```

### Missing Values

Possible approaches include:

- Remove samples with missing data.
- Fill with the mean, median, or most common value.
- Use a model designed to handle missing values.

The correct choice depends on why the values are missing.

## 11. Important Practical Ideas

### Data Leakage

Data leakage happens when information unavailable in the real prediction situation accidentally enters training.

For example, calculating normalization statistics using the test set gives the model information about the test data.

Fit preprocessing operations on the training data, then apply the same transformations to validation and test data.

### Class Imbalance

A dataset is imbalanced when one class has far more samples than another.

Possible solutions include:

- Use precision, recall, F1, or area under the precision-recall curve.
- Give more weight to minority-class mistakes.
- Resample the training data.
- Collect more minority-class examples.

### Feature Engineering

Feature engineering creates useful features from raw data. Good features can make simple models perform very well.

Examples:

- Extracting hour and weekday from a timestamp
- Calculating body mass index from height and weight
- Counting whether each letter appears in a string

### Reproducibility

Random initialization and random data splitting can change results. Set a random seed when you need repeatable experiments.

## 12. How to Choose an Algorithm

| Problem | Useful starting algorithm |
|---|---|
| Predict a number | Linear regression |
| Binary classification | Logistic regression |
| Explainable rule-based prediction | Decision tree |
| Small normalized dataset | KNN or SVM |
| Strong general-purpose tabular model | Random forest or gradient boosting |
| Find groups without labels | K-means |
| Images, text, speech, or large complex data | Neural network |

There is no single best algorithm for every dataset. Start with a simple baseline, measure its performance, and increase complexity only when necessary.

## 13. A Small End-to-End Example

Suppose we want to classify emails as spam or not spam.

### Inputs

Features might include:

```text
number of links
contains the word "free"
sender is known
message length
```

The label is:

```text
0 = not spam
1 = spam
```

### Process

```text
1. Collect labeled emails.
2. Convert each email into numeric features.
3. Split the emails into training, validation, and test sets.
4. Train logistic regression.
5. Predict probabilities on the validation set.
6. Choose an appropriate probability threshold.
7. Measure precision, recall, and F1.
8. Evaluate once on the test set.
9. Deploy and monitor the model.
```

If blocking legitimate email is very costly, prioritize precision. If missing spam is very costly, prioritize recall.

## 14. Suggested Learning Order

For a beginner, this order provides a useful foundation:

1. Python basics, lists, loops, functions, and classes
2. Vectors and matrices
3. Mean, variance, and basic probability
4. Train, validation, and test datasets
5. Linear regression
6. Logistic regression
7. Evaluation metrics and confusion matrices
8. KNN
9. Decision trees and random forests
10. K-means clustering
11. Gradient descent
12. Neural networks and backpropagation

Implementing small versions of these algorithms without a machine-learning framework is a good way to understand them. After the ideas are clear, libraries such as NumPy and scikit-learn make practical work much easier.

## 15. Quick Reference

```text
Feature             Input value
Label/target        Correct answer
Prediction          Model's answer
Parameter           Value learned during training
Hyperparameter      Setting chosen before training
Loss                Measurement of model error
Gradient            Direction and rate of loss change
Epoch               One pass through the training data
Batch               Samples processed before an update
Inference           Using a trained model to predict
Generalization      Performance on unseen data
Overfitting         Memorizing training data
Underfitting        Failing to learn enough structure
```

The central idea of machine learning is simple:

> Learn patterns from past examples, verify those patterns on unseen data, and use the learned model to make useful predictions.
