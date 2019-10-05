import tensorflow as tf

class CalculatorModel:
    def __init__(self):
        pass

    def create_add_model(self):
        #텐서플로우에서 변수 2개 선언
        #placeholder - 변수
        #virable -> 텐서플로 내부에서 사용하는 변수
        w1 = tf.placeholder(tf.float32, name='w1')
        w2 = tf.placeholder(tf.float32, name='w2')
        #json과 1대1로 대응
        #int a = 3 과 같이 초기화 작업하는 것
        #op_add라는 모델명으로 w1과w2를 더하여 10.0이 나오는 경우를 모델로 준 것
        #mpa자료형과 비슷(딕셔너리)
        feed_dict = {'w1':8.0, 'w2':2.0}
        r = tf.add(w1, w2, name='op_add')
        sess = tf.Session()
        #임시변수
        _ = tf.Variable(initial_value='fake_variable')
        #전역변수 선언
        sess.run(tf.global_variables_initializer())
        #저장작업
        saver = tf.train.Saver()
        result = sess.run(r, {w1 : feed_dict['w1'], w2 : feed_dict['w2']})
        print('TF 덧셈결과:{}'.format(result))
        #10이 나오는 덧셈 연산을 1000번 해라
        saver.save(sess, './saved_add_model/model', global_step=1000)

    def create_min_model(self):
        w1 = tf.placeholder(tf.float32, name='w1')
        w2 = tf.placeholder(tf.float32, name='w2')
        feed_dict={'w1': 10.0, 'w2':2.0}
        #마이너스 -> subtract
        r = tf.subtract(w1, w2, name='op_min')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(r, {w1 : feed_dict['w1'], w2 : feed_dict['w2']})
        saver.save(sess, './saved_min_model/model', global_step=1000)

    def create_mul_model(self):
        w1 = tf.placeholder(tf.float32, name='w1')
        w2 = tf.placeholder(tf.float32, name='w2')
        feed_dict = {'w1': 10.0, 'w2': 2.0}
        # 마이너스 -> subtract
        r = tf.multiply(w1, w2, name='op_mul')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        saver.save(sess, './saved_mul_model/model', global_step=1000)

    def create_div_model(self):
        w1 = tf.placeholder(tf.float32, name='w1')
        w2 = tf.placeholder(tf.float32, name='w2')
        feed_dict = {'w1': 10.0, 'w2': 2.0}
        # 마이너스 -> subtract
        r = tf.divide(w1, w2, name='op_div')
        sess = tf.Session()
        _ = tf.Variable(initial_value='fake_variable')
        sess.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        result = sess.run(r, {w1: feed_dict['w1'], w2: feed_dict['w2']})
        saver.save(sess, './saved_div_model/model', global_step=1000)