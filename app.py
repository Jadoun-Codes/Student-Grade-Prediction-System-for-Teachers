import streamlit as st
import pandas as pd
from io import BytesIO

from analytics import Analytics
from grading import GradeManager


st.set_page_config(
    page_title="Student Grade Prediction System",
    layout="wide"
)

st.title("🎓 Student Grade Prediction System")

st.write("Upload student marks and automatically generate grades and risk analysis.")

st.sidebar.title("Navigation")
st.sidebar.info("Student Grade Prediction System")

st.markdown("---")

# Upload Excel File
uploaded_file = st.file_uploader(
    "Upload Student Dataset",
    type=["xlsx"]
)

if uploaded_file is not None:

    df = pd.read_excel(uploaded_file)

    # Remove unnamed columns
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

    st.success("Dataset Uploaded Successfully")

st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

st.write(f"Rows: {df.shape[0]}")
st.write(f"Columns: {df.shape[1]}")

st.subheader("📈 Dataset Summary")
st.dataframe(df.describe())
    st.markdown("---")

    # Statistics
    st.subheader("📊 Class Statistics")

    col1, col2, col3, col4 = st.columns(4)

    highest = df["FINAL"].max()
    lowest = df["FINAL"].min()
    average = round(df["FINAL"].mean(), 2)
    total_students = len(df)

    col1.metric("Highest Marks", highest)
    col2.metric("Lowest Marks", lowest)
    col3.metric("Average Marks", average)
    col4.metric("Students", total_students)

    st.markdown("---")

    # Grade Configuration
    st.subheader("📝 Teacher Grade Configuration")

    st.write("Enter Grade Ranges")

    grade_rules = []

    grades = ["O", "A", "B", "C", "D", "F"]

    for grade in grades:

        col1, col2 = st.columns(2)

        min_marks = col1.number_input(
            f"{grade} Min Marks",
            min_value=0,
            max_value=100,
            value=0,
            key=f"{grade}_min"
        )

        max_marks = col2.number_input(
            f"{grade} Max Marks",
            min_value=0,
            max_value=100,
            value=100,
            key=f"{grade}_max"
        )

        grade_rules.append(
            (
                min_marks,
                max_marks,
                grade
            )
        )

    st.markdown("---")

    if st.button("Generate Grades & Risk"):

        # Apply Grades
        df = GradeManager.apply_grades(
            df,
            grade_rules
        )

        # Generate Risk
        df = GradeManager.generate_risk(df)

        st.success(
            "Grades and Risk Generated Successfully"
        )

        st.subheader("📋 Result Preview")

        st.dataframe(df)

        # Grade Distribution
        st.subheader("📈 Grade Distribution")

        st.bar_chart(
            df["GRADE"].value_counts()
        )

        # Risk Distribution
        st.subheader("⚠ Risk Distribution")

        st.bar_chart(
            df["RISK"].value_counts()
        )

        # Excel Export
        output = BytesIO()

        with pd.ExcelWriter(
            output,
            engine="xlsxwriter"
        ) as writer:

            df.to_excel(
                writer,
                index=False,
                sheet_name="Results"
            )

        excel_data = output.getvalue()

        st.download_button(
            label="⬇ Download Updated Excel",
            data=excel_data,
            file_name="graded_students.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )