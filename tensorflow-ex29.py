import tensorflow as tf

W = tf.Variable(10)

sess1 = tf.Session()
sess2 = tf.Session()

sess1.run(W.initializer)
sess2.run(W.initializer)

print(sess1.run(W.assign_add(10)))
print(sess2.run(W.assign_sub(2)))

print(sess1.run(W.assign_add(100)))
print(sess2.run(W.assign_sub(50)))

# with tf.Session() as session:
#     session.run(W.initializer)
#     writer = tf.summary.FileWriter('./graphs', session.graph)
#     print(session.run(W.assign_add(10)))
#     print(session.run(W.assign_add(2)))
#
# writer.close()

