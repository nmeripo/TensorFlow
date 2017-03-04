import tensorflow as tf

a = tf.placeholder("float") # Create a symbolic variable 'a'
b = tf.placeholder("float") # Create a symbolic variable 'b'

c = tf.multiply(a, b)

with tf.Session() as session:
	print '{} should equal 2.0'.format(session.run(c, feed_dict={a: 1, b: 2}))
