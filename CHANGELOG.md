# Changelog

## [1.1.0] - 2025-07-21

### Added
- Support for `--password` flag to `ari add` (by @bsam05443)
- Support for `--passphrase` flag to `ari add` (by @bsam05443)
- `ari run` securely prompts for password and/or SSH key passphrase if configured
- Updated `config.py` to persist these options in your aliases JSON

---

## [1.0.0] - 2025-07-20

### Added
- Initial release with core SSH alias manager features: add, delete, list, run, import/export, backup, rename, update, status.