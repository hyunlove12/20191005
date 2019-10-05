class Mammal:
    def __init__(self):
        pass

    def execute(self):
        import tensorflow as tf
        import numpy as np
        # [털, 날개] 털과 날개라는 feature를 이용하여 포유류나 조류냐를 판단
        # 기타, 포유류, 조류로 분류 하여라 (feature는 2개) -> 확률변수 y로 변경
        """
        원 핫 인코딩
        0 -> 없음
             [0, 0] -> [1, 0, 0] 기타 -> 털, 날개 없음
             [1, 0] -> [0, 1, 0] 포유류
             [1, 1] -> [0, 0, 1] 조류             
             [0, 0] -> [1, 0, 0] 기타
             [0, 0] -> [1, 0, 0] 기타
             [0, 1] -> [0, 0, 1] 조류
        
        """
        #학습 데이터
        x_data = np.array(
            [
             [0, 0],
             [1, 0],
             [1, 1],
             [0, 1],
             [0, 0],
             [0, 1]
             ]
        )
        # 학습 데이터 -> x에 대한 y값
        y_data = np.array(
            [
             [1, 0, 0],
             [0, 1, 0],
             [0, 0, 1],
             [1, 0, 0],
             [1, 0, 0],
             [0, 0, 1]
            ]
        )
        X = tf.placeholder(tf.float32)  #외부에서 주입되는 값은 placeholder
        Y = tf.placeholder(tf.float32)
        W = tf.Variable(tf.random_uniform([2, 3], -1, 1.))             #가중치 variable은 내부에서 결정
        # -1 -> all
        # 신경망 neural network 앞으로는 nn 으로표기
        # nn은 2차원으로 [입력층(특성), 출력층(레이블)] -> [2,3] 으로 정합니다.
        b = tf.Variable(tf.zeros([3])) #내부에서 결정 #y = wx + b x,b 는 플레이스홀더
        # b는 편향 bias
        # W는 가중치 weight
        # b는 각 레이어의 아웃풋 갯수로 설정함
        # b는 최종 결과값의 분류갯수인 3으로 설정함

        L = tf.add(tf.matmul(X, W), b) # WX + b 한개의 뉴런
        #가중치와 편향을 이용해 계산한 결과 값에
        L = tf.nn.relu(L) #인공망 추가 #활성화 함수 #nn인공 신경마 하나가 된다. 뉴런의 망에 위의 데이터를 입력하는 것 -> 각각의 자리에 대입
        model = tf.nn.softmax(L) #추가하는 것
        """
            softmax 소프트맥스 함수는 다음 처럼 결과값을 전체 합이 1인 확률로 만들어 주는 함수 // 가중치를 결정 하기 위한 것 // 임의로 조절 가능
            예) [8.04, 2.76, -6.52] -> [0.53, 0.24, 0.23] #스케일링
        """

        #학습을 하지 않은 상태
        print('---- 모델 내부 보기 ----')
        print(model)
        cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(model), axis = 1))
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
        train_op = optimizer.minimize(cost)
        # 비용함수를 최소화 시키면 (=경사도를 0으로 만들면) 그 값이 최적화 된 값이다.
        init = tf.global_variables_initializer()
        sess = tf.Session()
        sess.run(init)
        for step in range(100): #학습 시키는 횟수
            sess.run(train_op, {X: x_data, Y:y_data})
            if(step + 1) % 10 == 0:
                print(step + 1, sess.run(cost, {X : x_data, Y : y_data}))

        #결과 확인
        prediction = tf.argmax(model, 1) #현재 모델
        target = tf.argmax(Y, 1) # arg_max옛날 모델
        print('예측값', sess.run(prediction, {X: x_data}))
        print('실제값', sess.run(target, {Y: y_data}))
        # tf.argmax : 예측값과 실제값의 행렬에서 tf.argmax를 이용해 가장 큰 값을 가져옴
        # 예) [[0, 1, 1][1, 0, 0]] -> [1, 0]
        #[[0.2, 0.7, 0.1][0.9, 0.1, 0.]] -> [1, 0]
        is_correct = tf.equal(prediction, target)
        accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
        print('정확도 : %.2f' % sess.run(accuracy * 100, {X : x_data, Y: y_data}))








