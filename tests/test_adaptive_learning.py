# test_adaptive_learning.py

import unittest
from adaptive_learning import AdaptiveLearningSystem

class TestAdaptiveLearningSystem(unittest.TestCase):
    
    def setUp(self):
        """
        Set up the test environment for adaptive learning.
        This will be called before each test.
        """
        self.adaptive_system = AdaptiveLearningSystem()

    def test_initial_conditions(self):
        """
        Test the initial conditions of the adaptive learning system.
        It should start with an empty model and no previous learning.
        """
        print("Testing initial conditions...")
        self.assertEqual(len(self.adaptive_system.model), 0, "The model should start empty.")
        self.assertEqual(self.adaptive_system.learning_rate, 0.1, "The learning rate should be 0.1 by default.")
    
    def test_learn_from_data(self):
        """
        Test that the system learns from a single set of data points.
        The model should adapt based on this new data.
        """
        print("Testing learning from data...")
        # Simulate a data input with simple features and labels
        training_data = [
            {"features": [1, 2], "label": 3},
            {"features": [4, 5], "label": 9},
            {"features": [7, 8], "label": 15},
        ]
        
        # Learning from the data
        self.adaptive_system.learn(training_data)
        
        # Ensure that the model has learned something
        self.assertGreater(len(self.adaptive_system.model), 0, "The model should have learned after training.")
        
        # Validate the model's first prediction based on the training data
        predicted = self.adaptive_system.predict([6, 7])  # Should be around 12
        self.assertAlmostEqual(predicted, 12, delta=2, msg="The prediction should be near the expected value.")
    
    def test_adaptation_to_new_data(self):
        """
        Test the adaptive learning system's ability to adapt to new data.
        The model should refine its predictions as more data is provided.
        """
        print("Testing adaptation to new data...")
        # Initial training data
        initial_data = [
            {"features": [1, 2], "label": 3},
            {"features": [4, 5], "label": 9}
        ]
        
        # Learning from initial data
        self.adaptive_system.learn(initial_data)
        
        # Test prediction before new data
        predicted_before = self.adaptive_system.predict([6, 7])
        self.assertAlmostEqual(predicted_before, 12, delta=2, msg="Prediction before learning should be around 12.")
        
        # Now, let's add more data to adapt the model
        new_data = [
            {"features": [7, 8], "label": 15},
            {"features": [10, 11], "label": 21}
        ]
        
        # Learn from new data
        self.adaptive_system.learn(new_data)
        
        # Test prediction after new learning
        predicted_after = self.adaptive_system.predict([6, 7])
        self.assertGreater(abs(predicted_after - 12), 0, msg="The system should have adapted its model after new data.")
    
    def test_learning_rate_update(self):
        """
        Test that the learning rate is being updated correctly as the system learns.
        """
        print("Testing learning rate update...")
        
        # Simulate learning over time
        initial_rate = self.adaptive_system.learning_rate
        self.adaptive_system.learn([{"features": [1, 1], "label": 2}])
        updated_rate = self.adaptive_system.learning_rate
        
        # Check that the learning rate was updated based on the learning process
        self.assertNotEqual(initial_rate, updated_rate, "The learning rate should be updated as learning progresses.")
    
    def test_large_scale_data(self):
        """
        Test how the system handles learning from a large amount of data.
        The system should adapt without errors or performance issues.
        """
        print("Testing learning from large-scale data...")
        
        # Generate large data (e.g., 1000 data points)
        large_data = [{"features": [i, i+1], "label": 2 * (i + 1)} for i in range(1000)]
        
        # Learn from the large data
        self.adaptive_system.learn(large_data)
        
        # Test prediction on a sample
        predicted = self.adaptive_system.predict([100, 101])  # Should predict 202
        self.assertAlmostEqual(predicted, 202, delta=5, msg="Prediction after learning from large data should be close to 202.")
    
    def test_invalid_data(self):
        """
        Test the system's ability to handle invalid data gracefully.
        It should raise an appropriate error or handle the data without crashing.
        """
        print("Testing handling of invalid data...")
        
        # Simulate invalid data (non-numeric, missing labels)
        invalid_data = [
            {"features": ["a", "b"], "label": "c"},
            {"features": None, "label": 9},
            {"features": [4, 5], "label": None}
        ]
        
        # Attempt to learn from invalid data
        try:
            self.adaptive_system.learn(invalid_data)
            self.fail("The system should raise an error when learning from invalid data.")
        except ValueError as e:
            print("Caught expected error:", e)
    
    def tearDown(self):
        """
        Clean up after each test.
        This will be called after each test.
        """
        print("Cleaning up after test...")
        self.adaptive_system = None


if __name__ == "__main__":
    # Run all the tests
    unittest.main()
