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
        
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            # Use csv.Sniffer to detect delimiter
            sample = file.read(1024)
            file.seek(0)
            sniffer = csv.Sniffer()
            delimiter = sniffer.sniff(sample).delimiter
            
            reader = csv.DictReader(file, delimiter=delimiter)
            for row in reader:
                # Clean up the row data
                cleaned_row = {}
                for key, value in row.items():
                    cleaned_key = key.strip() if key else key
                    cleaned_value = value.strip() if value else value
                    cleaned_row[cleaned_key] = cleaned_value
                
                schema_data.append(cleaned_row)
        
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
            
            # Map to Java type
            java_type = self.java_type_mapping.get(data_type, data_type)
            
            fields.append((field_name, java_type, required))
        
        return fields
    
    def _xpath_to_field_name(self, xpath: str) -> str:
        """Convert XPath to Java field name"""
        if not xpath:
            return "unknownField"
        
        # Extract the last part of the xpath
        parts = xpath.split('/')
        field_name = parts[-1] if parts else xpath
        
        # Remove any brackets or special characters
        field_name = field_name.split('[')[0]  # Remove array notation
        field_name = field_name.replace('@', '')  # Remove attribute symbol
        
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
