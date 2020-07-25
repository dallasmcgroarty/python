# *** Supervised Learning ***

# supervised learning algorithms are trained using labeled examples, 
# such as an input where the desired output is known
# for example a segment of text could havea category label such as:
    # spam vs legitimate emails
    # positive vs negative moview review


# how it works:
    # networks receives a set of inputs along with the corresponding correct outputs,
    # and the algorithm learns by comparing its actual output with corect outputs
    # to find errors
    # it then modifies the model accordingly

# supervised learning is commonly used in applications where historical data
# predicts likely future events

# Machine Learning Process - simplified approach
# 1. Data Acquisition - getting your data
# 2. Data Cleaning - clean and format data (using pandas)
# 3. Split data into Test Data and Training Data
#   a. fit a model to the training data
#   b. run test data through model we created
#   c. compare and evaulate the model after testing
# 4. Model Deployment


# Data often split into 3 sets:
#   1. Training Data - used to train model parameters
#   2. Validation Data - used to determine what model hyperparameters to adjust
#   3. Test Data - used to get some final performance metric


# After we see the results on the final test set we do not go back and 
# adjust any model parameters
# This final measure is what we label the true performance of the model to be 
# on unseen data


# In this course, in general we will simplify our data by using simple 
# train/test split
# We will simply train and then evaluate on a test set
# After going through the course, you will be bale to easily perform
# another split to get 3 data sets if you desire