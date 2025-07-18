# CSV to Java Structure Generator

A Python application that reads CSV files containing XPath schema information and generates Java-like class structures for multiple data models.

## Features

- **CSV Schema Parsing**: Reads structured CSV files with XPath, data types, and model configurations
- **Multiple Model Generation**: Creates four different Java model classes from a single schema
- **Conditional Field Inclusion**: Supports excluding fields per model based on CSV values
- **Java Type Mapping**: Automatically maps string data types to appropriate Java types
- **Complete Class Generation**: Generates full Java classes with:
  - Private fields with proper naming
  - Default and parameterized constructors
  - Getter and setter methods
  - `toString()`, `equals()`, and `hashCode()` methods
  - Comprehensive JavaDoc documentation

## Installation

1. **Clone or download** this project to your local machine
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage
```bash
python main.py <csv_file_path> [output_directory]
```

### Examples
```bash
# Generate models from sample CSV to default 'output' directory
python main.py sample_schema.csv

# Generate models to custom directory
python main.py sample_schema.csv generated_models/

# Use the provided sample file
python main.py sample_schema.csv
```

## CSV Format

The input CSV file must contain the following columns:

| Column | Description | Example |
|--------|-------------|---------|
| `xpath` | XPath expression identifying the field | `/root/person/name/first` |
| `required/optional` | Whether the field is required | `required`, `optional` |
| `data_type` | Data type of the field | `string`, `integer`, `boolean` |
| `model1` | Value/behavior for Model 1 | `firstName` |
| `model2` | Value/behavior for Model 2 | `givenName` |
| `model3` | Value/behavior for Model 3 | `do not use` |
| `model4` | Value/behavior for Model 4 | `personalName` |
| `additional columns` | Any extra columns (optional) | `validation_rules`, `description`, etc. |

### Sample CSV Content
```csv
xpath,required/optional,data_type,model1,model2,model3,model4,validation_rules
/root/person/id,required,integer,personId,userId,entityId,recordId,min:1 max:999999
/root/person/name/first,required,string,firstName,givenName,do not use,personalName,minLength:1 maxLength:50
/root/person/email,optional,string,emailAddress,contactEmail,email,primaryEmail,pattern:email format
```

### Supported Data Types
- `string`, `str` → `String`
- `integer`, `int` → `Integer`
- `long` → `Long`
- `double` → `Double`
- `float` → `Float`
- `boolean`, `bool` → `Boolean`
- `date` → `LocalDate`
- `datetime`, `timestamp` → `LocalDateTime`
- `decimal` → `BigDecimal`
- `list`, `array` → `List<String>`

### Conditional Field Inclusion
Use these values in model columns to exclude fields:
- `do not use`
- `skip`
- `ignore`
- `exclude`
- `n/a`, `na`
- `null`, `none`
- `-`

## Output

The application generates four Java class files (Model1.java, Model2.java, Model3.java, Model4.java) in the specified output directory.

### Example Generated Class
```java
package com.example.models;

import java.time.LocalDate;
import java.math.BigDecimal;

/**
 * Model1 - Auto-generated model class
 * Generated from CSV schema definition
 */
public class Model1 {
    /**
     * xpath: /root/person/id
     * required/optional: required
     * data_type: Integer
     * model_value: personId
     * additional_info: validation_rules: min:1 max:999999
     * default_value: personId
     */
    private Integer id;

    /**
     * xpath: /root/person/name/first
     * required/optional: required
     * data_type: String
     * model_value: firstName
     * additional_info: validation_rules: minLength:1 maxLength:50
     * default_value: firstName
     */
    private String first = "firstName";

    // Constructors, getters, setters, equals, hashCode, toString...
}
```

## Project Structure

```
csvToJavaStructure/
├── main.py                    # Application entry point
├── requirements.txt           # Python dependencies
├── sample_schema.csv         # Example CSV file
├── src/
│   ├── __init__.py
│   ├── csv_parser.py         # CSV parsing logic
│   ├── model_generator.py    # Model creation logic
│   └── java_structure.py     # Java code generation
├── .github/
│   └── copilot-instructions.md
└── README.md
```

## Error Handling

The application includes comprehensive error handling for:
- Missing or invalid CSV files
- Incorrect CSV format or missing columns
- Invalid data types
- File system errors during output generation

## Development

### Running Tests
```bash
# Test with the sample CSV
python main.py sample_schema.csv test_output/
```

### Customization
- Modify `java_type_mapping` in `ModelGenerator` to add new data types
- Update `JavaStructureGenerator` to change Java code formatting
- Extend `CSVSchemaParser` to support additional CSV formats

## Requirements

- Python 3.7+
- pandas >= 2.0.0
- dataclasses-json >= 0.6.0
- typing-extensions >= 4.5.0

## License

This project is open source and available under the MIT License.
