#!/usr/bin/env python3
"""
Debug UML Generator - Shows detailed parsing information
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.uml_generator import UMLGenerator
import csv


def debug_csv_parsing(csv_file_path):
    """Debug CSV parsing to identify issues"""
    print(f"🔍 Debugging CSV file: {csv_file_path}")
    print("=" * 60)
    
    if not os.path.exists(csv_file_path):
        print(f"❌ ERROR: File '{csv_file_path}' not found!")
        return
    
    try:
        # Check file encoding and content
        with open(csv_file_path, 'r', encoding='utf-8') as f:
            first_lines = [f.readline().strip() for _ in range(5)]
        
        print("📄 First 5 lines of file:")
        for i, line in enumerate(first_lines, 1):
            print(f"  {i}: {repr(line)}")
        
        print("\n" + "─" * 60)
        
        # Test CSV parsing
        generator = UMLGenerator()
        schema_data = generator._parse_csv_file(csv_file_path)
        
        print(f"📊 Parsed {len(schema_data)} rows")
        print("\n🔍 First 3 parsed rows:")
        
        for i, row in enumerate(schema_data[:3]):
            print(f"\nRow {i+1}:")
            for key, value in row.items():
                print(f"  '{key}': '{value}'")
            
            # Test XPath conversion
            xpath = row.get('xpath', '')
            print(f"  XPath: '{xpath}' (type: {type(xpath).__name__}, len: {len(xpath) if xpath else 0})")
            if xpath:
                field_name = generator._xpath_to_field_name(xpath)
                print(f"  → Field name: '{field_name}'")
                if field_name == 'unknownField':
                    print(f"  ⚠️  WARNING: XPath '{xpath}' resulted in 'unknownField'")
                    # Debug the parsing steps
                    if '@' in xpath:
                        attribute_part = xpath.split('@')[-1]
                        print(f"      After @ split: '{attribute_part}'")
                        attribute_part = attribute_part.split('[')[0].strip()
                        print(f"      After bracket removal: '{attribute_part}'")
                        if '/' in attribute_part:
                            final_part = attribute_part.split('/')[-1]
                            print(f"      Final part after /: '{final_part}'")
            else:
                print(f"  → Field name: 'unknownField' (empty or None xpath)")
                print(f"  ⚠️  WARNING: XPath is empty, None, or missing!")
        
        print("\n" + "─" * 60)
        
        # Test model field extraction
        print("🏗️ Model field extraction test:")
        for model_num in range(1, 5):
            model_column = f"model{model_num}"
            fields = generator._get_model_fields(schema_data, model_column)
            print(f"  Model{model_num} ({model_column}): {len(fields)} fields")
            if fields:
                print(f"    First 3 fields: {fields[:3]}")
            else:
                print(f"    No fields found!")
                # Debug why no fields
                print(f"    Available columns: {list(schema_data[0].keys()) if schema_data else 'No data'}")
                if schema_data:
                    sample_row = schema_data[0]
                    model_value = sample_row.get(model_column, 'MISSING_COLUMN')
                    print(f"    Sample {model_column} value: '{model_value}'")
    
    except Exception as e:
        print(f"❌ ERROR during parsing: {str(e)}")
        import traceback
        traceback.print_exc()


def main():
    """Debug CSV parsing and field name generation"""
    csv_file = sys.argv[1] if len(sys.argv) > 1 else "sample_schema.csv"
    debug_csv_parsing(csv_file)


if __name__ == "__main__":
    main()
