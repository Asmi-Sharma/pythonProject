#
# from keras.models import Sequential
# from keras.layers import Dense
# from keras.layers import Flatten
# from keras.layers import Dropout
# from keras.layers.convolutional import Conv1D
# from keras.layers.convolutional import MaxPooling1D
#
# def fit_model(train, test):
#     verbose, epochs, batch_size = 0, 10, 32
#     n_timesteps, n_features, n_outputs = 1, 1, 1
#     model = Sequential()
#     model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(n_timesteps,n_features)))
#     model.add(Conv1D(filters=64, kernel_size=3, activation='relu'))
#     model.add(Dropout(0.5))
#     model.add(MaxPooling1D(pool_size=2))
#     model.add(Flatten())
#     model.add(Dense(100, activation='relu'))
#     model.add(Dense(n_outputs, activation='softmax'))
#     model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#     # fit network
#     model.fit(train, epochs=epochs, batch_size=batch_size, verbose=verbose)
#     # evaluate model
#     accuracy = model.evaluate(test, batch_size=batch_size, verbose=0)
#     print(accuracy)