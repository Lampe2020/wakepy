from unittest.mock import patch
from wakepy.core.platform import get_current_platform, PlatformName

import pytest


class TestGetCurrentPlatform:

    @patch("platform.system", lambda: "Windows")
    def test_windows(self):
        assert get_current_platform() == PlatformName.WINDOWS

    @patch("platform.system", lambda: "Darwin")
    def test_macos(self):
        assert get_current_platform() == PlatformName.MACOS

    @patch("platform.system", lambda: "Linux")
    def test_linux(self):
        assert get_current_platform() == PlatformName.LINUX

    @patch("platform.system", lambda: "This does not exist")
    def test_linux(self):
        with pytest.warns(UserWarning, match="Could not detect current platform!"):
            assert get_current_platform() == PlatformName.OTHER
