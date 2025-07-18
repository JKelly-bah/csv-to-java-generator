# CSV to Java Structure Generator - Developer Instructions

## Overview

The CSV to Java Structure Generator is a Python application that transforms CSV files containing XPath schema definitions into complete Java class structures. The application is designed to generate multiple Java model variations from a single CSV schema, making it ideal for data transformation projects where different system components require different field representations.

## Architecture

### Application Flow
1. **CSV Parsing**: Read and validate CSV schema files
2. **Data Modeling**: Transform CSV rows into internal data structures
3. **Java Generation**: Create complete Java classes with proper formatting
4. **File Output**: Write generated classes to specified directories

### Module Structure

```
src/
├── csv_parser.py       # CSV file parsing and validation
├── model_generator.py  # Internal model creation and field mapping
└── java_structure.py   # Java code generation and formatting
```

## Libraries and Dependencies

### Core Dependencies

#### 1. **pandas >= 2.0.0**
**Purpose**: CSV file reading and data manipulation

**Why Chosen**:
- **Robust CSV Parsing**: Handles various CSV formats, encodings, and edge cases
- **Data Validation**: Built-in support for checking data types and null values
- **Performance**: Optimized for reading large CSV files efficiently
- **Mature Ecosystem**: Well-tested library with extensive documentation

**Usage in Application**:
```python
df = pd.read_csv(file_path)
for _, row in df.iterrows():
    # Process each row
```

#### 2. **dataclasses-json >= 0.6.0**
**Purpose**: Enhanced dataclass functionality and JSON serialization

**Why Chosen**:
- **Type Safety**: Provides better type hints and validation
- **Serialization**: Easy conversion between dataclasses and JSON (future extensibility)
- **Code Clarity**: Makes data structures more readable and maintainable
- **Python Standards**: Built on top of Python's native dataclasses

**Usage in Application**:
```python
@dataclass
class SchemaField:
    xpath: str
    required: str
    data_type: str
    # ... other fields
```

#### 3. **typing-extensions >= 4.5.0**
**Purpose**: Advanced type hinting support

**Why Chosen**:
- **Type Safety**: Provides Optional, List, Dict type hints for better code clarity
- **IDE Support**: Enhanced autocomplete and error detection in development
- **Future Compatibility**: Ensures type hints work across Python versions
- **Code Documentation**: Type hints serve as inline documentation

**Usage in Application**:
```python
from typing import List, Dict, Optional

def generate_models(self, schema_fields: List[SchemaField]) -> Dict[str, Model]:
```

## Core Components

### 1. CSV Parser (`csv_parser.py`)

**Responsibility**: Read and validate CSV schema files

#### Key Classes:

##### `SchemaField`
- **Purpose**: Represents a single row from the CSV schema
- **Fields**: xpath, required status, data type, model values, additional info
- **Design Decision**: Uses dataclass for immutability and type safety

##### `CSVSchemaParser`
- **Purpose**: Main parsing logic and validation
- **Key Methods**:
  - `parse_csv()`: Main entry point for CSV processing
  - `_validate_columns()`: Ensures required columns are present
- **Error Handling**: Comprehensive validation with descriptive error messages

#### Design Decisions:

1. **Flexible Column Support**: Beyond the 7 required columns, any additional columns are automatically captured in `additional_info`
2. **Normalization**: Column names are normalized (lowercase, stripped) for case-insensitive matching
3. **Robust Validation**: Validates CSV structure before processing to fail fast with clear errors

### 2. Model Generator (`model_generator.py`)

**Responsibility**: Transform CSV data into internal model structures

#### Key Classes:

##### `ModelField`
- **Purpose**: Represents a field in the generated Java model
- **Enhanced Metadata**: Stores all CSV column information for comprehensive documentation
- **Type Mapping**: Handles conversion from string data types to Java types

##### `Model`
- **Purpose**: Represents a complete Java class structure
- **Package Management**: Configurable package names
- **Class Naming**: Automatic conversion to proper Java naming conventions

##### `ModelGenerator`
- **Purpose**: Orchestrates the model generation process
- **Key Features**:
  - Four model generation from single schema
  - Conditional field inclusion based on model values
  - Java type mapping with sensible defaults

#### Design Decisions:

1. **Java Type Mapping**: Comprehensive mapping from common data types to Java equivalents
   ```python
   java_type_mapping = {
       'string': 'String',
       'integer': 'Integer',
       'boolean': 'Boolean',
       'date': 'LocalDate',
       'decimal': 'BigDecimal',
       # ... more mappings
   }
   ```

2. **Skip Logic**: Multiple ways to exclude fields (`do not use`, `skip`, `ignore`, etc.)
3. **camelCase Conversion**: Automatic conversion from various naming conventions
4. **Metadata Preservation**: All CSV information is preserved for documentation generation

