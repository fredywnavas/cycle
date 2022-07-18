class Director:
    """
    A person who directs the game.
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """
    def __init__(self, video_service):
        