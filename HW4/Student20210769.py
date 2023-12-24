import os
import sys
import numpy as np
import operator

# 데이터 불러오기
def createDataSet(folder_name):
        group_tmp = []
        labels = [] # 각 데이터와 매칭되는 라벨 리스트
        file_list = os.listdir(folder_name)
        for i in range(len(file_list)):
                file_name = os.path.join(folder_name, file_list[i])
                fileNm_split = file_name.split('/')
                labels.append(fileNm_split[-1].split('_')[0])
                data = ""
                list = []
                with open(file_name, 'r') as file:
                        data = file.read().replace('\n', '').strip()
                        for ch in data:
                                list.append(int(ch))
                group_tmp.append(list)
        group = np.array(group_tmp) # 배열 생성
        return group, labels

# 거리 계산
def classify0(inX, dataSet, labels, k):
        dataSetSize = dataSet.shape[0]
        diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
        sqDiffMat = diffMat ** 2
        sqDistances = sqDiffMat.sum(axis = 1)
        sortedDistIndicies = sqDistances.argsort()
        classCount = {}
        for i in range(k):
                voteIlabel = labels[sortedDistIndicies[i]]
                classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
        return sortedClassCount[0][0]

# 에러율 계산 - 인식한 결과와 실제 라벨을 비교
def compare_predictions(predicted_result, labels):
        cnt = 0 # 예측을 실패한 경우
        file_cnt = len(predicted_result)
        for i in range(file_cnt):
                if (predicted_result[i] != labels[i]):
                        cnt += 1
        result = round(cnt / file_cnt * 100)
        return result

# Main
training_folder = sys.argv[1]
test_folder = sys.argv[2]

train_group, train_labels = createDataSet(training_folder)
test_group, labels = createDataSet(test_folder)

# 거리 계산, 에러율 계산
result = []
for i in range(1, 21):
        pred_labels = []
        for j in range(len(test_group)):
                pred_labels.append(classify0(test_group[j], train_group, train_labels, i))
        result.append(compare_predictions(pred_labels, labels))

# 에러율 출력
for err_rate in result:
        print(err_rate)