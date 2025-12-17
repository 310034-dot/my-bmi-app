import streamlit as st

# 原始計算邏輯
def calculate_bmi(w, h_m): return round(w / (h_m**2), 2) if h_m > 0 else 0
def calculate_bmr(w, h_cm, age, gender):
    val = (10 * w) + (6.25 * h_cm) - (5 * age)
    return round(val + 5, 0) if gender == 'M' else round(val - 161, 0)

# 網頁介面
st.title("🚀 體重變化快速模擬器")
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("性別", ["M", "F"])
    height = st.number_input("身高 (cm)", value=175.0)
    weight = st.number_input("體重 (kg)", value=70.0)
with col2:
    age = st.number_input("年齡", value=25)
    activity = st.select_slider("活動量", options=[1.2, 1.375, 1.55, 1.725, 1.9])
    intake = st.number_input("每日攝取熱量", value=2000)

bmr = calculate_bmr(weight, height, age, gender)
tdee = bmr * activity
diff = intake - tdee
pred_weight = weight + (diff * 30 / 7700)

st.divider()
st.metric("您的 TDEE (每日總消耗)", f"{tdee:.0f} kcal")
st.subheader(f"📅 30 天後預測：{pred_weight:.2f} kg")

if diff < 0:
    st.success(f"🔥 預計減重: {abs(pred_weight - weight):.2f} kg")
else:
    st.warning(f"⚠️ 預計增重: {abs(pred_weight - weight):.2f} kg")
