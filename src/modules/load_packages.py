import streamlit as st
import pandas as pd
import openai
import os



openai.api_key = os.environ.get("OPENAI_API_KEY")