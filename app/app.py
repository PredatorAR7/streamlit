import streamlit as st

def main():
    print("entered to streamlit")
    # log_message("Streamlit app loaded")
    st.write(" streamlit app loaded")

    st.title("🌸 Blossom Identifier: Unveil the Secrets of Flowers 🌺")

    # Updated fun and engaging description
    st.write("""
    ## Welcome to the Blossom Identifier! 🎉 version - 2
    Imagine you're wandering through a magical garden, and you spot a flower that captures your eye. But what's its name? With the **Blossom Identifier**, you're just a click away from discovering the secrets of the floral world.
    
    Our app uses AI superpowers to identify flowers from just a picture. However, even superheroes have their limits. Currently, our botanical expertise extends to five enchanting varieties: **daisies, dandelions, roses, sunflowers, and tulips**. So if you've got one of these, you're in luck! 🌼🌹🌻🌷

    ### Here's How to Uncover Flower Names:
    - **Step 1**: Capture the beauty of the flower with your camera or find its image online.
    - **Step 2**: Paste the image URL below.
    - **Step 3**: Press "Identify" and watch the magic happen! The name of the flower and how sure we are about it will bloom on the screen.

    Ready to test the limits of this botanical oracle? Let's dive into the garden of mysteries and see which flowers we can name together! 🚀🌸
    """)

    # Creating two columns for input and output
    col1, col2 = st.columns([8, 2], gap="large")
    
    with col1:  # Input column
        flower_url = st.text_input("Enter Flower Image URL:")
        if flower_url:
            st.image(flower_url, caption="Uploaded Flower Image", use_column_width=True)
    
    # Assign a unique key to the button by passing the `key` parameter
    identify_button = st.button("Identify", key="identify_button")
    

if __name__ == "__main__":
    main()
