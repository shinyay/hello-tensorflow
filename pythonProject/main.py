# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def first_tensorflow():
    import tensorflow as tf
    import numpy as np

    from tensorflow.keras import Sequential
    from tensorflow.keras.layers import Dense

    model = Sequential([Dense(units=1, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')

    xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0])
    ys = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0])

    model.fit(xs, ys, epochs=500)

    print(model.predict([10.0]))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    first_tensorflow()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/