#训练y=0.1x+0.3

import tensorflow as tf
import numpy as np

#crate data
x_data=np.random.rand(100).astype(np.float32)
y_data=x_data*0.1+0.3

###crate tensorflow structure start

Weights=tf.Variable(tf.random_uniform([1],-1,1))
biases=tf.Variable(tf.zeros([1]))

y=Weights*x_data+biases

loss=tf.reduce_mean(tf.square(y-y_data))
optimizer=tf.train.GradientDescentOptimizer(0.5)
train=optimizer.minimize(loss)

init=tf.initialize_all_variables()
###crate tensorflow structure end

sess=tf.Session()
sess.run(init)

for step in range(201):
    sess.run(train)
    if step%20==0:
        print(step,sess.run(Weights),sess.run(biases))

'''
0 [0.4364684] [0.150761]
20 [0.18556574] [0.25111604]
40 [0.12302695] [0.28684464]
60 [0.10619689] [0.2964597]
80 [0.10166769] [0.29904726]
100 [0.1004488] [0.29974362]
120 [0.10012081] [0.299931]
140 [0.10003253] [0.29998142]
160 [0.10000876] [0.299995]
180 [0.10000235] [0.29999867]
200 [0.10000064] [0.29999965]
'''