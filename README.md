# Config Validator 🛠️

A lightweight Python CLI tool to validate **JSON** and **YAML** configuration files against a **JSON Schema**.

This utility helps catch missing fields, incorrect data types, and invalid structures *before* configuration files are used in applications, deployments, or CI/CD pipelines.

---

## Features

- ✅ Supports **JSON** and **YAML** configuration files  
- ✅ Validates against **JSON Schema**  
- ✅ Simple command-line interface  
- ✅ Fails fast with clear validation errors  

---

## Requirements

- Python **3.8+**
- Python packages:
  - `pyyaml`
  - `jsonschema`

Install dependencies:

```bash
pip install pyyaml jsonschema
```

---

## Usage

### Command format

```bash
python config_checker.py <config_file> <schema_file>
```

### Example

```bash
python config_checker.py app_config.yaml schema.json
```

If the configuration is valid:

```text
Configuration file is valid according to the schema.
```

If invalid, a descriptive error will be raised by `jsonschema`.

---

## Supported File Types

### Configuration File
- `.json`
- `.yaml`
- `.yml`

### Schema File
- Valid JSON Schema  
- `.json`, `.yaml`, or `.yml`

---

## Project Structure (Example)

```text
.
├── config_checker.py
├── app_config.yaml
├── schema.json
└── README.md
```

---

## How It Works

1. Loads the configuration file (JSON or YAML)
2. Loads the schema file
3. Validates the configuration using `jsonschema.validate`
4. Exits successfully if valid, otherwise raises an error

---

## Error Handling

- ❌ Unsupported file formats raise a `ValueError`
- ❌ Schema violations raise `jsonschema.ValidationError`
- ❌ Invalid JSON/YAML syntax raises parsing errors

This behavior is intentional to stop invalid configurations early.

---

## Use Cases

- Configuration validation for scripts or services  
- Pre-deployment checks in CI/CD pipelines  
- Local validation before committing config changes  
- Learning or experimenting with JSON Schema  

---

## Possible Enhancements

- Add `--verbose` or `--quiet` flags  
- Support validating multiple config files  
- Improve error formatting  
- Add exit codes for CI/CD integration  

---

## License

MIT License
