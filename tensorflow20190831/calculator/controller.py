import tensorflow as tf

class CalculatorController:
    def __init__(self, num1, num2, opcode):
        self._num1 = num1
        self._num2 = num2
        self._opcode= opcode

    def calc(self):
        n1 = self._num1
        n2 = self._num2
        opcode = self._opcode
        _meta = ''
        _checkPoint = ''
        print('app.py에서 받은 n1 = {}, n2 = {}, opcode = {}'.format(n1, n2, opcode))
        tf.reset_default_graph()
        #세션에 있는 모델 호출
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            #상대겨로가 인식 안된다
            #절대경로로 표시
            saver = tf.train.import_meta_graph('calculator/saved_'+ opcode +'_model/model-1000.meta')
            #checkpoint가 훈련에 대한 로그
            #가장 마지막로그를 가져오는 것

            saver.restore(sess, tf.train.latest_checkpoint('calculator/saved_' + opcode + '_model'))

            graph = tf.get_default_graph()
            #이름을 공유?
            w1 = graph.get_tensor_by_name('w1:0')
            w2 = graph.get_tensor_by_name('w2:0')
            feed_dict = {w1:float(n1), w2:float(n2)}
            #r = tf.subtract(w1, w2, name='op_add') 이 부분과 일치
            #name이 같으면 덮어쓰여진다?
            op_to_restore = graph.get_tensor_by_name('op_' + opcode + ':0')
            result = sess.run(op_to_restore, feed_dict)
            print('텐서가 계산한 결과 : {}'.format(result))
        return result