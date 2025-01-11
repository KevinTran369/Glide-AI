# test_feedback_loop.py

import unittest
from feedback_loop import FeedbackLoop
from decision_maker import DecisionMaker

class TestFeedbackLoop(unittest.TestCase):
    
    def setUp(self):
        """
        Set up the test environment for the feedback loop.
        This will be called before each test.
        """
        self.decision_maker = DecisionMaker()  # Create a DecisionMaker instance for feedback loop testing
        self.feedback_loop = FeedbackLoop(self.decision_maker)

    def test_initial_conditions(self):
        """
        Test the initial conditions of the feedback loop.
        The system should have no feedback processed initially.
        """
        print("Testing initial conditions...")
        self.assertEqual(len(self.feedback_loop.feedback_history), 0, "The feedback history should start empty.")
        self.assertEqual(self.feedback_loop.performance_data, {}, "The performance data should start empty.")

    def test_process_feedback(self):
        """
        Test that feedback is correctly processed by the feedback loop and updates the system's performance.
        """
        print("Testing feedback processing...")
        
        # Example feedback after a decision
        feedback_data = {
            "action": "recommendation_accepted",  # Hypothetical action taken by the system
            "performance_score": 0.85            # Hypothetical feedback score
        }
        
        # Process feedback and ensure the performance data is updated
        self.feedback_loop.process_feedback(feedback_data)
        
        # Check that the feedback has been recorded
        self.assertIn("action", self.feedback_loop.feedback_history[0], "The feedback should include an action.")
        self.assertIn("performance_score", self.feedback_loop.feedback_history[0], "The feedback should include a performance score.")
        
        # Check that performance data is updated
        self.assertEqual(self.feedback_loop.performance_data["recommendation_accepted"], 0.85, "The performance score for the action should be updated correctly.")

    def test_adaptive_learning_with_feedback(self):
        """
        Test the system's ability to adapt its decision-making based on feedback over multiple iterations.
        The feedback loop should refine decision-making to improve performance over time.
        """
        print("Testing adaptive learning with feedback...")
        
        # Initial decision input and feedback loop processing
        initial_input = {"sensor_data": 50, "context": "gaming"}
        decision = self.decision_maker.make_decision(initial_input)
        feedback_data = {"action": decision["action"], "performance_score": 0.70}
        self.feedback_loop.process_feedback(feedback_data)
        
        # Simulate an additional round of decision-making with new input
        new_input = {"sensor_data": 60, "context": "gaming"}
        new_decision = self.decision_maker.make_decision(new_input)
        
        # Check if the new decision is influenced by the feedback received
        self.assertNotEqual(decision["action"], new_decision["action"], "The decision should evolve based on feedback.")

    def test_feedback_loop_over_multiple_iterations(self):
        """
        Test that the feedback loop improves the system's performance over multiple iterations.
        The system should be able to refine its decisions and actions over time.
        """
        print("Testing feedback loop over multiple iterations...")
        
        feedback_data_1 = {"action": "recommendation_accepted", "performance_score": 0.70}
        feedback_data_2 = {"action": "recommendation_accepted", "performance_score": 0.85}
        feedback_data_3 = {"action": "recommendation_accepted", "performance_score": 0.90}
        
        # Process feedback multiple times
        self.feedback_loop.process_feedback(feedback_data_1)
        self.feedback_loop.process_feedback(feedback_data_2)
        self.feedback_loop.process_feedback(feedback_data_3)
        
        # Check that feedback history contains 3 entries
        self.assertEqual(len(self.feedback_loop.feedback_history), 3, "The feedback history should contain 3 feedback entries.")
        
        # Check that performance data is updated over time
        self.assertEqual(self.feedback_loop.performance_data["recommendation_accepted"], 0.90, "The performance score should improve over time.")

    def test_invalid_feedback(self):
        """
        Test the system's ability to handle invalid or malformed feedback gracefully.
        The system should ignore invalid feedback or raise an appropriate error.
        """
        print("Testing handling of invalid feedback...")
        
        invalid_feedback_1 = {"action": None, "performance_score": 0.8}  # Invalid action
        invalid_feedback_2 = {"action": "recommendation_accepted", "performance_score": None}  # Invalid performance score
        
        # Test with invalid feedback data
        try:
            self.feedback_loop.process_feedback(invalid_feedback_1)
            self.fail("The system should raise an error for feedback with an invalid action.")
        except ValueError as e:
            print("Caught expected error for invalid action:", e)
        
        try:
            self.feedback_loop.process_feedback(invalid_feedback_2)
            self.fail("The system should raise an error for feedback with an invalid performance score.")
        except ValueError as e:
            print("Caught expected error for invalid performance score:", e)

    def test_real_time_feedback_processing(self):
        """
        Test that feedback is processed in real-time and used to improve decisions on the fly.
        """
        print("Testing real-time feedback processing...")
        
        real_time_feedback = [
            {"action": "recommendation_accepted", "performance_score": 0.60},
            {"action": "recommendation_accepted", "performance_score": 0.80},
            {"action": "recommendation_accepted", "performance_score": 0.90},
        ]
        
        # Process feedback in real-time
        for feedback in real_time_feedback:
            self.feedback_loop.process_feedback(feedback)
            self.assertIn("action", self.feedback_loop.feedback_history[-1], "Real-time feedback should contain an action.")
            self.assertIn("performance_score", self.feedback_loop.feedback_history[-1], "Real-time feedback should contain a performance score.")
        
        # Check if the performance score evolves over time
        self.assertEqual(self.feedback_loop.performance_data["recommendation_accepted"], 0.90, "The performance score should evolve based on real-time feedback.")
    
    def tearDown(self):
        """
        Clean up after each test.
        This will be called after each test.
        """
        print("Cleaning up after test...")
        self.feedback_loop = None
        self.decision_maker = None


if __name__ == "__main__":
    # Run all the tests
    unittest.main()
