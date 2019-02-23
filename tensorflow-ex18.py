import tensorflow as tf

# create variable a with scalar value.
a = tf.Variable(2, name="scalar")

# create variable b as a vector.
b = tf.Variable([2, 3], name="vector")

# create variable c as a 2x2 matrix.
c = tf.Variable([0, 1], [2, 3], name="matrix")

# create variable W as 784 x 10 tensor, filled with zeros.
W = tf.Variable(tf.zeros([784, 10]))

with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)

