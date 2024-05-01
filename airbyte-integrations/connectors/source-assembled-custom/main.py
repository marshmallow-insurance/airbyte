#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from airbyte_cdk.entrypoint import launch
from source_assembled_custom import SourceAssembledCustom

if __name__ == "__main__":
    source = SourceAssembledCustom()
    launch(source, sys.argv[1:])
