# Module 02: Layered Project Layout, Health Endpoint & Automated Testing

## 1. Architectural Philosophy: Layered Modular API Architecture

The backend implements a **Layered Architecture** with strict separation of concerns, eliminating cross-domain coupling and circular imports:

- **`src/api/` (Transport & Routing Layer):** Exposes HTTP routes, marshals inputs/outputs, and handles status codes. Contains zero database queries or core business algorithms.
- **`src/schemas/` (Data Transfer Objects - DTOs):** Governed by Pydantic models. Validates incoming payload shapes, coerces types, strips forbidden fields, and shapes responses.
- **`src/services/` (Business Logic Layer):** Contains domain rules, invariant validations (e.g., verifying requester status before volunteer dispatch), and transaction coordinators.
- **`src/models/` (Persistence Layer):** Houses SQLAlchemy declarative mappings mirroring the PostgreSQL relational schema.
- **`src/core/` (Configuration & Cross-Cutting Concerns):** Houses application settings, security policies, and environment parsers.
- **`src/db/` (Database Session & Migrations):** Manages connection pool life cycles and Alembic database version control scripts.

---

## 2. Configuration Management: `src/core/config.py`

### Line-by-Line Breakdown

```python
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Share Help API"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"

    model_config = SettingsConfigDict(case_sensitive=True)


settings = Settings()
```
