import tensorflow as tf

session = tf.InteractiveSession()

a = tf.constant(5.0)
b = tf.constant(6.0)
c = a * b

print(c.eval())

session.close()

# with tf.Session() as session:
#     session.run(W.initializer)
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     print(session.run(W.assign_add(10)))
#     print(session.run(W.assign_add(2)))
#
# writer.close()

