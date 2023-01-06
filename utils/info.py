#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os

API_ID       = int(os.environ.get("API_ID", "25847347"))
API_HASH     = os.environ.get("API_HASH", "11569826ebbc9f8b14c3ab1c5ddb937b")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "5691268868:AAE4Fcaq8v1PRR5R1-tUszu4X3MdBaaDC0g")
SESSION      = os.environ.get("SESSION", "BQDMOvAAYxucTTMgEVWfr6zBrQ4iBLhSP8VqGbp0HUBY-pokWaMb-MBliRTycfqFiLcJqvcNCOIdtkn4ZDQeWjkurz3mLPxR-L3c4lvYP-58LuxY-1EHxS1OkDAcV3QzBAtWAZuQIfJhO6YY6zZAwX6S9_ocL9XNBaYO7qNdqoVAXnodKD_aXZVZ-jFhpERWyqBfekhwWHa0cE97CxADTgYy7FzZ_EXoBmIWx4q5bmRC2PYD41gTdLs_SsvdQbIxFc7Yj46evPHXiUMtoB2Q2t4mj9GbmiD1-6eoOhUd0xR8BR-upUM2IQa8mfLsbboYvWUYYN1PFFRQq5jbcSYFVYgeEmuvcgAAAABrD2cWAA")
TIME         = int(os.environ.get("TIME", 600))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1001828029453").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Maxime:0HbZa16hfOklBe7a@clusterp6.zmbbgqt.mongodb.net/?retryWrites=true&w=majority")
PORT         = os.environ.get("PORT", "8080")
