#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_looker_custom import SourceLookerCustom

if __name__ == "__main__":
    source = SourceLookerCustom()
    launch(source, sys.argv[1:])
