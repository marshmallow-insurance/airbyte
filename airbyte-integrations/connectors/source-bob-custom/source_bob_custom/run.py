#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from .source import SourceBobCustom

def run():
    source = SourceBobCustom()
    launch(source, sys.argv[1:])
