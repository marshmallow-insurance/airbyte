#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_bob_custom import SourceBobCustom

if __name__ == "__main__":
    source = SourceBobCustom()
    launch(source, sys.argv[1:])
