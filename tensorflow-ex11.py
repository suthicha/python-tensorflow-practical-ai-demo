import tensorflow as tf

# 'start' is 3, 'limit' is 18, 'delta' is 3
a = tf.range(3, 18, 3)

# 'start' is 3, 'limit' is 1,  'delta' is -0.5
b = tf.range(3, 1, -0.5)

# limit is 5
c = tf.range(5)


with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(a), session.run(b), session.run(c))

# close the writer when we have done.
writer.close()

