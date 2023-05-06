from VaccumAgent import VaccumAgent
from TwoRoomVaccumCleanerEnvironment import TwoRoomVaccumCleanerEnvironment


if __name__ == '__main__':
    vcagent = VaccumAgent()
    env = TwoRoomVaccumCleanerEnvironment(vcagent)
    env.executeStep(50)