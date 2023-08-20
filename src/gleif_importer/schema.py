from typing import Any

from pydantic import BaseModel, Field, model_validator


class Schema(BaseModel):
    lei: str = Field(alias="LEI")
    legal_name: str = Field(alias="Entity.LegalName")
    address_line_1: str | None = Field(
        None, alias="Entity.LegalAddress.FirstAddressLine"
    )
    address_line_2: str | None = Field(
        None, alias="Entity.LegalAddress.AdditionalAddressLine.1"
    )
    city: str | None = Field(None, alias="Entity.LegalAddress.City")
    country: str | None = Field(None, alias="Entity.LegalAddress.Country")
    postal_code: str | None = Field(None, alias="Entity.LegalAddress.PostalCode")

    class Config:
        populate_by_name = True
        use_enum_values = True

    @model_validator(mode="before")
    @classmethod
    def check_empty_string(cls, data: Any) -> Any:
        for key, value in data.items():
            if value == "":
                data[key] = None
        return data
