import tensorflow as tf
from keras import layers, models

def train_and_save_model():
    # 1. Load MNIST dataset
    print("Loading data...")
    mnist = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # 2. Preprocess: Scale pixels to [0, 1] and reshape for CNN (28x28x1)
    x_train = x_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0
    x_test = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0

    # 3. Build a Simple CNN
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])

    # 4. Compile
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    # 5. Train
    print("Training model...")
    model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

    # 6. Save the model for FastAPI
    model.save("./model/mnist_model.h5")
    print("Model saved as mnist_model.h5")

if __name__ == "__main__":
    train_and_save_model()