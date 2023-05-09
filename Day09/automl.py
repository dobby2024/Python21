!pip install --upgrade numpy

!sudo apt-get install build-essential swig
!curl https://raw.githubusercontent.com/automl/auto-sklearn/master/requirements.txt | xargs -n 1 -L 1 pip install
!pip install auto-sklearn



import autosklearn.classification
import sklearn.model_selection
import sklearn.datasets
import sklearn.metrics
import joblib

# 데이터 로딩
X, y = sklearn.datasets.load_iris(return_X_y=True)

# train, test 데이터셋 분리
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, random_state=1)

# Auto-Sklearn 모델 생성
automl = autosklearn.classification.AutoSklearnClassifier(
    time_left_for_this_task=120,  # 2분동안 실행
    per_run_time_limit=30,  # 각각의 모델은 30초 동안 실행
)

# 모델 학습
automl.fit(X_train, y_train)

# 모델 예측
y_pred = automl.predict(X_test)

# 정확도 출력
print("Accuracy score:", sklearn.metrics.accuracy_score(y_test, y_pred))

# 최적 모델 출력
print("Best model:", automl.show_models())

# 모델 저장
joblib.dump(automl, "autosklearn_model.joblib")





'''
import joblib

# 모델 불러오기
loaded_model = joblib.load("autosklearn_model.joblib")

# 새로운 데이터 예측
new_data = [[5.1, 3.5, 1.4, 0.2], [6.2, 3.4, 5.4, 2.3]]
predictions = loaded_model.predict(new_data)

# 예측 결과 출력
print(predictions)

'''