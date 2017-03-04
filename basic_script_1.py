import tensorflow as tf

x = tf.constant([10, 20, 30], name = 'x')
y = tf.Variable(x + 10, name = 'y')

model = tf.global_variables_initializer()

with tf.Session() as session:
	session.run(model)
	print session.run(y)

