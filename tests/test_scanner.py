# test_scanner.py

import unittest
from scanner import Scanner

class TestScanner(unittest.TestCase):
    
    def setUp(self):
        """
        Set up the test environment for the scanner.
        This will be called before each test.
        """
        self.scanner = Scanner()  # Initialize the Scanner instance

    def test_initial_conditions(self):
        """
        Test the initial conditions of the scanner.
        The scanner should start with an empty data buffer.
        """
        print("Testing initial conditions...")
        self.assertEqual(len(self.scanner.data_buffer), 0, "The scanner should start with an empty data buffer.")
        self.assertEqual(self.scanner.state, "idle", "The initial scanner state should be 'idle'.")
    
    def test_scan_data(self):
        """
        Test that the scanner can successfully scan and store data.
        The scanner should process the scanned data and store it in its buffer.
        """
        print("Testing data scanning...")
        
        # Simulate a sensor reading input
        sensor_input = {"sensor_id": "123", "value": 100, "timestamp": 1609459200}
        
        # Perform the scan
        self.scanner.scan_data(sensor_input)
        
        # Verify that the data has been added to the data buffer
        self.assertEqual(len(self.scanner.data_buffer), 1, "The data buffer should contain 1 item.")
        self.assertEqual(self.scanner.data_buffer[0], sensor_input, "The first item in the data buffer should match the scanned input.")
    
    def test_multiple_data_scans(self):
        """
        Test that the scanner can handle multiple data scans and store each separately.
        """
        print("Testing multiple data scans...")
        
        # Simulate multiple sensor readings
        sensor_input_1 = {"sensor_id": "124", "value": 150, "timestamp": 1609459201}
        sensor_input_2 = {"sensor_id": "125", "value": 200, "timestamp": 1609459202}
        
        # Perform the scans
        self.scanner.scan_data(sensor_input_1)
        self.scanner.scan_data(sensor_input_2)
        
        # Verify that both inputs are in the buffer
        self.assertEqual(len(self.scanner.data_buffer), 2, "The data buffer should contain 2 items.")
        self.assertEqual(self.scanner.data_buffer[0], sensor_input_1, "The first item should match the first sensor input.")
        self.assertEqual(self.scanner.data_buffer[1], sensor_input_2, "The second item should match the second sensor input.")
    
    def test_invalid_data_scan(self):
        """
        Test how the scanner handles invalid or malformed data.
        The system should raise an error or handle invalid data gracefully.
        """
        print("Testing invalid data scanning...")
        
        # Invalid data (missing required fields)
        invalid_data = {"sensor_id": "126", "timestamp": 1609459203}
        
        # Test with invalid data
        with self.assertRaises(ValueError):
            self.scanner.scan_data(invalid_data)
        
        # Invalid data (empty dictionary)
        empty_data = {}
        
        # Test with empty data
        with self.assertRaises(ValueError):
            self.scanner.scan_data(empty_data)
    
    def test_real_time_data_scanning(self):
        """
        Test that the scanner can continuously scan real-time data.
        The scanner should handle streaming data in a real-time scenario.
        """
        print("Testing real-time data scanning...")
        
        # Simulate a series of sensor readings over time
        real_time_data = [
            {"sensor_id": "127", "value": 180, "timestamp": 1609459204},
            {"sensor_id": "128", "value": 220, "timestamp": 1609459205},
            {"sensor_id": "129", "value": 250, "timestamp": 1609459206}
        ]
        
        # Scan the real-time data
        for data in real_time_data:
            self.scanner.scan_data(data)
        
        # Ensure all data is in the data buffer
        self.assertEqual(len(self.scanner.data_buffer), 3, "The data buffer should contain 3 items.")
        for i, data in enumerate(real_time_data):
            self.assertEqual(self.scanner.data_buffer[i], data, f"Item {i+1} should match the expected real-time data.")
    
    def test_state_transition(self):
        """
        Test that the scanner transitions between states correctly.
        The scanner should transition from 'idle' to 'scanning' and back to 'idle'.
        """
        print("Testing scanner state transition...")
        
        # Initially, the scanner should be idle
        self.assertEqual(self.scanner.state, "idle", "The initial state should be 'idle'.")
        
        # Simulate scanning data
        sensor_input = {"sensor_id": "130", "value": 300, "timestamp": 1609459207}
        self.scanner.scan_data(sensor_input)
        
        # The state should change to 'scanning'
        self.assertEqual(self.scanner.state, "scanning", "The state should be 'scanning' after starting the scan.")
        
        # Simulate completing the scan
        self.scanner.finish_scanning()
        
        # The state should return to 'idle'
        self.assertEqual(self.scanner.state, "idle", "The state should return to 'idle' after finishing the scan.")
    
    def tearDown(self):
        """
        Clean up after each test.
        This will be called after each test.
        """
        print("Cleaning up after test...")
        self.scanner = None


if __name__ == "__main__":
    # Run all the tests
    unittest.main()
