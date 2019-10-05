class BreastCancer:
    def __init__(self):
        pass

    def execute(self):
        import sklearn
        from sklearn.tree import DecisionTreeClassifier
        import sklearn.datasets
        from sklearn.datasets import load_breast_cancer
        from sklearn.model_selection import train_test_split #train과 분리 하는 것은 지도학습을 의미
        cancer = load_breast_cancer()
        X_train, X_test, y_train, y_test = train_test_split(
            cancer.data, cancer.target, stratify=cancer.target, random_state=42 #42번째 값을 가져온다
        ) #대문자 X는 확률 변수(덩어리로 들어간다) 소문자는 한개의 값 출력
        tree = DecisionTreeClassifier(random_state=0) #암이냐 아니냐를 예측하는 것이기 때문에 군집화 이용
        tree.fit(X_train, y_train)
        print('훈련세트의 정확도 : {:.3f}'.format(tree.score(X_train, y_train)))
        print('테스트세트의 정확도 : {:.3f}'.format(tree.score(X_test, y_test)))
        """
        독립변수의 개수가 많은 빅데이터에서는 과최적화가 쉽게 발생한다.
        
        """



