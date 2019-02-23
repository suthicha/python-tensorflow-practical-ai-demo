import tensorflow as tf

# create a variable whose original value is 2.
a = tf.Variable(2, name="scalar")

# assign a * 2 to a and call that op a_times_two
a_times_two = a.assign(a * 2)

init = tf.global_variables_initializer()

with tf.Session() as session:
    session.run(init)
    writer = tf.summary.FileWriter('./graphs', session.graph)
    print(session.run(a_times_two))
    print(session.run(a_times_two))
    print(session.run(a_times_two))

writer.close()

