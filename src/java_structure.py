"""
Java Structure Generator Module

This module generates Java class files from model structures.
"""

from typing import Dict
from pathlib import Path
from src.model_generator import Model, ModelField


class JavaStructureGenerator:
    """Generates Java class files from model structures."""
    
    def __init__(self):
        self.imports = {
            'LocalDate': 'java.time.LocalDate',
            'LocalDateTime': 'java.time.LocalDateTime',
            'BigDecimal': 'java.math.BigDecimal',
            'List': 'java.util.List',
            'ArrayList': 'java.util.ArrayList'
        }
    
    def generate_java_files(self, models: Dict[str, Model], output_dir: str) -> None:
        """
        Generate Java class files for all models.
        
        Args:
            models: Dictionary of model name to Model objects
            output_dir: Output directory for generated files
        """
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
        
        for model_name, model in models.items():
            java_content = self._generate_java_class(model)
            file_path = output_path / f"{model.class_name}.java"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(java_content)
    
    def _generate_java_class(self, model: Model) -> str:
        """
        Generate Java class content for a model.
        
        Args:
            model: Model object to generate Java class for
            
        Returns:
            Java class content as string
        """
        # Collect required imports
        required_imports = self._get_required_imports(model)
        
        # Generate class content
        class_content = []
        
        # Package declaration
        class_content.append(f"package {model.package_name};")
        class_content.append("")
        
        # Imports
        if required_imports:
            for import_statement in sorted(required_imports):
                class_content.append(f"import {import_statement};")
            class_content.append("")
        
        # Class documentation
        class_content.append("/**")
        class_content.append(f" * {model.class_name} - Auto-generated model class")
        class_content.append(" * Generated from CSV schema definition")
        class_content.append(" */")
        
        # Class declaration
        class_content.append(f"public class {model.class_name} {{")
        class_content.append("")
        
        # Field declarations
        for field in model.fields:
            class_content.extend(self._generate_field_declaration(field))
        
        # Default constructor
        class_content.append("    /**")
        class_content.append("     * Default constructor")
        class_content.append("     */")
        class_content.append(f"    public {model.class_name}() {{")
        class_content.append("    }")
        class_content.append("")
        
        # Parameterized constructor
        if model.fields:
            class_content.extend(self._generate_parameterized_constructor(model))
        
        # Getters and setters
        for field in model.fields:
            class_content.extend(self._generate_getter_setter(field))
        
        # toString method
        class_content.extend(self._generate_to_string_method(model))
        
        # equals and hashCode methods
        class_content.extend(self._generate_equals_method(model))
        class_content.extend(self._generate_hash_code_method(model))
        
        # Close class
        class_content.append("}")
        
        return "\n".join(class_content)
    
    def _get_required_imports(self, model: Model) -> set:
        """Get required import statements for the model."""
        required_imports = set()
        
        for field in model.fields:
            data_type = field.data_type
            if data_type in self.imports:
                required_imports.add(self.imports[data_type])
            elif data_type.startswith('List<'):
                required_imports.add(self.imports['List'])
        
        return required_imports
    
    def _generate_field_declaration(self, field: ModelField) -> list:
        """Generate field declaration with comprehensive documentation."""
        lines = []
        
        # Field documentation
        lines.append("    /**")
        
        # XPath information
        if field.xpath:
            lines.append(f"     * xpath: {field.xpath}")
        
        # Required/Optional status
        if field.required_optional_status:
            lines.append(f"     * required/optional: {field.required_optional_status}")
        
        # Data type
        lines.append(f"     * data_type: {field.data_type}")
        
        # Model value for this specific model
        if field.model_value:
            lines.append(f"     * model_value: {field.model_value}")
        
        # Additional info from extra columns
        if field.additional_info:
            lines.append(f"     * additional_info: {field.additional_info}")
        
        # Default value
        if field.default_value:
            lines.append(f"     * default_value: {field.default_value}")
        
        lines.append("     */")
        
        # Field declaration
        field_line = f"    private {field.data_type} {field.name}"
        if field.default_value and field.data_type == "String":
            field_line += f' = "{field.default_value}"'
        field_line += ";"
        
        lines.append(field_line)
        lines.append("")
        
        return lines
    
    def _generate_parameterized_constructor(self, model: Model) -> list:
        """Generate parameterized constructor."""
        lines = []
        
        # Constructor documentation
        lines.append("    /**")
        lines.append("     * Parameterized constructor")
        for field in model.fields:
            lines.append(f"     * @param {field.name} {field.description or field.name}")
        lines.append("     */")
        
        # Constructor signature
        params = [f"{field.data_type} {field.name}" for field in model.fields]
        lines.append(f"    public {model.class_name}({', '.join(params)}) {{")
        
        # Constructor body
        for field in model.fields:
            lines.append(f"        this.{field.name} = {field.name};")
        
        lines.append("    }")
        lines.append("")
        
        return lines
    
    def _generate_getter_setter(self, field: ModelField) -> list:
        """Generate getter and setter methods for a field."""
        lines = []
        
        # Getter
        getter_name = f"get{field.name.capitalize()}"
        lines.append(f"    /**")
        lines.append(f"     * Get {field.name}")
        lines.append(f"     * @return {field.data_type}")
        lines.append(f"     */")
        lines.append(f"    public {field.data_type} {getter_name}() {{")
        lines.append(f"        return {field.name};")
        lines.append("    }")
        lines.append("")
        
        # Setter
        setter_name = f"set{field.name.capitalize()}"
        lines.append(f"    /**")
        lines.append(f"     * Set {field.name}")
        lines.append(f"     * @param {field.name} {field.data_type}")
        lines.append(f"     */")
        lines.append(f"    public void {setter_name}({field.data_type} {field.name}) {{")
        lines.append(f"        this.{field.name} = {field.name};")
        lines.append("    }")
        lines.append("")
        
        return lines
    
    def _generate_to_string_method(self, model: Model) -> list:
        """Generate toString method."""
        lines = []
        
        lines.append("    /**")
        lines.append("     * String representation of the object")
        lines.append("     * @return String")
        lines.append("     */")
        lines.append("    @Override")
        lines.append("    public String toString() {")
        
        if model.fields:
            field_strings = [f'"{field.name}=" + {field.name}' for field in model.fields]
            toString_content = f'"{model.class_name}{{" + ' + ' + ", " + '.join(field_strings) + ' + "}"'
            lines.append(f"        return {toString_content};")
        else:
            lines.append(f'        return "{model.class_name}{{}}";')
        
        lines.append("    }")
        lines.append("")
        
        return lines
    
    def _generate_equals_method(self, model: Model) -> list:
        """Generate equals method."""
        lines = []
        
        lines.append("    /**")
        lines.append("     * Check equality with another object")
        lines.append("     * @param obj Object to compare")
        lines.append("     * @return boolean")
        lines.append("     */")
        lines.append("    @Override")
        lines.append("    public boolean equals(Object obj) {")
        lines.append("        if (this == obj) return true;")
        lines.append("        if (obj == null || getClass() != obj.getClass()) return false;")
        lines.append(f"        {model.class_name} that = ({model.class_name}) obj;")
        
        if model.fields:
            conditions = []
            for field in model.fields:
                if field.data_type in ['String', 'BigDecimal'] or field.data_type.startswith('List'):
                    conditions.append(f"java.util.Objects.equals({field.name}, that.{field.name})")
                else:
                    conditions.append(f"java.util.Objects.equals({field.name}, that.{field.name})")
            
            lines.append(f"        return {' && '.join(conditions)};")
        else:
            lines.append("        return true;")
        
        lines.append("    }")
        lines.append("")
        
        return lines
    
    def _generate_hash_code_method(self, model: Model) -> list:
        """Generate hashCode method."""
        lines = []
        
        lines.append("    /**")
        lines.append("     * Generate hash code")
        lines.append("     * @return int")
        lines.append("     */")
        lines.append("    @Override")
        lines.append("    public int hashCode() {")
        
        if model.fields:
            field_names = [field.name for field in model.fields]
            lines.append(f"        return java.util.Objects.hash({', '.join(field_names)});")
        else:
            lines.append("        return 0;")
        
        lines.append("    }")
        lines.append("")
        
        return lines
