import streamlit as st
from news_scraper import get_sl_news
from social_monitor import get_reddit_trends
from processor import analyze_news  # Import the new function name

st.set_page_config(page_title="ModelX: SL Business Intel", page_icon="🇱🇰", layout="wide")

st.title("🇱🇰 ModelX: Strategic Situational Awareness")
st.markdown("Real-time categorization and risk assessment for Sri Lankan industries.")
st.divider()

if st.button("🔄 Refresh Data"):
    st.cache_data.clear()
    st.rerun()

col1, col2 = st.columns([1.5, 1])

# --- COLUMN 1: CATEGORIZED NEWS ---
with col1:
    st.subheader("📰 Categorized Market Intelligence")
    
    # Fetch news
    try:
        news_items = get_sl_news()
    except:
        news_items = []
        st.error("Connection error to news source.")

    if news_items:
        for headline in news_items:
            # Analyze using the new logic
            data = analyze_news(headline)
            
            # Create a Card-like layout using a container
            with st.container():
                # Color code based on Status
                if "Risk" in data['status']:
                    st.error(f"🚨 **{headline}**")
                else:
                    st.success(f"**{headline}**")
                
                # Display Tags (Industry | Location | Time)
                c1, c2, c3 = st.columns(3)
                c1.caption(f"🏭 **{data['industry']}**")
                c2.caption(f"📍 **{data['location']}**")
                c3.caption(f"⏳ **{data['timeline']}**")
                
                # Display Advice if any
                if data['advice']:
                    for tip in data['advice']:
                        st.info(f"💡 Action: {tip}")
                
                st.divider() # Visual separator
    else:
        st.write("No news data available.")

# --- COLUMN 2: SOCIAL & RISKS ---
with col2:
    st.subheader("🛡️ Risk Overview")
    
    # We can aggregate stats here
    st.markdown("#### Industry Heatmap (Live)")
    
    # Calculate counts dynamically
    if news_items:
        industry_counts = {}
        for item in news_items:
            cat = analyze_news(item)['industry']
            industry_counts[cat] = industry_counts.get(cat, 0) + 1
        
        # Display top affected industries
        st.bar_chart(industry_counts)

    st.subheader("🗣️ Social Signals")
    reddit_data = get_reddit_trends()
    if reddit_data:
        for post in reddit_data:
            st.markdown(f"• [{post['title']}]({post['link']})")