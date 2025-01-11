# test_gaming_engine.py

import unittest
from gaming_engine import GamingEngine
from decision_maker import DecisionMaker

class TestGamingEngine(unittest.TestCase):
    
    def setUp(self):
        """
        Set up the test environment for the gaming engine.
        This will be called before each test.
        """
        self.decision_maker = DecisionMaker()  # Create a DecisionMaker instance for gaming engine testing
        self.gaming_engine = GamingEngine(self.decision_maker)

    def test_initial_conditions(self):
        """
        Test the initial conditions of the gaming engine.
        The game should start with no actions and no current state.
        """
        print("Testing initial conditions...")
        self.assertEqual(self.gaming_engine.game_state, {}, "The initial game state should be empty.")
        self.assertEqual(len(self.gaming_engine.game_actions), 0, "There should be no game actions initially.")
    
    def test_generate_game_action(self):
        """
        Test that the gaming engine can generate a valid action.
        """
        print("Testing game action generation...")
        # Simulate some input from the game environment
        game_input = {"player_position": (10, 15), "enemy_position": (20, 25)}
        
        # Generate a game action based on the input
        action = self.gaming_engine.generate_action(game_input)
        
        # Ensure that the generated action contains the expected keys
        self.assertIn("action_type", action, "The generated action should contain 'action_type'.")
        self.assertIn("target_position", action, "The generated action should contain 'target_position'.")
        self.assertIn("action_strength", action, "The generated action should contain 'action_strength'.")
    
    def test_adaptive_gameplay_with_feedback(self):
        """
        Test the ability of the gaming engine to adapt gameplay based on feedback.
        The engine should change its actions over multiple iterations.
        """
        print("Testing adaptive gameplay with feedback...")
        
        # Initial game input and generate action
        initial_input = {"player_position": (10, 15), "enemy_position": (20, 25)}
        action = self.gaming_engine.generate_action(initial_input)
        
        # Provide feedback based on the initial action
        feedback_data = {"action": action["action_type"], "performance_score": 0.75}
        self.gaming_engine.process_feedback(feedback_data)
        
        # Simulate new game input after feedback has been processed
        new_input = {"player_position": (15, 20), "enemy_position": (25, 30)}
        new_action = self.gaming_engine.generate_action(new_input)
        
        # Ensure the new action is influenced by the feedback (i.e., a different action is chosen)
        self.assertNotEqual(action["action_type"], new_action["action_type"], "The game action should evolve based on feedback.")
    
    def test_real_time_game_action_processing(self):
        """
        Test that the gaming engine processes actions in real-time based on dynamic input.
        """
        print("Testing real-time game action processing...")
        
        # Simulate dynamic game inputs
        dynamic_inputs = [
            {"player_position": (5, 5), "enemy_position": (10, 10)},
            {"player_position": (8, 10), "enemy_position": (15, 15)},
            {"player_position": (12, 12), "enemy_position": (20, 20)},
        ]
        
        # Process the game actions based on dynamic inputs
        for game_input in dynamic_inputs:
            action = self.gaming_engine.generate_action(game_input)
            self.assertIn("action_type", action, "Real-time actions should have an 'action_type'.")
            self.assertIn("target_position", action, "Real-time actions should have a 'target_position'.")
            self.assertIn("action_strength", action, "Real-time actions should have an 'action_strength'.")

    def test_invalid_game_input(self):
        """
        Test how the gaming engine handles invalid or malformed game input.
        The system should raise an appropriate error or ignore invalid data.
        """
        print("Testing handling of invalid game input...")
        
        # Invalid game input (missing positions)
        invalid_input = {"player_position": None, "enemy_position": None}
        
        # Test with invalid game input data
        with self.assertRaises(ValueError):
            self.gaming_engine.generate_action(invalid_input)
        
        # Invalid game input (empty dictionary)
        empty_input = {}
        
        # Test with empty input
        with self.assertRaises(ValueError):
            self.gaming_engine.generate_action(empty_input)

    def test_game_action_history(self):
        """
        Test that the gaming engine maintains a history of actions taken during gameplay.
        """
        print("Testing game action history...")
        
        # Simulate multiple rounds of gameplay
        game_inputs = [
            {"player_position": (10, 10), "enemy_position": (15, 15)},
            {"player_position": (12, 15), "enemy_position": (20, 25)},
            {"player_position": (15, 20), "enemy_position": (30, 35)}
        ]
        
        for game_input in game_inputs:
            self.gaming_engine.generate_action(game_input)
        
        # Check that the action history contains all generated actions
        self.assertEqual(len(self.gaming_engine.game_actions), 3, "The game action history should contain 3 actions.")
        
        # Check that the last action contains the expected keys
        last_action = self.gaming_engine.game_actions[-1]
        self.assertIn("action_type", last_action, "The last action should contain 'action_type'.")
        self.assertIn("target_position", last_action, "The last action should contain 'target_position'.")
        self.assertIn("action_strength", last_action, "The last action should contain 'action_strength'.")

    def tearDown(self):
        """
        Clean up after each test.
        This will be called after each test.
        """
        print("Cleaning up after test...")
        self.gaming_engine = None
        self.decision_maker = None


if __name__ == "__main__":
    # Run all the tests
    unittest.main()
