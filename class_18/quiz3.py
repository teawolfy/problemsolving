ELECTORS = {'CA': 55, 'TX': 38, 'FL': 29, 'MA': 11}


class Candidate:
    """The presidential candidate"""

    def __init__(self, name, winning_states = None, votes = 0, influence = 0):
        """Initialize candidate.
        name: string
        winning_states: a list of strings representing initial winning state(s).
        votes: integer, representing number of votes
        """
        self.name = name
        self.votes = votes
        self.winning_states = []
        self.influence = influence
        if winning_states != None:
            for state in winning_states:
                self.win_state(state)
        pass

    def __str__(self):
        """Return a string representaion of this candidate,
        including name and winning state(s).
        """
        return 'Candidate: %s \nWinning States: %s\n' %(self.name, ', '.join(self.winning_states))
        pass

    def win_state(self, state):
        """Adds a state to winning_states and updates votes.
        state: a string of state abbreviation
        """
        self.winning_states.append(state)
        self.votes += ELECTORS.get(state)
        pass

    def __gt__(self, other):
        if self.votes == other.votes:
            return self.influence > other.influence
        else:
            return self.votes > other.votes


def main():
    trump = Candidate('Donald Trump', influence = 10)
    clinton = Candidate('Hillary Clinton', winning_states=['CA'], influence = 80)
    print(trump)
    print(clinton)
    print()
    print('After election:')
    trump.win_state('FL')
    trump.win_state('TX')
    clinton.win_state('MA')
    print(trump)
    print(clinton)
    print('Does Trump win?')
    print(trump > clinton)

if __name__ == '__main__':
    main()