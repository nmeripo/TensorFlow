import numpy as np 
import tensorflow as tf

x = np.random.randint(1000, size = 10000)
y = tf.Variable(5 * pow(x, 2) - 3 * x + 15, name = 'y')

model = tf.global_variables_initializer()

with tf.Session() as session:
	session.run(model)
	print session.run(y)
