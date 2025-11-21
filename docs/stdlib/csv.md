# .\csv.axec

## model CsvRow

CSV row model - represents a single row of CSV data

## model CsvDocument

CSV document model - represents an entire CSV file

## model CsvOptions

CSV parser options

## def default_options(): CsvOptions

Create default CSV options (comma delimiter, double quote, no header assumption)

## def create_document(arena: ref Arena): CsvDocument

Create a new empty CSV document with arena allocator

## def create_row(): CsvRow

Create a new empty CSV row

## def add_field(row: ref CsvRow, field: string, arena: ref Arena)

Add a field to a CSV row (using arena allocation)

## def add_row(doc: ref CsvDocument, row: CsvRow)

Add a row to a CSV document (using arena allocation)

## def get_row(doc: ref CsvDocument, index: usize): ref CsvRow

Get a row from a CSV document by index

## def get_field(row: ref CsvRow, index: usize): string

Get a field from a CSV row by index

## def parse(csv_data: string, options: CsvOptions, arena: ref Arena): CsvDocument

Parse a CSV string into a document (using arena allocation)

## def parse_simple(csv_data: string, arena: ref Arena): CsvDocument

Parse CSV with default options (comma delimiter) using arena allocation

## def to_string(doc: ref CsvDocument, options: CsvOptions): string

Convert a CSV document back to a string (using arena allocation)
