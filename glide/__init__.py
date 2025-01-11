# __init__.py

# Importing important modules from the Glide AI package
from .game_simulation import GameSimulation
from .business_intelligence import BusinessIntelligence
from .medical_analysis import MedicalAnalysis
from .autonomous_vehicle import AutonomousVehicle
from .glide_system import GlideSystem
from .research_tools import ResearchTools

# Expose important classes and functions to the package level
__all__ = [
    'GameSimulation', 
    'BusinessIntelligence', 
    'MedicalAnalysis', 
    'AutonomousVehicle', 
    'GlideSystem',
    'ResearchTools'
]

# Optional: You can also add some initial setup or configuration here
def initialize_glide():
    """
    Initializes Glide system components.
    """
    print("Initializing Glide AI system...")

# You can also add version information here, or other configurations
__version__ = "1.0.0"
