import tensorflow as tf

# placeholder 정의 - (1)
a = tf.placeholder(tf.int32, [None]) # 배열의 크기를 None으로 지정

# 배열의 모든 값을 10배하는 연산 정의 - (2)
b = tf.constant(10)
x10_op = a * b

# 세션 시작 - (3)
sess = tf.Session()

# placeholder에 값을 넣어 실행 - (4)
r1 = sess.run(x10_op, feed_dict={a: [1, 2, 3, 4, 5]})
print(r1)
r2 = sess.run(x10_op, feed_dict={a: [10, 20]})
print(r2)