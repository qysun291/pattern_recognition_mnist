figure文件夹中包含本次作业中的一些图片；
input文件夹中为训练集和测试集的csv文件，由于文件比较大没有上传，想运行程序可以在Kaggle上下载，放入input文件夹中即可；
mnist文件夹中为一些程序。包含data_prepare.py和mnist.py，data_prepare.py为数据预处理，mnist.py为神经网络搭建及一些画图的程序；
loss.txt为训练50个epoch的损失和精度；
mnist_test.csv为最终上传的预测结果。

进入mnist文件夹运行mnist.py即可得结果，运行的结果都会存储在mnist文件夹下。
本程序在tensorflow 1.13.1 + cuda 10.1 + cdunn7.6.1.34 + python3.7的环境下测试通过。
GPU为GTX 2080 Ti。
