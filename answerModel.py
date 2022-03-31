from tensorflow import keras
import keras.models as models
import re
import tensorflow as tf
import numpy as np

print(tf.__version__)

class PositionalEncoding(tf.keras.layers.Layer):
      def __init__(self, position, d_model, **kwargs):
        super(PositionalEncoding, self).__init__()
        self.pos_encoding = self.positional_encoding(position, d_model)

      def get_angles(self, position, i, d_model):
        angles = 1 / tf.pow(10000, (2 * (i // 2)) / tf.cast(d_model, tf.float32))
        return position * angles

      def positional_encoding(self, position, d_model):
        angle_rads = self.get_angles(
            position=tf.range(position, dtype=tf.float32)[:, tf.newaxis],
            i=tf.range(d_model, dtype=tf.float32)[tf.newaxis, :],
            d_model=d_model)

        # 배열의 짝수 인덱스(2i)에는 사인 함수 적용
        sines = tf.math.sin(angle_rads[:, 0::2])

        # 배열의 홀수 인덱스(2i+1)에는 코사인 함수 적용
        cosines = tf.math.cos(angle_rads[:, 1::2])

        angle_rads = np.zeros(angle_rads.shape)
        angle_rads[:, 0::2] = sines
        angle_rads[:, 1::2] = cosines
        pos_encoding = tf.constant(angle_rads)
        pos_encoding = pos_encoding[tf.newaxis, ...]

        print(pos_encoding.shape)
        return tf.cast(pos_encoding, tf.float32)

      def call(self, inputs):
        return inputs + self.pos_encoding[:, :tf.shape(inputs)[1], :]

model = keras.models.load_model('C:/Users/MJ/Desktop/0325_default.h5/0325_default.h5', custom_objects={'PositionalEncoding':PositionalEncoding})

# json_file = open('model.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# loaded_model = models.model_from_json(loaded_model_json)

# loaded_model.load_weights('0325_default.h5')

# def preprocess_sentence(sentence):
#   sentence = re.sub(r"([?.!,])", r" \1 ", sentence)
#   sentence = sentence.strip()
#   return sentence

# def evaluate(sentence):
#   sentence = preprocess_sentence(sentence)

#   sentence = tf.expand_dims(
#       loaded_model.START_TOKEN + loaded_model.tokenizer.encode(sentence) + loaded_model.END_TOKEN, axis=0)

#   output = tf.expand_dims(loaded_model.START_TOKEN, 0)

#   # 디코더의 예측 시작
#   for i in range(loaded_model.MAX_LENGTH):
#     predictions = model(inputs=[sentence, output], training=False)

#     # 현재(마지막) 시점의 예측 단어를 받아온다.
#     predictions = predictions[:, -1:, :]
#     predicted_id = tf.cast(tf.argmax(predictions, axis=-1), tf.int32)

#     # 만약 마지막 시점의 예측 단어가 종료 토큰이라면 예측을 중단
#     if tf.equal(predicted_id, loaded_model.END_TOKEN[0]):
#       break

#     # 마지막 시점의 예측 단어를 출력에 연결한다.
#     # 이는 for문을 통해서 디코더의 입력으로 사용될 예정이다.
#     output = tf.concat([output, predicted_id], axis=-1)

#   return tf.squeeze(output, axis=0)


# def predict(sentence):
#   prediction = evaluate(sentence)

#   predicted_sentence = loaded_model.tokenizer.decode(
#       [i for i in prediction if i < loaded_model.tokenizer.vocab_size])

#   print('Input: {}'.format(sentence))
#   print('Output: {}'.format(predicted_sentence))

#   return predicted_sentence