### 3. Java Structure Generator (`java_structure.py`)

**Responsibility**: Generate complete, well-formatted Java classes

#### Key Features:

##### Code Generation:
- **Complete Classes**: Constructors, getters, setters, equals, hashCode, toString
- **JavaDoc Documentation**: Comprehensive comments with CSV metadata
- **Import Management**: Automatic import resolution for Java types
- **Formatting**: Proper Java code formatting and indentation

##### Documentation Generation:
- **Field Comments**: Include all CSV column information
- **Method Documentation**: Complete JavaDoc for all generated methods
- **Type Information**: Clear parameter and return type documentation

#### Design Decisions:

1. **Template-Based Generation**: Uses string templates for consistent code structure
2. **Import Optimization**: Only imports types that are actually used
3. **Documentation Format**: Structured comments with clear column name labels
4. **Java Conventions**: Follows standard Java naming and formatting conventions

## Configuration and Extensibility

### Adding New Data Types

To add support for new data types, update the `java_type_mapping` in `ModelGenerator`:

```python
self.java_type_mapping = {
    # Existing mappings...
    'uuid': 'UUID',
    'json': 'JsonNode',
    'custom_type': 'CustomClass'
}
```

### Modifying Java Code Templates

Java code generation is handled in `JavaStructureGenerator`. Key methods to modify:

- `_generate_field_declaration()`: Field generation and comments
- `_generate_getter_setter()`: Accessor method generation
- `_generate_constructor()`: Constructor generation

### Adding New Model Types

To support more than 4 models, update the range in `ModelGenerator.generate_models()`:

```python
for model_num in range(1, 6):  # Now supports 5 models
```

## Error Handling Strategy

### Validation Levels:
1. **CSV Structure**: Column validation before processing
2. **Data Validation**: Row-by-row validation during parsing
3. **Type Validation**: Data type checking during model generation
4. **File System**: I/O error handling during output generation

### Error Types:
- `FileNotFoundError`: Missing CSV files
- `ValueError`: Invalid CSV structure or data
- `IOError`: File system errors during output

## Performance Considerations

### Memory Usage:
- **Streaming**: CSV is processed row-by-row to minimize memory footprint
- **Lazy Generation**: Java code is generated on-demand
- **String Optimization**: Uses string concatenation for better performance

### Scalability:
- **Large CSVs**: Designed to handle CSV files with thousands of rows
- **Multiple Models**: Efficient generation of multiple model variations
- **Concurrent Processing**: Could be extended for parallel model generation

## Testing Strategy

### Unit Tests:
- CSV parsing with various formats and edge cases
- Model generation with different data types
- Java code generation validation

### Integration Tests:
- End-to-end workflow with sample CSV files
- Error handling with malformed inputs
- Output validation with generated Java classes

### Test Data:
- Sample CSV files with various scenarios
- Edge cases (empty fields, special characters, etc.)
- Invalid data for error testing

## Development Workflow

### Setup:
1. **Environment**: Python 3.7+ with virtual environment
2. **Dependencies**: Install via `pip install -r requirements.txt`
3. **IDE**: Configured for Python development with type checking

### Code Style:
- **Python**: Follows PEP 8 guidelines
- **Type Hints**: Comprehensive type annotations
- **Documentation**: Docstrings for all public methods
- **Comments**: Inline comments for complex logic

### Version Control:
- **Git**: Standard Git workflow with feature branches
- **Commits**: Descriptive commit messages
- **Tags**: Version tagging for releases

## Future Enhancements

### Potential Features:
1. **Template Customization**: User-defined Java class templates
2. **Multiple Languages**: Support for C#, TypeScript, etc.
3. **Validation Rules**: Generate validation annotations from CSV data
4. **API Generation**: Create REST API endpoints from models
5. **Database Schema**: Generate DDL scripts from models

### Technical Improvements:
1. **Configuration Files**: External configuration for mappings and templates
2. **Plugin Architecture**: Extensible plugin system for custom generators
3. **CLI Enhancements**: More command-line options and flags
4. **GUI Interface**: Web-based interface for non-technical users

## Troubleshooting

### Common Issues:

#### CSV Format Problems:
- **Solution**: Ensure CSV has proper headers and encoding
- **Debug**: Check column names match expected format

#### Type Mapping Issues:
- **Solution**: Verify data type names in CSV match mapping dictionary
- **Debug**: Add logging to see unmapped types

#### Generated Code Errors:
- **Solution**: Check Java syntax in templates
- **Debug**: Validate generated code with Java compiler

#### File Permission Errors:
- **Solution**: Ensure write permissions on output directory
- **Debug**: Check file system permissions and disk space

### Debug Mode:
Enable verbose logging by modifying the main application:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

This comprehensive developer guide provides all the necessary information for understanding, maintaining, and extending the CSV to Java Structure Generator application.
