class Television:
    min_volume: int = 0
    max_volume: int = 2
    min_channel: int = 0
    max_channel: int = 3

    def __init__(self) -> None:
        """
        Initializes variables
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.min_volume
        self.__channel: int = self.min_channel
        self.__previous_volume: int = self.min_volume

    def power(self) -> None:
        """
        Turns the power of the tv on and off
        """
        self.__status = not self.__status  # switches the power on and off

    def mute(self) -> None:
        """
        Mutes and unmutes the tv
        """
        if self.__status:
            self.__muted = not self.__muted  # mutes or unmutes the tv
            if self.__muted:
                self.__previous_volume = self.__volume
                self.__volume = self.min_volume  # affects volume accordingly and unmutes if the tv is muted
            else:
                self.__volume = self.__previous_volume

    def channel_up(self) -> None:
        """
        Increases the volume by 1
        """
        if self.__status:
            if self.__channel == self.max_channel:
                self.__channel = self.min_channel  # goes to the smallest numbered channel if it goes past the max
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decreases the channel by 1
        """
        if self.__status:
            if self.__channel == self.min_channel:  # goes to the largest numbered channel if it goes past the min
                self.__channel = self.max_channel
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increases the volume by 1
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
                self.__volume += 1  # unmutes the tv and changes the volume when the tv is muted
            else:
                if self.__volume < self.max_volume:
                    self.__volume += 1  # increases the volume if it's not at the max

    def volume_down(self) -> None:
        """
        Decreases the volume by 1
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
                self.__volume -= 1  # unmutes the tv and changes the volume when the tv is muted
            else:
                if self.__volume > self.min_volume:
                    self.__volume -= 1  # decreases the volume if it's not at the min

    def __str__(self) -> str:
        """
        Prints the status of the power, channel, and volume of the tv
        :return: string containing the power, channel, and volume values
        """
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"