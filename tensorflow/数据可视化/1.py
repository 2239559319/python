import tensorflow as tf
import numpy as np

x_data=np.linspace(-1,1,300)[:,np.newaxis]
noise=np.random.normal(0,0.05,x_data.shape)
y_data=np.square(x_data)-0.5

with tf.name_scope('inputs'):
    xs=tf.placeholder(tf.float32,[None,1],name='x_input')
    ys=tf.placeholder(tf.float32,[None,1],name='y_input')

def add_layer(inputs,in_size,outsize,activation_function=None):             #添加神经层
    with tf.name_scope('layer'):
        with tf.name_scope('Weights'):
            Weights=tf.Variable(tf.random_normal([in_size,outsize]),name="W")
        with tf.name_scope('biases'):
            biases=tf.Variable(tf.zeros([1,outsize])+1,name='b')
        with tf.name_scope('Wx_plus_b'):
            Wx_plus_b=tf.matmul(inputs,Weights)+biases

        if activation_function is None:
            return Wx_plus_b
        else:
            return activation_function(Wx_plus_b)

l1=add_layer(xs,1,10,activation_function=tf.nn.relu)
prediction=add_layer(l1,10,1,activation_function=None)

with tf.name_scope('loss'):
    loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))
with tf.name_scope('train'):
    train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init=tf.initialize_all_variables()
sess=tf.Session()
writer=tf.summary.FileWriter("logs/",sess.graph)            #数据可视化，tensorboard --logdir=logs
sess.run(init)

for i in range(1000):           #训练
    sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
    if i%50==0:
        print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))