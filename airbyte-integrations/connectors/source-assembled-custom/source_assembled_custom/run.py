#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from .source import SourceAssembledCustom

def run():
    source = SourceAssembledCustom()
    launch(source, sys.argv[1:])
