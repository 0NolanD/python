from television import Television
import pytest


class TestTelevision:
    @pytest.fixture
    def tv(self):
        return Television()

    def test_init(self, tv):
        assert tv._Television__status == False
        assert tv._Television__channel == 0
        assert tv._Television__volume == 0

    def test_power(self, tv):
        assert tv._Television__status == False
        tv.power()
        assert tv._Television__status == True

    def test_mute(self, tv):
        tv.power()
        tv.volume_up()
        tv.mute()
        assert tv._Television__muted == True
        assert tv._Television__volume == 0
        assert tv._Television__previous_volume == 1

        tv.mute()
        assert tv._Television__muted == False
        assert tv._Television__volume == 1

        tv.power()
        assert tv._Television__status == False
        assert tv._Television__muted == False

        tv.mute()
        assert tv._Television__status == False
        assert tv._Television__muted == False

    def test_channel_up(self, tv):
        tv.channel_up()
        assert tv._Television__channel == 0

        tv.power()
        assert tv._Television__channel == 0
        tv.channel_up()
        assert tv._Television__channel == 1

        tv.channel_up()
        tv.channel_up()
        tv.channel_up()
        assert tv._Television__channel != 4

    def test_channel_down(self, tv):
        tv.channel_down()
        assert tv._Television__channel == 0

        tv.power()
        tv.channel_down()
        assert tv._Television__channel != -1

    def test_volume_up(self, tv):
        tv.channel_up()
        assert tv._Television__volume == tv.min_volume

        tv.power()
        tv.volume_up()
        assert tv._Television__volume == 1

        tv.mute()
        tv.volume_up()
        assert tv._Television__muted == False
        assert tv._Television__volume == 2

        tv.volume_up()
        assert tv._Television__volume == 2

    def test_volume_down(self, tv):
        tv.volume_down()
        assert tv._Television__volume == 0

        tv.power()
        tv.volume_up()
        tv.volume_up()
        assert tv._Television__volume == 2
        tv.volume_down()
        assert tv._Television__volume == 1

        tv.mute()
        tv.volume_down()
        assert tv._Television__volume == 0

        tv.volume_down()
        assert tv._Television__volume == 0








