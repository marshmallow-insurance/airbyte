from typing import Any, Mapping, Type

from airbyte_cdk.sources.file_based.config.avro_format import AvroFormat
from airbyte_cdk.sources.file_based.config.csv_format import CsvFormat
from airbyte_cdk.sources.file_based.config.jsonl_format import JsonlFormat
from airbyte_cdk.sources.file_based.config.parquet_format import ParquetFormat
from airbyte_cdk.sources.file_based.config.unstructured_format import UnstructuredFormat
from airbyte_cdk.sources.file_based.config.xlsx_format import XlsxFormat

from .avro_parser import AvroParser
from .csv_parser import CsvParser
from .file_type_parser import FileTypeParser
from .jsonl_parser import JsonlParser
from .parquet_parser import ParquetParser
from .unstructured_parser import UnstructuredParser
from .xlsx_parser import XlsxParser

default_parsers: Mapping[Type[Any], FileTypeParser] = {
    AvroFormat: AvroParser(),
    CsvFormat: CsvParser(),
    JsonlFormat: JsonlParser(),
    ParquetFormat: ParquetParser(),
    UnstructuredFormat: UnstructuredParser(),
    XlsxFormat: XlsxParser(),
}

__all__ = ["AvroParser", "CsvParser", "JsonlParser", "ParquetParser", "UnstructuredParser", "XlsxParser", "default_parsers"]
