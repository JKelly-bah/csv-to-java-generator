"""
Model Generator Module

This module creates data models based on parsed CSV schema information.
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from src.csv_parser import SchemaField


@dataclass
class ModelField:
    """Represents a field in a generated model."""
    name: str
    data_type: str
    required: bool
    default_value: Optional[str] = None
    description: Optional[str] = None
    xpath: Optional[str] = None
    required_optional_status: Optional[str] = None
    model_value: Optional[str] = None
    additional_info: Optional[str] = None


@dataclass
class Model:
    """Represents a complete model/class structure."""
    name: str
    fields: List[ModelField]
    package_name: str = "com.example.models"
    
    @property
    def class_name(self) -> str:
        """Get properly formatted class name."""
        # Capitalize first letter and ensure proper Java naming
        return self.name.replace("_", "").replace("-", "").title()


class ModelGenerator:
    """Generates model structures from schema data."""
    
    def __init__(self):
        self.java_type_mapping = {
            'string': 'String',
            'str': 'String',
            'integer': 'Integer',
            'int': 'Integer',
            'long': 'Long',
            'double': 'Double',
            'float': 'Float',
            'boolean': 'Boolean',
            'bool': 'Boolean',
            'date': 'LocalDate',
            'datetime': 'LocalDateTime',
            'timestamp': 'LocalDateTime',
            'decimal': 'BigDecimal',
            'list': 'List<String>',
            'array': 'List<String>'
        }
    
    def generate_models(self, schema_fields: List[SchemaField]) -> Dict[str, Model]:
        """
        Generate four different models based on schema data.
        
        Args:
            schema_fields: List of parsed schema fields
            
        Returns:
            Dictionary with model names as keys and Model objects as values
        """
        models = {}
        
        # Generate each of the four models
        for model_num in range(1, 5):
            model_name = f"Model{model_num}"
            model_fields = self._generate_model_fields(schema_fields, model_num)
            
            models[model_name] = Model(
                name=model_name,
                fields=model_fields,
                package_name="com.example.models"
            )
        
        return models
    
    def _generate_model_fields(self, schema_fields: List[SchemaField], model_num: int) -> List[ModelField]:
        """
        Generate fields for a specific model based on schema data.
        
        Args:
            schema_fields: List of schema fields
            model_num: Model number (1-4)
            
        Returns:
            List of ModelField objects
        """
        model_fields = []
        
        for schema_field in schema_fields:
            # Get the value for this specific model
            model_value = self._get_model_value(schema_field, model_num)
            
            # Skip if value indicates "do not use"
            if self._should_skip_field(model_value):
                continue
            
            # Create model field
            field_name = self._camel_case(schema_field.field_name)
            java_type = self._map_to_java_type(schema_field.data_type)
            
            model_field = ModelField(
                name=field_name,
                data_type=java_type,
                required=schema_field.is_required,
                default_value=model_value if model_value and model_value != schema_field.field_name else None,
                description=f"Field mapped from XPath: {schema_field.xpath}",
                xpath=schema_field.xpath,
                required_optional_status=schema_field.required,
                model_value=model_value,
                additional_info=schema_field.additional_info
            )
            
            model_fields.append(model_field)
        
        return model_fields
    
    def _get_model_value(self, schema_field: SchemaField, model_num: int) -> str:
        """Get the value for a specific model from schema field."""
        model_values = {
            1: schema_field.model1_value,
            2: schema_field.model2_value,
            3: schema_field.model3_value,
            4: schema_field.model4_value
        }
        return model_values.get(model_num, '')
    
    def _should_skip_field(self, model_value: str) -> bool:
        """Check if field should be skipped based on model value."""
        skip_indicators = [
            'do not use', 'skip', 'ignore', 'exclude', 
            'n/a', 'na', 'null', 'none', '-'
        ]
        return model_value.lower().strip() in skip_indicators
    
    def _camel_case(self, snake_str: str) -> str:
        """Convert snake_case or kebab-case to camelCase."""
        # Handle various separators
        for separator in ['_', '-', '.', '/']:
            snake_str = snake_str.replace(separator, '_')
        
        components = snake_str.split('_')
        # Keep first component lowercase, capitalize rest
        return components[0].lower() + ''.join(word.capitalize() for word in components[1:])
    
    def _map_to_java_type(self, data_type: str) -> str:
        """Map string data type to Java type."""
        normalized_type = data_type.lower().strip()
        return self.java_type_mapping.get(normalized_type, 'String')  # Default to String
