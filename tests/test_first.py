import pytest


@pytest.mark.usefixtures('setup')
class TestFirst:
    def test_first(self):
        pass