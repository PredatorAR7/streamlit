import streamlit as st

def extract_websocket_api_key():
    """Extract API key from WebSocket headers in Streamlit."""
    try:
        cookies = st.context.cookies
        if cookies and 'vps-auth-token' in cookies and len(cookies['vps-auth-token']) > 0:
            return cookies['vps-auth-token']
        else:
            return ""
    except Exception as e:
        return str(e)

def extract_websocket_app_id():
    """Extract app id from WebSocket headers in Streamlit."""
    try:
        cookies = st.context.cookies
        if cookies and 'vps-app-id' in cookies and len(cookies['vps-app-id']) > 0:
            return cookies['vps-app-id']
        else:
            return ""
    except Exception as e:
        return str(e)

# Streamlit app
st.title("WebSocket API Key and App ID Extractor")

# Extract API Key
api_key = extract_websocket_api_key()
if api_key:
    st.success(f"API Key: {api_key}")
else:
    st.warning("No API Key found in cookies.")

# Extract App ID
app_id = extract_websocket_app_id()
if app_id:
    st.success(f"App ID: {app_id}")
else:
    st.warning("No App ID found in cookies.")
