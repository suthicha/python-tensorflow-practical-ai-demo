import tensorflow as tf

a = tf.random_normal([2, 2], mean=0.0, stddev=1.0, dtype=tf.float32)
b = tf.truncated_normal([2, 2], mean=0.0, stddev=1.0, dtype=tf.float32)
c = tf.random_uniform([2, 2], minval=0, maxval=None, dtype=tf.float32)
d = tf.random_shuffle([12, 35, 64, 5, 16])

with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(a), session.run(b), session.run(c), session.run(d))


# close the writer when we have done.
writer.close()

