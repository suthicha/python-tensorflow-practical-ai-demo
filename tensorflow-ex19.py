import tensorflow as tf

# create variable a with scalar value.
a = tf.Variable(2, name="scalar")

with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)
    session.run(a.initializer)
    print(session.run(a.value()))

writer.close()

