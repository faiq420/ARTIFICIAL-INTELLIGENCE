from Agent import Agent

class VaccumAgent(Agent):
    ''' classdocs '''
    def __init__(self):
        ''' Constructor '''
        pass

    def sense(self, env):
        self.environment = env

    def act(self):
        if self.environment.currentRoom.status == 'dirty':
            return 'clean'
        if self.environment.currentRoom.location == 'A':
            return 'right'
        else:
            return 'left'