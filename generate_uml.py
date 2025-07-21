#!/usr/bin/env python3
"""
UML Diagram Generator Script
Generates UML diagrams from CSV schema files
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.uml_generator import UMLGenerator


def main():
    """Generate UML diagram from CSV file"""
    
    # Default files
    csv_file = "sample_schema.csv"
    output_file = "output/schema_uml.puml"
    
    # Check for command line arguments
    if len(sys.argv) >= 2:
        csv_file = sys.argv[1]
    if len(sys.argv) >= 3:
        output_file = sys.argv[2]
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Check if CSV file exists
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found")
        print("Available files:")
        for file in os.listdir('.'):
            if file.endswith('.csv'):
                print(f"  - {file}")
        sys.exit(1)
    
    try:
        # Generate UML diagram
        generator = UMLGenerator()
        generator.generate_plantuml(csv_file, output_file)
        
        print(f"✅ UML diagram generated successfully!")
        print(f"📁 Input: {csv_file}")
        print(f"📄 Output: {output_file}")
        print()
        print("🔍 To view the diagram:")
        print("1. Install PlantUML: https://plantuml.com/starting")
        print(f"2. Generate image: plantuml {output_file}")
        print("3. Or use online viewer: https://www.plantuml.com/plantuml/uml/")
        print(f"4. Or paste content into: http://www.plantuml.com/plantuml/uml/")
        
    except Exception as e:
        print(f"❌ Error generating UML diagram: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
