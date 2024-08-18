#import required libraries

import unittest

from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector("I am glad this happened joy")
        self.assertEqual(result_1['max_emotion'],'joy')
        result_1 = emotion_detector("I am really mad about this")
        self.assertEqual(result_1['max_emotion'],'anger')
        result_1 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result_1['max_emotion'],'disgust')
        result_1 = emotion_detector("I am so sad about this")
        self.assertEqual(result_1['max_emotion'],'sadness')
        result_1 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result_1['max_emotion'],'fear')
        
unittest.main()


