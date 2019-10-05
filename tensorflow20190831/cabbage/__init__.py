from cabbage.model import CabbageModel
import os
if __name__ == '__main__':
    cabb = CabbageModel()
    #리눅스에서 돌아간다
    #모델이 존재하지 않을경우만 실행한다.
    if not os.path.exists('saved_model/checkpoint'):
        cabb.create_model()
