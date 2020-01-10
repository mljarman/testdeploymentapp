This app serves as an API to predict AirBnB prices in Berlin.

The pickled model uses a vectorizer, Ordinal Encoding, and Standard Scalar to preprocess the data and then runs it through a Ridge Regression model.

The API receives the JSON request from the end_user, transforms it into a dataframe that the model can understand, runs it through the pickled pipeline and creates a predicted price based on the inputs that is a JSON object.

The API connects with the backend engineer's databases and allows the user to store listings, create new listings, edit, copy, and delete etc from within their account.
