#!/bin/bash

# generate_docs.sh - Auto-generates UML diagrams from PlantUML files

# Enhanced dependency check with cross-platform support
DEP_ERROR="Error: PlantUML is required but not installed."

# Check for PlantUML in Unix-like and Windows environments
if command -v plantuml &>/dev/null; then
    UML_CMD="plantuml"
elif command -v plantuml.bat &>/dev/null; then
    UML_CMD="plantuml.bat"
else
    echo "$DEP_ERROR" >&2
    echo "Installation options:" >&2
    echo "  Linux:   sudo apt install plantuml" >&2
    echo "  macOS:   brew install plantuml" >&2
    echo "  Windows: choco install plantuml" >&2
    echo "Or download from: https://plantuml.com/download" >&2
    exit 1
fi

# Configuration
UML_SOURCE_DIR="./docs/uml"
OUTPUT_DIR="./docs/diagrams"
FORMATS="png svg"  # Multiple output formats

# Create output directory if needed
mkdir -p "$OUTPUT_DIR"

# Process all PlantUML files
echo "Generating diagrams..."
for file in "$UML_SOURCE_DIR"/*.{puml,wsd,pu}; do
    if [ -f "$file" ]; then
        echo "Processing $(basename "$file")..."
        $UML_CMD -o "../diagrams" -t"$FORMATS" "$file"
    fi
done

echo "Diagrams generated in $OUTPUT_DIR"
