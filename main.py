#!/usr/bin/env python3
"""
CSV to Java Structure Generator

This application reads a CSV file containing XPath schema information and generates
Java-like class structures for four different models.

Usage:
    python main.py <csv_file_path> [output_directory]

CSV Format:
    xpath, required/optional, data_type, model1, model2, model3, model4
"""

import sys
import os
from pathlib import Path
from typing import Optional

from src.csv_parser import CSVSchemaParser
from src.model_generator import ModelGenerator
from src.java_structure import JavaStructureGenerator


def main():
    """Main entry point for the application."""
    if len(sys.argv) < 2:
        print("Usage: python main.py <csv_file_path> [output_directory]")
        print("\nExample:")
        print("python main.py schema.csv output/")
        sys.exit(1)
    
    csv_file_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "output"
    
    # Validate input file
    if not os.path.exists(csv_file_path):
        print(f"Error: CSV file '{csv_file_path}' not found.")
        sys.exit(1)
    
    # Create output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    try:
        # Parse CSV schema
        print(f"Reading schema from {csv_file_path}...")
        parser = CSVSchemaParser()
        schema_data = parser.parse_csv(csv_file_path)
        
        # Generate models
        print("Generating Java-like class structures...")
        model_generator = ModelGenerator()
        models = model_generator.generate_models(schema_data)
        
        # Generate Java structure files
        java_generator = JavaStructureGenerator()
        java_generator.generate_java_files(models, output_dir)
        
        print(f"\nSuccess! Generated {len(models)} model files in '{output_dir}' directory:")
        for model_name in models.keys():
            print(f"  - {model_name}.java")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
