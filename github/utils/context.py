"""
/utils/context.py

    Copyright (c) 2019 ShineyDev
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import aiohttp


class SessionContext():
    def __init__(self, session: aiohttp.ClientSession):
        self.session = session
        self.callable = True if callable(session) else False

    async def __aenter__(self):
        if (self.callable):
            self.session = self.session()

        return self.session

    async def __aexit__(self, *args):
        if (self.callable):
            await self.session.close()