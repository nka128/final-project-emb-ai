import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    '''
    A class to test the functionality of the EmotionDetection
    package
    '''
    def test_emotion_detector(self):
        '''
        This is a test function for the emotion_detector function
        in EmotionDetection package
        '''
        response = emotion_detector("I am glad this happend")
        self.assertEqual(response['dominant_emotion'], "joy")

        response = emotion_detector("I am really mad about this")
        self.assertEqual(response['dominant_emotion'], "anger")

        response = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(response['dominant_emotion'], "disgust")

        response = emotion_detector("I am sad about this")
        self.assertEqual(response['dominant_emotion'], "sadness")

        response = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(response['dominant_emotion'], "fear")

if __name__ == "__main__":
    unittest.main()