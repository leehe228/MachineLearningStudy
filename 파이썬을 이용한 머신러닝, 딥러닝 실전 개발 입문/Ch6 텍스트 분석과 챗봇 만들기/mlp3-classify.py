from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
from sklearn import model_selection, metrics
import json

# 입력 단어 수
max_words = 56681
# 카테고리 수
nb_classes = 6

# 배치 크기
batch_size = 64
# 학습 수
epoch = 20

# MLP 모델 생성 - (1)
def build_model():
    model = Sequential()
    model.add(Dense(512, input_shape=(max_words, )))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))
    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )
    return model

# 데이터 읽어들이기 - (2)
data = json.load(open("data-mini.json"))
X = data["X"]
Y = data["Y"]

# 학습하기 - (3)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y)
Y_train = np_utils.to_categorical(Y_train, nb_classes)
print(len(X_train), len(Y_train))

model = KerasClassifier(
    build_fn=build_model,
    nb_epoch=epoch,
    batch_size=batch_size
)
model.fit(X_train, Y_train)

# 예측하기 - (4)
y = model.predict(X_test)
ac_score = metrics.accuracy_score(Y_test, y)
cl_report = metrics.classification_report(Y_test, y)
print("정답률 :", ac_score)
print("리포트 :\n", cl_report)
