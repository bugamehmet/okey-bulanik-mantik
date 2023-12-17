import pandas as pd
import numpy as np
import keras
import cv2
import tensorflow
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator
from sklearn.preprocessing import LabelEncoder
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Dense, BatchNormalization, Flatten
import glob



# CSV dosyalarını oku ve birleştir
filenames = glob.glob("/Users/mehmet/PycharmProjects/okey/train/_annotations.csv")
data_list = [pd.read_csv(filename) for filename in filenames]
data = pd.concat(data_list)

# Etiketleri encode et
label_encoder = LabelEncoder()
data["class_encoded"] = label_encoder.fit_transform(data["class"])

# Eğitim ve doğrulama bölünmesini tanımla
x_train, x_val, y_train, y_val = train_test_split(
    data[["filename", "xmin", "ymin", "xmax", "ymax"]],
    data["class_encoded"],
    test_size=0.3,
    random_state=42,
)


# Modeli oluştur
model = Sequential()
model.add(Conv2D(16, (3,3), activation='relu', input_shape=(640, 640, 3)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Conv2D(32, (3,3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Conv2D(128, (3,3), activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Dense(75, activation='softmax'))
model.summary()

optimizer = keras.optimizers.legacy.Adam()
model.compile(loss='sparse_categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

train_datagen = ImageDataGenerator(rescale=1./255)
train_generator = train_datagen.flow_from_dataframe(
    dataframe=data,
    directory="/Users/mehmet/PycharmProjects/okey/train/",
    x_col="filename",
    y_col="class_encoded",
    target_size=(640, 640),
    batch_size=32,
    class_mode="raw"  # raw kullanarak sparse_categorical_crossentropy'ı
)

# Modeli eğit
history = model.fit(
    train_generator,
    epochs=1,
    validation_data=(x_val, y_val)
)

# Eğitim ve doğrulama kayıp grafiği
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Eğitim ve doğrulama doğruluk grafiği
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

model.save('model_with_weights.keras')