#!/usr/bin/env python3
"""
CSV Line Fixer - Fixes CSV files where rows got split across multiple lines
Joins lines that don't start with '/' back to the previous line
"""

import sys
import os


def fix_csv_lines(input_file, output_file=None):
    """Fix CSV file by joining split lines"""
    
    if not os.path.exists(input_file):
        print(f"❌ ERROR: File '{input_file}' not found!")
        return False
    
    # If no output file specified, overwrite the original
    if output_file is None:
        output_file = input_file
        print(f"🔄 Fixing CSV lines: {input_file} (will overwrite original)")
    else:
        print(f"🔄 Fixing CSV lines: {input_file} → {output_file}")
    
    try:
        # Read the original file
        with open(input_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        print(f"📄 Original file: {len(lines)} lines")
        
        # Show problematic lines
        print("\n📋 Lines that don't start with '/' or header (will be joined):")
        problem_count = 0
        for i, line in enumerate(lines):
            line_stripped = line.strip()
            # Skip empty lines and check if line doesn't start with '/' or common header terms
            if line_stripped and not line_stripped.startswith('/') and not any(header in line_stripped.lower() for header in ['xpath', 'required', 'optional', 'data_type', 'model']):
                print(f"  Line {i+1}: {repr(line_stripped)}")
                problem_count += 1
                if problem_count >= 10:  # Limit output
                    print(f"  ... and {sum(1 for l in lines[i:] if l.strip() and not l.strip().startswith('/') and not any(h in l.lower() for h in ['xpath', 'required', 'optional', 'data_type', 'model']))} more")
                    break
        
        if problem_count == 0:
            print("  None found - file may already be correct!")
        
        # Fix the lines
        fixed_lines = []
        i = 0
        
        while i < len(lines):
            current_line = lines[i].rstrip('\n\r')  # Remove newline but keep content
            
            # Check if this line starts a new row (starts with '/' or looks like header)
            line_stripped = current_line.strip()
            is_new_row = (
                line_stripped.startswith('/') or 
                any(header in line_stripped.lower() for header in ['xpath', 'required', 'optional', 'data_type', 'model']) or
                i == 0  # First line is always kept as-is
            )
            
            if is_new_row or not line_stripped:
                # This is a proper row start or empty line, keep it
                fixed_lines.append(current_line)
            else:
                # This line doesn't start with '/', so it's probably a continuation
                # Join it to the previous line
                if fixed_lines:  # Make sure we have a previous line
                    # Remove the last newline from the previous line and append this content
                    fixed_lines[-1] = fixed_lines[-1] + ' ' + line_stripped
                    print(f"  ✓ Joined line {i+1} to previous line: {repr(line_stripped[:50])}...")
                else:
                    # No previous line to join to, keep as-is (shouldn't happen normally)
                    fixed_lines.append(current_line)
            
            i += 1
        
        # Convert back to string with newlines
        fixed_content = '\n'.join(fixed_lines)
        
        print(f"\n📊 Results:")
        print(f"  Original lines: {len(lines)}")
        print(f"  Fixed lines: {len(fixed_lines)}")
        print(f"  Lines merged: {len(lines) - len(fixed_lines)}")
        
        # Show first few lines after fixing
        fixed_lines_preview = fixed_content.split('\n')
        print(f"\n📋 First 5 lines AFTER fixing:")
        for i, line in enumerate(fixed_lines_preview[:5], 1):
            print(f"  {i}: {repr(line)}")
        
        # Write the fixed content
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        
        print(f"\n✅ CSV lines fixed successfully!")
        print(f"📁 Output: {output_file}")
        
        # Test if the fixed file can be parsed
        print(f"\n🧪 Testing fixed file...")
        import csv
        try:
            with open(output_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                headers = reader.fieldnames
                print(f"  ✅ Successfully detected headers: {headers}")
                
                # Count rows and check for proper structure
                row_count = 0
                for row in reader:
                    row_count += 1
                    if row_count <= 3:  # Check first few rows
                        xpath = row.get('xpath', '')
                        if xpath and xpath.startswith('/'):
                            print(f"  ✅ Row {row_count}: Valid XPath '{xpath}'")
                        else:
                            print(f"  ⚠️  Row {row_count}: XPath '{xpath}' doesn't start with '/'")
                    elif row_count == 4:
                        print(f"  ... checking remaining rows ...")
                
                print(f"  ✅ Total data rows: {row_count}")
                    
        except Exception as e:
            print(f"  ❌ WARNING: Fixed file still has CSV issues: {e}")
            print(f"  You may need to run clean_csv.py after this to fix delimiter issues.")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ ERROR during line fixing: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Fix CSV file lines that got split incorrectly"""
    if len(sys.argv) < 2:
        print("Usage: python fix_csv_lines.py input_file.csv [output_file.csv]")
        print("\nThis script fixes CSV files where rows got split across multiple lines.")
        print("It joins lines that don't start with '/' back to the previous line.")
        print("\nExamples:")
        print("  python fix_csv_lines.py my_schema.csv")
        print("  python fix_csv_lines.py my_schema.csv fixed_schema.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = fix_csv_lines(input_file, output_file)
    
    if success:
        print("\n🎉 Line fixing completed! You may now want to run:")
        final_file = output_file if output_file else input_file
        print(f"    python clean_csv.py {final_file}      # To fix any remaining delimiter issues")
        print(f"    python generate_uml.py {final_file}   # To generate your UML diagram")
    else:
        print("\n💥 Line fixing failed. Please check the file manually.")
        sys.exit(1)


if __name__ == "__main__":
    main()
