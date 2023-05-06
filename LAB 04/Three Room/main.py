from VacuumAgent import VaccumAgent
from Lab4 import TwoRoomVaccumCleanerEnvironment

vcagent = VaccumAgent()
env = TwoRoomVaccumCleanerEnvironment(vcagent) 
env.executeStep(20)
