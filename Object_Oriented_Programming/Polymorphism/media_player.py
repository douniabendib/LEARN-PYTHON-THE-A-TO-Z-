from abc import ABC, abstractmethod


class Playable(ABC):
    """Create a Playable interface (abstract base class)"""

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class MediaInfo(ABC):
    """Create a MediaInfo interface (abstract base class)"""

    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def get_duration(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Song(Playable, MediaInfo):
      """Create a concrete classe that implement both interfaces"""

      def __init__(self, title, artist, duration):
          self.title = title
          self.artist = artist
          self.duration = duration

      def play(self):
          return f"Playing song: {self.title}"

      def pause(self):
          return f"Paused song: {self.title}"

      def stop(self):
          return f"Stopped song: {self.title}"

      def get_title(self):
          return f"{self.title}"

      def get_duration(self):
          return self.duration

      def get_info(self):
          minutes = self.duration // 60
          seconds = self.duration % 60 
          return f"Song: {self.title} by {self.artist} ({minutes}:{seconds:02d})"


class Video(Playable, MediaInfo):
    """Create a concrete classe that implement both interfaces"""

    def __init__(self, title, resolution, duration):
        self.title = title
        self.resolution = resolution
        self.duration = duration

    def play(self):
        return f"Playing video: {self.title}"

    def pause(self):
        return f"Paused video: {self.title}"

    def stop(self):
        return f"Stopped video: {self.title}"

    def get_title(self):
        return f"{self.title}"

    def get_duration(self):
        return self.duration

    def get_info(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"Video: {self.title} ({self.resolution}) ({minutes}:{seconds:02d})"


class MediaPlayer:
    """Create a class that can work with any object Playable interface"""

    def __init__(self, current_media=None):
        self.current_media = current_media

    def set_media(self, media):
        self.current_media = media

    def play(self):
        if self.current_media:
           return self.current_media.play()
        return "No media to play"

    def pause(self):
        if self.current_media:
           return self.current_media.pause()
        return "No media to pause"

    def stop(self):
        if self.current_media:
           return self.current_media.stop()
        return "No media to stop"


# Test your implementation
song = Song("Bohemian Rhapsody", "Queen", 355)
video = Video("Python Tutorial", "1080p", 1800)
player = MediaPlayer()

# Test with song
player.set_media(song)
print(player.current_media.get_info())
print(player.play())
print(player.pause())
print(player.stop())
print()  # Empty line for readability

# Test with video
player.set_media(video)
print(player.current_media.get_info())
print(player.play())
print(player.pause())
