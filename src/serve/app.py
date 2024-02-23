"""Streamlit app."""

from importlib.metadata import version

import streamlit as st

st.title(f"Poetry Cookiecutter v{version('poetry-cookiecutter')}")  # type: ignore[no-untyped-call]
