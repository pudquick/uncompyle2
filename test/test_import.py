import sys
import os, sys, BaseHTTPServer

import test.test_MimeWriter

from rfc822 import Message
from mimetools import Message, decode, choose_boundary
from os import *

for k, v in globals().items():
    print `k`, v
