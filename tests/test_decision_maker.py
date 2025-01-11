# test_decision_maker.py

import unittest
from decision_maker import DecisionMaker

class TestDecisionMaker(unittest.TestCase):
    
    def setUp(self):
        """
        Set up the test environment for the decision maker.
        This will be called before each test.
        """
        self.decision_maker = DecisionMaker()

    def test_initial_conditions(self):
        """
        Test the initial conditions of the decision-making system.
        It should start with no decisions made and an empty decision model.
        """
        print("Testing initial conditions...")
        self.assertEqual(len(self.decision_maker.decision_history), 0, "The decision history should start empty.")
        self.assertEqual(self.decision_maker.current_state, {}, "The current state should start empty.")
    
    def test_make_decision(self):
        """
        Test that the system can make decisions based on input data.
        The decision should be valid and based on the provided conditions.
        """
        print("Testing decision-making process...")
        input_data = {"sensor_data": 45, "context": "gaming"}
        
        # Simulate a decision-making process
        decision = self.decision_maker.make_decision(input_data)
        
        self.assertIn("action", decision, "The decision should contain an action.")
        self.assertIn("confidence", decision, "The decision should contain a confidence score.")
        self.assertTrue(0 <= decision["confidence"] <= 1, "The confidence score should be between 0 and 1.")
    
    def test_adaptive_decision_making(self):
        """
        Test the system's ability to adapt its decisions based on new data.
        It should adjust its decision-making logic based on updated input or context.
        """
        print("Testing adaptive decision-making...")
        
        initial_input = {"sensor_data": 50, "context": "gaming"}
        initial_decision = self.decision_maker.make_decision(initial_input)
        
        # Ensure a decision is made
        self.assertIn("action", initial_decision, "A valid action should be selected.")
        
        # Now adapt the decision maker with new data
        new_input = {"sensor_data": 90, "context": "gaming"}
        adapted_decision = self.decision_maker.make_decision(new_input)
        
        # Ensure the new decision differs from the initial one
        self.assertNotEqual(initial_decision["action"], adapted_decision["action"], "The decision should adapt to new input data.")
    
    def test_multiple_decisions(self):
        """
        Test that the system can make multiple decisions in succession and track the decision history.
        """
        print("Testing multiple decisions...")
        
        # Make a series of decisions
        decision_1 = self.decision_maker.make_decision({"sensor_data": 30, "context": "business"})
        decision_2 = self.decision_maker.make_decision({"sensor_data": 60, "context": "healthcare"})
        decision_3 = self.decision_maker.make_decision({"sensor_data": 15, "context": "gaming"})
        
        # Check the decision history
        self.assertEqual(len(self.decision_maker.decision_history), 3, "The decision history should contain 3 decisions.")
        
        # Validate the actions taken in each decision
        self.assertIn("action", decision_1, "The first decision should contain an action.")
        self.assertIn("action", decision_2, "The second decision should contain an action.")
        self.assertIn("action", decision_3, "The third decision should contain an action.")
    
    def test_invalid_input(self):
        """
        Test the system's ability to handle invalid or incomplete input data gracefully.
        The system should raise an error or handle the invalid input.
        """
        print("Testing handling of invalid input...")
        
        invalid_input_1 = {"sensor_data": None, "context": "gaming"}  # Invalid sensor data
        invalid_input_2 = {"sensor_data": 100, "context": None}  # Invalid context
        
        # Try making decisions with invalid inputs
        try:
            self.decision_maker.make_decision(invalid_input_1)
            self.fail("The system should raise an error for invalid sensor data.")
        except ValueError as e:
            print("Caught expected error for invalid sensor data:", e)
        
        try:
            self.decision_maker.make_decision(invalid_input_2)
            self.fail("The system should raise an error for invalid context.")
        except ValueError as e:
            print("Caught expected error for invalid context:", e)
    
    def test_real_time_decision(self):
        """
        Test the system's ability to make decisions in real-time with rapidly changing inputs.
        The system should make decisions promptly based on dynamic data.
        """
        print("Testing real-time decision-making...")
        
        real_time_inputs = [
            {"sensor_data": 45, "context": "gaming"},
            {"sensor_data": 60, "context": "business"},
            {"sensor_data": 30, "context": "healthcare"},
        ]
        
        # Make real-time decisions
        for input_data in real_time_inputs:
            decision = self.decision_maker.make_decision(input_data)
            self.assertIn("action", decision, "Each real-time decision should contain an action.")
            self.assertIn("confidence", decision, "Each real-time decision should contain a confidence score.")
    
    def tearDown(self):
        """
        Clean up after each test.
        This will be called after each test.
        """
        print("Cleaning up after test...")
        self.decision_maker = None


if __name__ == "__main__":
    # Run all the tests
    unittest.main()
