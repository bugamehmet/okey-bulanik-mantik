import pandas as pd
import matplotlib.pyplot as plt
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
data["class_encoded"] = data["class_encoded"].astype("str")

train_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_dataframe(
    dataframe=data,
    directory="/Users/mehmet/PycharmProjects/okey/train/",
    x_col="filename",
    y_col="class_encoded",
    target_size=(640, 640),
    batch_size=16,
    class_mode="categorical"
)

validation_generator = validation_datagen.flow_from_dataframe(
    dataframe=data,
    directory="/Users/mehmet/PycharmProjects/okey/train/",
    x_col="filename",
    y_col="class_encoded",
    target_size=(640, 640),
    batch_size=16,
    class_mode="categorical"
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
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Dense(75, activation='softmax'))
model.summary()

model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

history = model.fit(
    train_generator,
    epochs=3,
)

# Eğitim ve doğrulama kayıp grafiği
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

model.save('model_with_weights.keras')