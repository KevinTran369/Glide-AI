# test_processor.py

import unittest
from processor import Processor

class TestProcessor(unittest.TestCase):
    
    def setUp(self):
        """
        Set up the test environment for the processor.
        This will be called before each test.
        """
        self.processor = Processor()  # Initialize the Processor instance

    def test_initial_conditions(self):
        """
        Test the initial conditions of the processor.
        The processor should start with an empty data queue.
        """
        print("Testing initial conditions...")
        self.assertEqual(len(self.processor.data_queue), 0, "The processor should start with an empty data queue.")
        self.assertEqual(self.processor.state, "idle", "The initial processor state should be 'idle'.")
    
    def test_process_data(self):
        """
        Test the processor's ability to process data.
        The processor should process incoming data and generate a result.
        """
        print("Testing data processing...")
        
        # Simulate incoming data
        data_input = {"sensor_reading": 100, "timestamp": 1609459200}
        
        # Process the data and get the result
        result = self.processor.process_data(data_input)
        
        # Ensure that the result is as expected
        self.assertIn("processed_data", result, "The processed data should contain the 'processed_data' key.")
        self.assertEqual(result["processed_data"], 100, "The processed data value should be 100.")
    
    def test_real_time_data_processing(self):
        """
        Test that the processor can handle real-time data streams.
        The processor should be able to process data continuously in a real-time scenario.
        """
        print("Testing real-time data processing...")
        
        # Simulate a series of data inputs
        real_time_data = [
            {"sensor_reading": 150, "timestamp": 1609459201},
            {"sensor_reading": 200, "timestamp": 1609459202},
            {"sensor_reading": 250, "timestamp": 1609459203}
        ]
        
        # Process each piece of real-time data
        for data_input in real_time_data:
            result = self.processor.process_data(data_input)
            self.assertIn("processed_data", result, "Each real-time processed data should contain the 'processed_data' key.")
            self.assertGreater(result["processed_data"], 0, "Processed data should have a value greater than 0.")
    
    def test_data_queue_management(self):
        """
        Test that the processor manages its data queue correctly.
        The processor should add new data to the queue and process it sequentially.
        """
        print("Testing data queue management...")
        
        # Simulate incoming data
        data_input_1 = {"sensor_reading": 50, "timestamp": 1609459204}
        data_input_2 = {"sensor_reading": 75, "timestamp": 1609459205}
        
        # Add data to the queue
        self.processor.add_to_queue(data_input_1)
        self.processor.add_to_queue(data_input_2)
        
        # Ensure that the data is in the queue
        self.assertEqual(len(self.processor.data_queue), 2, "The processor's data queue should contain 2 items.")
        
        # Process data from the queue
        result_1 = self.processor.process_from_queue()
        result_2 = self.processor.process_from_queue()
        
        self.assertEqual(result_1["processed_data"], 50, "The first processed data should be 50.")
        self.assertEqual(result_2["processed_data"], 75, "The second processed data should be 75.")
    
    def test_invalid_data_processing(self):
        """
        Test how the processor handles invalid or malformed data.
        The system should raise an appropriate error or handle invalid data gracefully.
        """
        print("Testing invalid data processing...")
        
        # Invalid data (missing required fields)
        invalid_data = {"timestamp": 1609459200}
        
        # Test with invalid data
        with self.assertRaises(ValueError):
            self.processor.process_data(invalid_data)
        
        # Invalid data (empty dictionary)
        empty_data = {}
        
        # Test with empty data
        with self.assertRaises(ValueError):
            self.processor.process_data(empty_data)
    
    def test_state_transition(self):
        """
        Test that the processor transitions between states correctly.
        The processor should transition from 'idle' to 'processing' and back to 'idle'.
        """
        print("Testing processor state transition...")
        
        # Initially, the processor should be idle
        self.assertEqual(self.processor.state, "idle", "The initial state should be 'idle'.")
        
        # Simulate processing data
        data_input = {"sensor_reading": 100, "timestamp": 1609459200}
        self.processor.process_data(data_input)
        
        # The state should change to 'processing'
        self.assertEqual(self.processor.state, "processing", "The state should be 'processing' after starting the data processing.")
        
        # Simulate completing the processing
        self.processor.finish_processing()
        
        # The state should return to 'idle'
        self.assertEqual(self.processor.state, "idle", "The state should return to 'idle' after finishing the data processing.")
    
    def tearDown(self):
        """
        Clean up after each test.
        This will be called after each test.
        """
        print("Cleaning up after test...")
        self.processor = None


if __name__ == "__main__":
    # Run all the tests
    unittest.main()
