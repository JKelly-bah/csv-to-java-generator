#!/usr/bin/env python3
"""
BOM Fixer - Removes UTF-8 BOM from CSV files
The BOM (Byte Order Mark) \ufeff causes column name mismatches
"""

import sys
import os


def fix_bom_in_csv(input_file, output_file=None):
    """Remove BOM from CSV file"""
    
    if not os.path.exists(input_file):
        print(f"❌ ERROR: File '{input_file}' not found!")
        return False
    
    # If no output file specified, overwrite the original
    if output_file is None:
        output_file = input_file
        print(f"🔄 Removing BOM from: {input_file} (will overwrite original)")
    else:
        print(f"🔄 Removing BOM from: {input_file} → {output_file}")
    
    try:
        # Read the file and check for BOM
        with open(input_file, 'rb') as f:
            raw_content = f.read()
        
        print(f"📄 Original file size: {len(raw_content)} bytes")
        
        # Check if file starts with UTF-8 BOM
        if raw_content.startswith(b'\xef\xbb\xbf'):
            print("🔍 UTF-8 BOM detected! Removing...")
            # Remove the BOM (first 3 bytes)
            raw_content = raw_content[3:]
            print(f"✅ BOM removed. New size: {len(raw_content)} bytes")
        else:
            print("ℹ️  No UTF-8 BOM found, but checking for other issues...")
        
        # Convert to text and check for Unicode BOM character
        try:
            content = raw_content.decode('utf-8')
        except UnicodeDecodeError:
            # Try other encodings
            try:
                content = raw_content.decode('utf-8-sig')  # This automatically removes BOM
                print("✅ Decoded with UTF-8-SIG (BOM handling)")
            except UnicodeDecodeError:
                content = raw_content.decode('windows-1252')
                print("✅ Decoded with Windows-1252")
        else:
            print("✅ Decoded with UTF-8")
        
        # Remove Unicode BOM character if present
        if content.startswith('\ufeff'):
            print("🔍 Unicode BOM character (\\ufeff) found in text! Removing...")
            content = content[1:]
            print("✅ Unicode BOM character removed")
        
        # Show first line after cleaning
        first_line = content.split('\n')[0]
        print(f"📋 First line after cleaning: {repr(first_line)}")
        
        # Write the cleaned content
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"\n✅ BOM removal completed!")
        print(f"📁 Output: {output_file}")
        
        # Test the result
        print(f"\n🧪 Testing cleaned file...")
        import csv
        try:
            with open(output_file, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                headers = reader.fieldnames
                print(f"  ✅ Column headers: {headers}")
                
                if headers:
                    first_header = headers[0]
                    print(f"  ✅ First header: '{first_header}' (len={len(first_header)}, repr={repr(first_header)})")
                    
                    if first_header == 'xpath':
                        print("  🎉 SUCCESS! First column is now exactly 'xpath'")
                    else:
                        print(f"  ⚠️  First column is still not 'xpath': {repr(first_header)}")
                        
        except Exception as e:
            print(f"  ❌ ERROR testing cleaned file: {e}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ ERROR during BOM removal: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Remove BOM from CSV file"""
    if len(sys.argv) < 2:
        print("Usage: python fix_bom.py input_file.csv [output_file.csv]")
        print("\nThis script removes UTF-8 BOM (Byte Order Mark) from CSV files.")
        print("The BOM causes column names like '\\ufeffxpath' instead of 'xpath'.")
        print("\nExamples:")
        print("  python fix_bom.py my_schema.csv")
        print("  python fix_bom.py my_schema.csv cleaned_schema.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = fix_bom_in_csv(input_file, output_file)
    
    if success:
        print("\n🎉 BOM removal completed! You can now run:")
        final_file = output_file if output_file else input_file
        print(f"    python generate_uml.py {final_file}")
    else:
        print("\n💥 BOM removal failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
