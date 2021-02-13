#!/usr/bin/env bash
echo "Removing unused imports"
JAVA_FILES=$1/*.java
for f in $JAVA_FILES; do
    echo "Removing unused import in $f"
    sed -i 's/import org.openapitools.jackson.nullable.JsonNullable;//g' $f
done