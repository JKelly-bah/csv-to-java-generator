#!/usr/bin/env python3
"""
CSV Cleaner - Fixes common CSV formatting issues that cause delimiter detection problems
Run this on your CSV file before running generate_uml.py
"""

import sys
import os
import re


def clean_csv_file(input_file, output_file=None):
    """Clean CSV file to fix delimiter detection issues"""
    
    if not os.path.exists(input_file):
        print(f"❌ ERROR: File '{input_file}' not found!")
        return False
    
    # If no output file specified, overwrite the original
    if output_file is None:
        output_file = input_file
        print(f"🔄 Cleaning CSV file: {input_file} (will overwrite original)")
    else:
        print(f"🔄 Cleaning CSV file: {input_file} → {output_file}")
    
    try:
        # Read the original file
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print(f"📄 Original file size: {len(content)} characters")
        
        # Show first few lines before cleaning
        lines = content.split('\n')
        print("\n📋 First 3 lines BEFORE cleaning:")
        for i, line in enumerate(lines[:3], 1):
            print(f"  {i}: {repr(line)}")
        
        # Clean the content
        print("\n🧹 Applying cleaning rules...")
        
        # 1. Fix triple quotes
        if '"""' in content:
            content = content.replace('"""', '"')
            print("  ✓ Fixed triple quotes (\"\"\" → \")")
        
        # 2. Fix double quotes
        if '""' in content:
            content = content.replace('""', '"')
            print("  ✓ Fixed double quotes (\"\" → \")")
        
        # 3. Replace commas inside quoted fields with semicolons
        # This regex finds quoted strings and replaces commas inside them
        def replace_commas_in_quotes(match):
            quoted_text = match.group(0)
            # Replace commas with semicolons inside the quotes
            return quoted_text.replace(',', ';')
        
        # Find quoted strings and replace commas inside them
        original_content = content
        content = re.sub(r'"[^"]*"', replace_commas_in_quotes, content)
        if content != original_content:
            print("  ✓ Replaced commas with semicolons inside quoted fields")
        
        # 4. Remove any remaining problematic quote patterns
        # Remove quotes around entire lines (sometimes Excel adds these)
        lines = content.split('\n')
        cleaned_lines = []
        for line in lines:
            # If entire line is wrapped in quotes, remove them
            if line.startswith('"') and line.endswith('"') and line.count('"') == 2:
                line = line[1:-1]
                print(f"  ✓ Removed quotes around entire line")
            cleaned_lines.append(line)
        content = '\n'.join(cleaned_lines)
        
        # Show first few lines after cleaning
        lines = content.split('\n')
        print("\n📋 First 3 lines AFTER cleaning:")
        for i, line in enumerate(lines[:3], 1):
            print(f"  {i}: {repr(line)}")
        
        # Write the cleaned content
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"\n✅ CSV file cleaned successfully!")
        print(f"📄 Cleaned file size: {len(content)} characters")
        print(f"📁 Output: {output_file}")
        
        # Test if the cleaned file can be parsed
        print("\n🧪 Testing cleaned file...")
        import csv
        try:
            with open(output_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                headers = reader.fieldnames
                print(f"  ✅ Successfully detected headers: {headers}")
                
                # Read first row to test
                try:
                    first_row = next(reader)
                    print(f"  ✅ Successfully read first data row")
                    if 'xpath' in first_row:
                        print(f"  ✅ Found xpath column with value: '{first_row['xpath']}'")
                except StopIteration:
                    print(f"  ⚠️  No data rows found (headers only)")
                    
        except Exception as e:
            print(f"  ❌ WARNING: Cleaned file still has issues: {e}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ ERROR during cleaning: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Clean CSV file to fix delimiter issues"""
    if len(sys.argv) < 2:
        print("Usage: python clean_csv.py input_file.csv [output_file.csv]")
        print("\nExample:")
        print("  python clean_csv.py my_schema.csv")
        print("  python clean_csv.py my_schema.csv clean_schema.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = clean_csv_file(input_file, output_file)
    
    if success:
        print("\n🎉 CSV cleaning completed! You can now run:")
        final_file = output_file if output_file else input_file
        print(f"    python generate_uml.py {final_file}")
    else:
        print("\n💥 CSV cleaning failed. Please check the file manually.")
        sys.exit(1)


if __name__ == "__main__":
    main()
