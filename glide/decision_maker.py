# decision_maker.py

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import random

class DecisionMaker:
    def __init__(self, model=None):
        """
        Initialize the decision-making system.
        
        :param model: Pretrained machine learning model (optional).
        """
        self.model = model if model else DecisionTreeClassifier()
        self.history = []
        
    def collect_data(self, scenario):
        """
        Simulate the collection of real-time decision-making data.
        
        :param scenario: The current environmental or situational data.
        :return: Processed input for the decision model.
        """
        # Example of creating data based on the scenario (e.g., features)
        data = {
            'feature_1': scenario['factor_1'],
            'feature_2': scenario['factor_2'],
            'feature_3': scenario['factor_3']
        }
        return np.array([list(data.values())])
    
    def make_decision(self, scenario):
        """
        Make a decision based on the current scenario using the model or rule-based system.
        
        :param scenario: Current environmental or situational data.
        :return: The chosen action based on the decision-making model.
        """
        # Collect data based on the current scenario
        input_data = self.collect_data(scenario)

        # If model exists, predict action based on model
        if self.model:
            decision = self.model.predict(input_data)
        else:
            # If no model, fall back to a simple rule-based decision system
            decision = self.rule_based_decision(scenario)

        return decision[0]

    def rule_based_decision(self, scenario):
        """
        A simple rule-based decision engine based on predefined conditions.
        
        :param scenario: The current scenario or environment data.
        :return: The chosen action (as a string).
        """
        # Define simple decision rules
        if scenario['factor_1'] > 0.7 and scenario['factor_2'] < 0.3:
            return "Action_A"
        elif scenario['factor_1'] < 0.4 and scenario['factor_3'] > 0.5:
            return "Action_B"
        else:
            return "Action_C"

    def evaluate_model(self, test_data, test_labels):
        """
        Evaluate the performance of the decision-making model.
        
        :param test_data: The test dataset for evaluating the model.
        :param test_labels: The expected labels for the test dataset.
        :return: The accuracy score of the model.
        """
        predictions = self.model.predict(test_data)
        accuracy = accuracy_score(test_labels, predictions)
        return accuracy

    def train_model(self, training_data, training_labels):
        """
        Train the decision-making model on the provided dataset.
        
        :param training_data: Data to train the model on.
        :param training_labels: Labels (actions) for training the model.
        """
        self.model.fit(training_data, training_labels)
        print("Model trained successfully!")

    def simulate_decisions(self, num_decisions=10):
        """
        Simulate a series of decisions based on random scenarios.
        
        :param num_decisions: Number of simulated decisions to make.
        :return: A list of actions chosen by the decision-making system.
        """
        actions = []
        for _ in range(num_decisions):
            # Simulate a random scenario with factors
            scenario = {
                'factor_1': random.random(),
                'factor_2': random.random(),
                'factor_3': random.random()
            }
            action = self.make_decision(scenario)
            actions.append(action)
        return actions

# Example usage of the DecisionMaker class.

if __name__ == "__main__":
    # Create decision maker instance
    decision_maker = DecisionMaker()
    
    # Simulate training the model with some data
    training_data = np.array([[0.8, 0.1, 0.7], [0.2, 0.4, 0.8], [0.6, 0.3, 0.4]])
    training_labels = np.array(["Action_A", "Action_B", "Action_C"])
    decision_maker.train_model(training_data, training_labels)
    
    # Simulate decision-making with random scenarios
    simulated_actions = decision_maker.simulate_decisions(num_decisions=5)
    print(f"Simulated Actions: {simulated_actions}")
    
    # Example of evaluating the model (with some test data)
    test_data = np.array([[0.9, 0.2, 0.6], [0.3, 0.5, 0.7]])
    test_labels = np.array(["Action_A", "Action_C"])
    accuracy = decision_maker.evaluate_model(test_data, test_labels)
    print(f"Model Accuracy: {accuracy:.2f}")
