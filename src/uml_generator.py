"""
UML Diagram Generator for CSV Schema
Generates PlantUML diagrams from CSV schema files
"""

import csv
import os
from typing import Dict, List, Tuple, Set


class UMLGenerator:
    """Generates UML class diagrams from CSV schema data"""
    
    def __init__(self):
        self.java_type_mapping = {
            'String': 'String',
            'Integer': 'int',
            'Long': 'long',
            'Double': 'double',
            'Boolean': 'boolean',
            'LocalDate': 'LocalDate',
            'LocalDateTime': 'LocalDateTime',
            'BigDecimal': 'BigDecimal',
            'List': 'List'
        }
    
    def generate_plantuml(self, csv_file_path: str, output_file_path: str) -> None:
        """Generate PlantUML diagram from CSV schema"""
        schema_data = self._parse_csv_file(csv_file_path)
        
        # Generate UML content
        uml_content = self._create_plantuml_content(schema_data)
        
        # Write to file
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(uml_content)
        
        print(f"UML diagram generated: {output_file_path}")
    
    def _parse_csv_file(self, csv_file_path: str) -> List[Dict]:
        """Parse CSV file and return schema data"""
        schema_data = []
        delimiter = ','  # Initialize with default
        
        try:
            # First, read and clean the CSV content
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Clean up problematic quotes while preserving commas
                # Remove multiple consecutive quotes but keep single quotes if needed
                import re
                # Replace 3+ quotes with single quote
                content = re.sub(r'"{3,}', '"', content)
                # Replace double quotes that aren't at field boundaries
                content = re.sub(r'""(?!")', '', content)
                
                # Create a StringIO object for csv.DictReader
                from io import StringIO
                cleaned_file = StringIO(content)
                
                # Use csv.Sniffer to detect delimiter
                sample = content[:1024]
                sniffer = csv.Sniffer()
                
                try:
                    delimiter = sniffer.sniff(sample).delimiter
                    print(f"Auto-detected delimiter: {repr(delimiter)}")
                except csv.Error:
                    # Try common delimiters in order of preference
                    for test_delimiter in [',', ';', '\t', '|']:
                        if test_delimiter in sample:
                            delimiter = test_delimiter
                            print(f"Using delimiter: {repr(delimiter)}")
                            break
                    else:
                        # Fallback to comma if no delimiter found
                        delimiter = ','
                        print(f"Using default delimiter: {repr(delimiter)}")
                
                # Parse the cleaned content
                reader = csv.DictReader(
                    cleaned_file, 
                    delimiter=delimiter,
                    quotechar='"',
                    quoting=csv.QUOTE_MINIMAL,
                    skipinitialspace=True
                )
                
                for row_num, row in enumerate(reader, start=2):  # Start at 2 since row 1 is headers
                    # Clean up the row data
                    cleaned_row = {}
                    for key, value in row.items():
                        if key is None:
                            continue  # Skip None keys from malformed CSV
                        
                        # Clean the key and value
                        cleaned_key = key.strip() if key else key
                        cleaned_value = value.strip() if value else value
                        
                        cleaned_row[cleaned_key] = cleaned_value
                    
                    # Only add rows that have an xpath value
                    if cleaned_row.get('xpath'):
                        schema_data.append(cleaned_row)
                    elif any(cleaned_row.values()):  # Row has some data but no xpath
                        print(f"⚠️  Warning: Row {row_num} has data but missing xpath: {cleaned_row}")
                        
        except UnicodeDecodeError:
            # Try with different encodings if UTF-8 fails
            for encoding in ['latin1', 'cp1252', 'iso-8859-1']:
                try:
                    with open(csv_file_path, 'r', encoding=encoding) as file:
                        content = file.read()
                        # Apply same cleaning
                        import re
                        content = re.sub(r'"{3,}', '"', content)
                        content = re.sub(r'""(?!")', '', content)
                        
                        from io import StringIO
                        cleaned_file = StringIO(content)
                        reader = csv.DictReader(
                            cleaned_file, 
                            delimiter=delimiter,
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL,
                            skipinitialspace=True
                        )
                        schema_data = []
                        for row in reader:
                            cleaned_row = {}
                            for key, value in row.items():
                                if key is None:
                                    continue
                                cleaned_key = key.strip() if key else key
                                cleaned_value = value.strip() if value else value
                                cleaned_row[cleaned_key] = cleaned_value
                            
                            if cleaned_row.get('xpath'):
                                schema_data.append(cleaned_row)
                        break
                except UnicodeDecodeError:
                    continue
            else:
                raise Exception("Could not decode CSV file with any common encoding")
        
        return schema_data
    
    def _create_plantuml_content(self, schema_data: List[Dict]) -> str:
        """Create PlantUML content from schema data"""
        uml_lines = [
            "@startuml CSV Schema Models",
            "!theme plain",
            "skinparam classAttributeIconSize 0",
            "skinparam classFontStyle bold",
            "skinparam classBackgroundColor lightblue",
            "skinparam classHeaderBackgroundColor darkblue",
            "skinparam classHeaderFontColor white",
            "",
            "title CSV Schema - Java Models UML Diagram",
            ""
        ]
        
        # Generate classes for each model
        for model_num in range(1, 5):
            model_name = f"Model{model_num}"
            fields = self._get_model_fields(schema_data, f"model{model_num}")
            
            if fields:
                uml_lines.extend(self._create_class_definition(model_name, fields))
                uml_lines.append("")
        
        # Add relationships if any common fields exist
        relationships = self._find_relationships(schema_data)
        if relationships:
            uml_lines.extend(relationships)
            uml_lines.append("")
        
        # Add notes with additional information
        uml_lines.extend(self._create_notes(schema_data))
        
        uml_lines.append("@enduml")
        
        return "\n".join(uml_lines)
    
    def _get_model_fields(self, schema_data: List[Dict], model_column: str) -> List[Tuple[str, str, str]]:
        """Get fields for a specific model"""
        fields = []
        
        for row in schema_data:
            model_value = row.get(model_column, '').strip().lower()
            
            # Skip if field should not be included in this model
            if model_value in ['do not use', 'skip', 'ignore', '']:
                continue
            
            xpath = row.get('xpath', '')
            data_type = row.get('data_type', 'String')
            required = row.get('required/optional', 'optional')
            
            # Convert xpath to field name
            field_name = self._xpath_to_field_name(xpath)
            
            # Parse data type and handle constraints like "String [0,17]"
            java_type = self._parse_data_type(data_type)
            
            fields.append((field_name, java_type, required))
        
        return fields
    
    def _parse_data_type(self, data_type: str) -> str:
        """Parse data type and handle constraints"""
        if not data_type:
            return 'String'
        
        data_type = data_type.strip()
        
        # Handle types with constraints like "String [0,17]"
        if '[' in data_type and ']' in data_type:
            # Extract base type before the bracket
            base_type = data_type.split('[')[0].strip()
            constraint = data_type.split('[')[1].split(']')[0].strip()
            
            # Map base type to Java type
            java_base_type = self.java_type_mapping.get(base_type, base_type)
            
            # For UML, we can show the constraint as additional info
            # Option 1: Just return base type
            # return java_base_type
            
            # Option 2: Include constraint in type (for UML documentation)
            return f"{java_base_type} [{constraint}]"
        else:
            # No constraints, just map the type
            return self.java_type_mapping.get(data_type, data_type)
    
    def _xpath_to_field_name(self, xpath: str) -> str:
        """Convert XPath to Java field name"""
        if not xpath:
            return "unknownField"
        
        # Handle attribute references (e.g., "../../@attribute" or "/path/@attr/sub")
        if '@' in xpath:
            # Extract everything after the @ symbol
            attribute_part = xpath.split('@')[-1]
            # Remove any trailing brackets or conditions
            attribute_part = attribute_part.split('[')[0].strip()
            
            # If there are additional path segments after @, take the last one
            # e.g., @name/first -> first, @attribute -> attribute
            if '/' in attribute_part:
                field_name = attribute_part.split('/')[-1]
            else:
                field_name = attribute_part
        else:
            # Extract the last part of the xpath
            parts = xpath.split('/')
            field_name = parts[-1] if parts else xpath
            # Remove any brackets or array notation
            field_name = field_name.split('[')[0]
        
        # Clean up the field name
        field_name = field_name.strip()
        if not field_name:
            return "unknownField"
        
        # Convert to camelCase
        words = field_name.replace('-', '_').replace('.', '_').split('_')
        if len(words) > 1:
            field_name = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
        else:
            field_name = field_name.lower()
        
        return field_name if field_name else "unknownField"
    
    def _create_class_definition(self, class_name: str, fields: List[Tuple[str, str, str]]) -> List[str]:
        """Create PlantUML class definition"""
        lines = [f"class {class_name} {{"]
        
        # Add fields
        for field_name, java_type, required in fields:
            required_marker = " {field}" if required.lower() == 'required' else ""
            lines.append(f"  - {field_name}: {java_type}{required_marker}")
        
        lines.append("  --")
        
        # Add constructor
        if fields:
            constructor_params = ", ".join([f"{java_type} {field_name}" for field_name, java_type, _ in fields])
            lines.append(f"  + {class_name}({constructor_params})")
        else:
            lines.append(f"  + {class_name}()")
        
        lines.append("  --")
        
        # Add getters and setters
        for field_name, java_type, _ in fields:
            getter_name = f"get{field_name.capitalize()}"
            setter_name = f"set{field_name.capitalize()}"
            lines.append(f"  + {getter_name}(): {java_type}")
            lines.append(f"  + {setter_name}({java_type}): void")
        
        # Add standard methods
        lines.append("  --")
        lines.append("  + equals(Object): boolean")
        lines.append("  + hashCode(): int")
        lines.append("  + toString(): String")
        
        lines.append("}")
        
        return lines
    
    def _find_relationships(self, schema_data: List[Dict]) -> List[str]:
        """Find relationships between models based on common fields"""
        relationships = []
        
        # Get field sets for each model
        model_fields = {}
        for model_num in range(1, 5):
            model_name = f"Model{model_num}"
            fields = self._get_model_fields(schema_data, f"model{model_num}")
            if fields:
                model_fields[model_name] = set(field[0] for field in fields)
        
        # Find common fields and create relationships
        model_names = list(model_fields.keys())
        for i in range(len(model_names)):
            for j in range(i + 1, len(model_names)):
                model1 = model_names[i]
                model2 = model_names[j]
                
                common_fields = model_fields[model1] & model_fields[model2]
                if common_fields:
                    # Create association based on number of common fields
                    if len(common_fields) > 3:
                        relationships.append(f"{model1} ||--|| {model2} : shares {len(common_fields)} fields")
                    else:
                        relationships.append(f"{model1} ..> {model2} : common fields")
        
        return relationships
    
    def _create_notes(self, schema_data: List[Dict]) -> List[str]:
        """Create notes with additional information"""
        notes = [
            "note top : Generated from CSV Schema",
            f"note bottom : Total Fields: {len(schema_data)}",
        ]
        
        # Count required vs optional fields
        required_count = sum(1 for row in schema_data if row.get('required/optional', '').lower() == 'required')
        optional_count = len(schema_data) - required_count
        
        notes.append(f"note bottom : Required: {required_count}, Optional: {optional_count}")
        
        return notes


def main():
    """Main function to generate UML diagram"""
    import sys
    
    if len(sys.argv) != 3:
        print("Usage: python -m src.uml_generator <csv_file> <output_file>")
        sys.exit(1)
    
    csv_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found")
        sys.exit(1)
    
    generator = UMLGenerator()
    generator.generate_plantuml(csv_file, output_file)
    
    print(f"UML diagram generated successfully!")
    print(f"To view the diagram:")
    print(f"1. Install PlantUML: https://plantuml.com/starting")
    print(f"2. Generate image: plantuml {output_file}")
    print(f"3. Or use online viewer: https://www.plantuml.com/plantuml/uml/")


if __name__ == "__main__":
    main()
