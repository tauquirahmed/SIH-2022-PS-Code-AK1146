import numpy as np
import cv2
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA

def mask():
        with_mask = np.load('with_mask.npy', allow_pickle=True)
        without_mask = np.load('without_mask.npy', allow_pickle=True)

        wm = with_mask.shape
        wtm = without_mask.shape

        with_mask = with_mask.reshape(wm[0], 7500)
        without_mask = without_mask.reshape(wtm[0], 7500)

        X = np.r_[with_mask, without_mask]

        labels = np.zeros(X.shape[0])
        labels[202:] = 1.0
        names = {0: 'Mask', 1: 'No Mask'}

        x_train, x_test, y_train, y_test = train_test_split(X, labels, test_size=0.25)

        pca = PCA(n_components=3)
        x_train = pca.fit_transform(x_train)

        
        x_train, x_test, y_train, y_test = train_test_split(X, labels, test_size=0.20)

        svm = SVC()
        svm.fit(x_train, y_train)

        # x_test = pca.transform(x_test)
        y_pred = svm.predict(x_test)

        accuracy_score(y_test, y_pred)

        haar_data = cv2.CascadeClassifier('data.xml')

        capture = cv2.VideoCapture(0)
        data = []
        font = cv2.FONT_HERSHEY_DUPLEX
        while True:
            flag, img = capture.read()
            if flag:
                faces = haar_data.detectMultiScale(img)
                for x, y, w, h in faces:
                    face = img[y:y+h, x:x+w, :]
                    face = cv2.resize(face, (50, 50))
                    face = face.reshape(1, -1)
                    # face = pca.transform(face)
                    pred = svm.predict(face)#[0]
                    n = names[int(pred)]
                    if int(pred)==0:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
                        cv2.putText(img, n, (x, y), font, 1, (0, 255, 0), 2)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 4)
                        cv2.putText(img, n, (x, y), font, 1, (0, 0, 255), 2)
                    print(n)
                    cv2.resize(face, (50, 50))
                cv2.imshow('result', img)
                if cv2.waitKey(2) == 27:
                    break
        capture.release()
        cv2.destroyAllWindows()



