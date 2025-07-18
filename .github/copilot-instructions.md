<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# CSV to Java Structure Generator - Copilot Instructions

This is a Python application that reads CSV files containing XPath schema information and generates Java-like class structures.

## Project Structure
- `main.py`: Main application entry point
- `src/csv_parser.py`: Handles CSV parsing and validation
- `src/model_generator.py`: Creates model structures from parsed data
- `src/java_structure.py`: Generates Java class files from models
- `sample_schema.csv`: Example CSV file with proper format

## Key Features
- Parses CSV files with XPath, data types, and model configurations
- Generates four different Java model classes based on CSV columns
- Supports conditional field inclusion based on model values
- Handles Java type mapping and proper naming conventions
- Generates complete Java classes with constructors, getters, setters, equals, hashCode, and toString

## CSV Format
Expected columns: xpath, required/optional, data_type, model1, model2, model3, model4, [additional columns...]
- Use "do not use", "skip", "ignore" in model columns to exclude fields
- Supports Java data types: String, Integer, Long, Double, Boolean, LocalDate, LocalDateTime, BigDecimal, List
- Any additional columns beyond the required ones will be included in field comments
- Generated comments include all column information with format: `<columnName>: <value>`

## Generated Comments Format
Each field includes comprehensive documentation:
- `xpath`: The XPath expression from the CSV
- `required/optional`: The requirement status from the CSV
- `data_type`: The Java data type
- `model_value`: The specific value for this model
- `additional_info`: Information from any extra CSV columns
- `default_value`: Default value if specified

## Code Style Guidelines
- Follow Python PEP 8 for Python code
- Generate Java code following standard Java conventions
- Use proper camelCase for Java field names
- Include comprehensive documentation and error handling
