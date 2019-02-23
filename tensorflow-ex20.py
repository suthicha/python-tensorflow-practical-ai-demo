import tensorflow as tf

init = tf.global_variables_initializer()

# create variables b as vector.
b = tf.Variable(2, name="scalar")

with tf.Session() as session:
    session.run(init)
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(b.value()))

writer.close()

