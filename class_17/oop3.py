class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __add__(self, other):
        """Adds two points"""
        newpoint = Point()
        newpoint.x = self.x + other.x
        newpoint.y = self.y + other.y
        return newpoint


class Time:
    """Represents the time of day.
       
    attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        """Initializes a time object.
        hour: int
        minute: int
        second: int or float
        """
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        """Returns a string representation of the time."""
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        """Returns the total number of seconds past midnight of a Time object."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def is_after(t1, t2):
        """Returns a boolean True if Time object t1 follows Time object t2 chronologically."""
        return t1.time_to_int() > t2.time_to_int()

    def add_time(self, other):
        """Returns a Time object equal to the addition of two Time objects"""
        final = self.time_to_int() + other.time_to_int()
        timey = int_to_time(final)
        return timey

    def increment(self, seconds):
        """Returns a Time object equal to the addition of a Time object and a number of seconds"""
        self_int = self.time_to_int()
        self_int += seconds
        return int_to_time(self_int)

    def subtract_time(self, other):
        """Returns a Time object equal to the amount of time between two Time objects"""
        final = abs(self.time_to_int() - other.time_to_int())
        timey = int_to_time(final)
        return timey

    def mul_time(self, other):
        """Returns a Time object equal to the product of a Time object and a number"""
        final = self.time_to_int() * other
        timey = int_to_time(final)
        return timey

    def is_expected(self, duration, arrival):
        """Returns True if the estimated arrival time (self + duration) is equal to the expected arrival time"""
        return self.time_to_int() + duration.time_to_int() == arrival.time_to_int()

def int_to_time(seconds):
    """Creates a Time object from a total number of seconds past midnight."""
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    my_time = Time(hour, minute, second)
    return my_time

def race_speed(finish, distance):
    """Returns mile time as a Time object when given a finish time and number of miles run."""
    return finish.mul_time(1/distance)


class Song():
    """Represents a song

    attributes: title, artist, lyrics
    """
    def __init__(self, title = '', artist = '', lyrics = ''):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def __str__(self):
        return 'Title: %s\nArtist: %s\n\nLyrics: %s' %(self.title, self.artist, self.lyrics)

    def __sub__(self, other):
        return str(self).lower().replace(other.lower(), '')

def main():
    my_song = Song(title = 'Twinkle Twinkle Little Star', artist = 'Duncan Rule', lyrics = 'Twinkle, twinkle, little star,\nHow I wonder what you are.\nUp above the world so high,\nLike a diamond in the sky.')
    print(str(my_song - 'Little'))

if __name__ == '__main__':
    main()