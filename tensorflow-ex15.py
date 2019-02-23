import tensorflow as tf

t_0 = 19

t_1 = [b"apple", b"peach", b"grape"]

t_2 = [[True, False, False], [False, False, True], [False, True, False]]

with tf.Session() as session:
    writer = tf.summary.FileWriter('./graphs', session.graph)
    # print(session.run(tf.zeros_like(t_0)))
    # print(session.run(tf.ones_like(t_0)))
    # print(session.run(tf.zeros_like(t_1)))
    # print(session.run(tf.ones_like(t_1)))
    print(session.run(tf.zeros_like(t_2)))
    print(session.run(tf.ones_like(t_2)))


# close the writer when we have done.
writer.close()

