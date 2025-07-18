"""
CSV Schema Parser Module

This module handles reading and parsing CSV files containing XPath schema information.
"""

import pandas as pd
from typing import List, Dict, Any
from dataclasses import dataclass


@dataclass
class SchemaField:
    """Represents a single field from the schema CSV."""
    xpath: str
    required: str  # Changed to string to preserve original value
    data_type: str
    model1_value: str
    model2_value: str
    model3_value: str
    model4_value: str
    additional_info: str = ""  # For any additional columns
    
    @property
    def field_name(self) -> str:
        """Extract field name from XPath."""
        # Extract the last element from xpath as field name
        # e.g., "/root/person/name" -> "name"
        parts = self.xpath.strip('/').split('/')
        return parts[-1] if parts else 'field'
    
    @property
    def is_required(self) -> bool:
        """Check if field is required."""
        return self.required.lower() in ['required', 'true', 'yes', '1']


class CSVSchemaParser:
    """Parser for CSV files containing schema information."""
    
    def __init__(self):
        self.required_columns = [
            'xpath', 'required/optional', 'data_type', 
            'model1', 'model2', 'model3', 'model4'
        ]
    
    def parse_csv(self, file_path: str) -> List[SchemaField]:
        """
        Parse CSV file and return list of SchemaField objects.
        
        Args:
            file_path: Path to the CSV file
            
        Returns:
            List of SchemaField objects
            
        Raises:
            ValueError: If CSV format is invalid
            FileNotFoundError: If file doesn't exist
        """
        try:
            # Read CSV file
            df = pd.read_csv(file_path)
            
            # Validate columns
            self._validate_columns(df.columns.tolist())
            
            # Parse each row into SchemaField objects
            schema_fields = []
            for _, row in df.iterrows():
                # Skip empty rows
                if pd.isna(row['xpath']) or row['xpath'].strip() == '':
                    continue
                
                # Get additional column info (any columns beyond the required ones)
                additional_info = []
                for col in df.columns:
                    if col.lower().strip() not in [req_col.lower().strip() for req_col in self.required_columns]:
                        if pd.notna(row[col]) and str(row[col]).strip():
                            additional_info.append(f"{col}: {str(row[col]).strip()}")
                
                field = SchemaField(
                    xpath=str(row['xpath']).strip(),
                    required=str(row['required/optional']).strip(),
                    data_type=str(row['data_type']).strip(),
                    model1_value=str(row['model1']).strip() if pd.notna(row['model1']) else '',
                    model2_value=str(row['model2']).strip() if pd.notna(row['model2']) else '',
                    model3_value=str(row['model3']).strip() if pd.notna(row['model3']) else '',
                    model4_value=str(row['model4']).strip() if pd.notna(row['model4']) else '',
                    additional_info=' | '.join(additional_info) if additional_info else ''
                )
                schema_fields.append(field)
            
            return schema_fields
            
        except FileNotFoundError:
            raise FileNotFoundError(f"CSV file not found: {file_path}")
        except Exception as e:
            raise ValueError(f"Error parsing CSV file: {e}")
    
    def _validate_columns(self, actual_columns: List[str]) -> None:
        """
        Validate that CSV has expected columns.
        
        Args:
            actual_columns: List of column names from CSV
            
        Raises:
            ValueError: If required columns are missing
        """
        # Normalize column names (strip whitespace, lowercase)
        normalized_actual = [col.strip().lower() for col in actual_columns]
        normalized_required = [col.strip().lower() for col in self.required_columns]
        
        missing_columns = []
        for required_col in normalized_required:
            if required_col not in normalized_actual:
                missing_columns.append(required_col)
        
        if missing_columns:
            raise ValueError(
                f"Missing required columns: {missing_columns}\n"
                f"Required columns: {self.required_columns}\n"
                f"Actual columns: {actual_columns}"
            )
