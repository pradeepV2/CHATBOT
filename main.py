#!/usr/bin/env python3

#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# limitations under the License.
# ==============================================================================

"""
Main script.
Use python 3
"""

from chatbot import chatbot


if __name__ == "__main__":
    chatbot = chatbot.Chatbot()
    chatbot.main()
