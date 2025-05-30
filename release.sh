#!/bin/bash

echo "🧼 Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info

echo "🔨 Building package..."
python -m build

echo "🚀 Uploading to PyPI..."
twine upload dist/*