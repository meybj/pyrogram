#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from .auto_name import AutoName


class ProfileColor(AutoName):
    """Profile color enumeration used in :meth:`~pyrogram.method.UpdateColor` and :obj:`~pyrogram.types.ChatColor`."""

    RED = 0
    ORANGE = 1
    VIOLET = 2
    GREEN = 3
    CYAN = 4
    BLUE = 5
    PINK = 6
    GRAY = 7

    RED_LIGHT_RED = 8
    ORANGE_LIGHT_ORANGE = 9
    VIOLET_LIGHT_VIOLET = 10
    GREEN_LIGHT_GREEN = 11
    CYAN_LIGHT_CYAN = 12
    BLUE_LIGHT_BLUE = 13
    PINK_LIGHT_PINK = 14
    GRAY_LIGHT_GRAY = 15
